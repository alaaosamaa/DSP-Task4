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
from PIL import Image
import imagehash

# >>> print(hash)
# d879f8f89b1bbf
# >>> otherhash = imagehash.average_hash(Image.open('other.bmp'))
# >>> print(otherhash)
# ffff3720200ffff
# >>> print(hash == otherhash)
# False
# >>> print(hash - otherhash)
# 36


class loop():
    def __init__(self):    
        super(loop, self).__init__()
        self.specArr=[]
        self.mfccArr=[]
        self.fluxArr=[]
        self.hashArr=[]

    def loopFiles(self):
        directory = os.fsdecode('Songs')
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            # filename=os.getcwd() + filename
            filename=os.path.join(directory, filename)
            if filename.endswith(".wav"):
                # print(filename)
                # print(os.path.join(directory, filename))
                sample_rate, sample = wavfile.read(filename)
                sample=sample[0:60*sample_rate]
                # print(sample_rate)
                # #spectrogram
                spectro, freqs, time, self.img = plt.specgram(sample, NFFT=None, Fs=sample_rate)
                self.specArr.append(spectro)
                pylab.savefig('loopsepcto.jpg', bbox_inches='tight')
                # hashing

                hash = imagehash.average_hash(Image.open('loopsepcto.jpg'))
                self.hashArr.append(hash)

                # Features
                # mfcc
                mfcc_feat = mfcc(sample,sample_rate)
                mfcc_data= np.swapaxes(mfcc_feat, 0 ,1)
                self.mfccArr.append(mfcc_data)

                # # to get flux
                # X=spectro
                # # difference spectrum (set first diff to zero)
                # X = np.c_[X[:, 0], X]
                # X = np.concatenate(X[:,0],X, axis=1)
                # afDeltaX = np.diff(X, 1, axis=1)
                # # flux
                # vsf = np.sqrt((afDeltaX**2).sum(axis=0)) / X.shape[0]
                # self.fluxArr.append(vsf)     



        print(self.specArr)
        print("mfccArr")
        print(self.mfccArr)
        print("hash")
        # print(self.hashArr)
        




def main(): 
    loop2=loop()
    loop2.loopFiles()




if __name__ == "__main__":
    main()

    