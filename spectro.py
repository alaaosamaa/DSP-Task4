
import matplotlib.pyplot as plt
import matplotlib as mp

# from scipy import signal
from scipy.io import wavfile
# import librosa
# import librosa.display
# import IPython.display as ipd
from python_speech_features import mfcc
import numpy as np
from playsound import playsound


playsound('Songs\eminem-lose_yourself001.wav')
sample_rate, samples = wavfile.read('Songs\eminem-lose_yourself001.wav')
samples=samples[0:60*sample_rate]

#spectrogram
spectro, freqs, time, img = plt.specgram(samples, NFFT=None, Fs=sample_rate)
print(spectro)

# mfcc
mfcc_feat = mfcc(samples,sample_rate)
print("mfcc")
print(mfcc_feat)
ig, ax = plt.subplots()
mfcc_data= np.swapaxes(mfcc_feat, 0 ,1)
print("mfcc_data")
print(mfcc_data)
cax = ax.imshow(mfcc_data, interpolation='nearest', origin='lower', aspect='auto')
ax.set_title('MFCC')
plt.show()

X=spectro

# to get flux
# difference spectrum (set first diff to zero)
X = np.c_[X[:, 0], X]
# X = np.concatenate(X[:,0],X, axis=1)
afDeltaX = np.diff(X, 1, axis=1)

# flux
vsf = np.sqrt((afDeltaX**2).sum(axis=0)) / X.shape[0]
print("vsf")
print(vsf)
plt.plot(vsf)
plt.show()
