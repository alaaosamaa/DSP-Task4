import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pylab
from scipy import signal
import os
import sys
import tkinter.messagebox
import warnings
import wave
from scipy.io import wavfile
from ui import Ui_MainWindow
from pydub import AudioSegment
from PyQt5 import QtGui, QtWidgets
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
# sample_rate, samples = wavfile.read('Songs\eminem-lose_yourself001.wav')
# samples=samples[0:60*sample_rate]

# #spectrogram
# spectro, freqs, time, img = plt.specgram(samples, NFFT=None, Fs=sample_rate)
# print(spectro)

# # mfcc
# mfcc_feat = mfcc(samples,sample_rate)
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
                self.Path1=str
                self.Path2=str
                self.ui.browse1.clicked.connect(lambda: self.BROWSE(1))
                self.ui.browse2.clicked.connect(lambda: self.BROWSE(2))


        def BROWSE(self,Number):
                filepath, _ =QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '/home', "Image Files (*.wav *.,p3)")
                if (Number==1):
                        self.Path1 = filepath
                        self.specto(self.Path1,1)
                elif (Number==2):
                        self.Path2 = filepath
                        self.specto(self.Path2,2)

    


        def specto(self,path,Numb):
                print(path)
                wav = wave.open(path, 'r')
                frames = wav.readframes(-1)
                soundData = pylab.fromstring(frames, 'Int16')
                frameRate = wav.getframerate()
                wav.close()
                soundData=soundData[0:60*frameRate]
                plotting = pylab.subplot(111, frameon=False)
                plotting.get_xaxis().set_visible(False)
                plotting.get_yaxis().set_visible(False)
                spectro= plt.specgram(soundData, Fs=frameRate)
                pylab.savefig('sepcto.jpg', bbox_inches='tight')

                imgArr = cv2.imread('sepcto.jpg')
                img = pg.ImageItem(imgArr)
                if Numb==1:
                        self.ui.song1.clear()
                        self.ui.song1.addItem(img)
                elif Numb==2:
                        self.ui.song2.clear()
                        self.ui.song2.addItem(img)
                        self.mix()
                elif Numb==3:
                        self.ui.mixedsong.clear()
                        self.ui.mixedsong.addItem(img)

        def mix(self):

                sound1 = AudioSegment.from_file(self.Path1)
                sound2 = AudioSegment.from_file(self.Path2)
                combined = sound1.overlay(sound2)
                mixedFilename = '/mixing.wav'
                combined.export(os.getcwd() +mixedFilename, format='wav')
                self.specto(os.getcwd() +mixedFilename,3)
        


def main():
        app = QtWidgets.QApplication(sys.argv)
        application = ApplicationWindow()
        application.show()
        app.exec_()



if __name__ == "__main__":
        main()
