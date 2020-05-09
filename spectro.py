import matplotlib.pyplot as plt
from matplotlib import pylab
# import pylab 
from scipy import signal
from scipy.io.wavfile import write
import os
import sys
import tkinter.messagebox
import warnings
import wave
import numpy as np
from scipy.io import wavfile
from ui import Ui_MainWindow
from pydub import AudioSegment
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import QTime, QTimer
import sys
import cv2
import pyqtgraph as pg
import matplotlib as mp
# from scipy import signal
# import librosa
# import librosa.display
# import IPython.display as ipd
from python_speech_features import mfcc
import numpy as np
from playsound import playsound


warnings.simplefilter("ignore", DeprecationWarning)


# playsound('Songs\eminem-lose_yourself001.wav')
# self.sample_rate, self.originalSamples = wavfile.read('Songs\eminem-lose_yourself001.wav')
# self.originalSamples=self.originalSamples[0:60*self.sample_rate]

# #spectrogram
# spectro, freqs, time, self.img = plt.specgram(self.originalSamples, NFFT=None, Fs=self.sample_rate)
# print(spectro)

# # mfcc
# mfcc_feat = mfcc(self.originalSamples,self.sample_rate)
# print("mfcc")
# print(mfcc_feat)
# ig, ax = plt.subplots()
# mfcc_data= np.swapaxes(mfcc_feat, 0 ,1)
# print("mfcc_data")
# print(mfcc_data)
# cax = ax.imshow(mfcc_data, interpolation='nearest', origin='lower', aspect='auto')
# ax.set_title('MFCC')
# plt.show()

# X=spectro

# # to get flux
# # difference spectrum (set first diff to zero)
# X = np.c_[X[:, 0], X]
# # X = np.concatenate(X[:,0],X, axis=1)
# afDeltaX = np.diff(X, 1, axis=1)

# # flux
# vsf = np.sqrt((afDeltaX**2).sum(axis=0)) / X.shape[0]
# print("vsf")
# print(vsf)
# plt.plot(vsf)
# plt.show()

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Path1 = str
        self.Path2 = str
        self.Path3 = str
        self.ui.browse1.clicked.connect(lambda: self.BROWSE(1))
        self.ui.browse2.clicked.connect(lambda: self.BROWSE(2))
        self.ui.Play.clicked.connect(self.playSong)
        self.imgArr = []
        self.sample1 = []
        self.sample2 = []
        self.sample_rate = int
        self.originalSamples = []
        self.mixed = []
        self.img = []


    def BROWSE(self,Number):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filepath, _ = QFileDialog.getOpenFileName(None, 'Browse Song', '', "Image Files (*.wav *.,p3)", options = options)
        if (Number == 1):
            self.Path1 = filepath
            self.plot(self.Path1,1)
        elif (Number == 2):
            self.Path2 = filepath
            self.plot(self.Path2,2)

    def fileRead(self,path):
        self.sample_rate, self.originalSamples = wavfile.read(path)
        self.originalSamples = self.originalSamples[0:60*self.sample_rate]
        return self.originalSamples, self.sample_rate

    def spectro(self,data):
        spectro, freqs, time, self.img = plt.specgram(self.originalSamples, NFFT=None, Fs=self.sample_rate)
        return spectro


    def plot(self,path,Numb):
        plotting = plt.subplot(111, frameon = False)
        plotting.get_xaxis().set_visible(False)
        plotting.get_yaxis().set_visible(False)
        
        self.originalSamples, self.sample_rate = self.fileRead(path)
        spectro = self.spectro(self.originalSamples)

        if (path == self.Path1):
            self.sample1 = self.originalSamples
            spectro1 = spectro
            pylab.savefig('sepcto1.jpg', bbox_inches='tight')
            self.imgArr = cv2.imread('sepcto1.jpg')
        if (path == self.Path2):
            self.sample2 = self.originalSamples
            spectro2 = spectro
            pylab.savefig('sepcto2.jpg', bbox_inches='tight')
            self.imgArr = cv2.imread('sepcto2.jpg')
        if (path == self.Path3):
            spectro3 = spectro
            pylab.savefig('sepcto3.jpg', bbox_inches='tight')
            self.imgArr = cv2.imread('sepcto3.jpg')
        
        self.img = pg.ImageItem(np.rot90(self.imgArr,3))
        if Numb == 1:
            self.ui.song1.clear()
            self.ui.song1.addItem(self.img)
        elif Numb == 2:
            self.ui.song2.clear()
            self.ui.song2.addItem(self.img)
            self.mix()
        elif Numb == 3:
            self.ui.mixedsong.clear()
            self.ui.mixedsong.addItem(self.img)

    def readSong(self, path):
        wav = wave.open(path, 'r')
        frames = wav.readframes(-1)
        soundData = pylab.fromstring(frames, 'Int16')
        frameRate = wav.getframerate()
        wav.close()
        return soundData

    def mix(self):
        sound1 = self.readSong(self.Path1)
        sound1Audio = AudioSegment.from_file(self.Path1)
        sound2 = self.readSong(self.Path2)
        sound2Audio = AudioSegment.from_file(self.Path2)
        self.mixed = np.add(np.multiply(sound1, self.ui.song1Slider.value()), np.multiply(sound2, self.ui.song2Slider.value()))
        combined = sound1Audio.overlay(sound2Audio)
        mixedFilename = '/mixing.wav'
        combined.export(os.getcwd() + mixedFilename, format = 'wav')
        write("Mixed.wav", 44100, self.mixed)
        self.Path3=os.getcwd() + "/Mixed.wav"
        self.plot(self.Path3,3)

        # sound = AudioSegment.get_array_of_samples
        # print(sound)
        #sound1sample = self.ui.song1Slider.value() * self.sample1
        #  #sound2sample = self.ui.song2Slider.value() * self.sample2
        
        # self.mixed = sound1sample + sound2sample
        # mixx = self.spectro(self.mixed)
        
        # obj = wave.open('newfile','w') 
        # obj.writeframes(mixx)
        # obj.setframerate(self.sample_rate)
        # obj.close()

    def playSong(self):
        playsound("Mixed.wav")
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()



if __name__ == "__main__":
    main()
