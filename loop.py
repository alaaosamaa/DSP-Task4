import matplotlib.pyplot as plt
from matplotlib import pylab
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
from python_speech_features import mfcc
import numpy as np
from playsound import playsound




class loop():
    def __init__(self):    
        super(loop, self).__init__()
        self.specArr=[]
        self.mfccArr=[]
    
    def loopFiles(self):
        directory = os.fsdecode('Songs')
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            # filename=os.getcwd() + filename
            filename=os.path.join(directory, filename)
            if filename.endswith(".wav"):
                print(filename)
                # print(os.path.join(directory, filename))
                self.sample_rate, self.originalSamples = wavfile.read(filename)
                self.originalSamples=self.originalSamples[0:60*self.sample_rate]
                # #spectrogram
                spectro, freqs, time, self.img = plt.specgram(self.originalSamples, NFFT=None, Fs=self.sample_rate)
                self.specArr.append(spectro)
                # mfcc
                mfcc_feat = mfcc(self.originalSamples,self.sample_rate)
                # print("mfcc")
                # print(mfcc_feat)
                # ig, ax = plt.subplots()
                mfcc_data= np.swapaxes(mfcc_feat, 0 ,1)
                self.mfccArr.append(mfcc_data)
                # print("mfcc_data")
                # print(mfcc_data)
                # cax = ax.imshow(mfcc_data, interpolation='nearest', origin='lower', aspect='auto')
                # ax.set_title('MFCC')
                # plt.show()

        print(self.specArr)
        print("mfccArr")
        print(self.mfccArr)




def main(): 
    loop2=loop()
    loop2.loopFiles()




if __name__ == "__main__":
    main()

    