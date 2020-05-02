
import matplotlib.pyplot as plt
import pylab
from scipy import signal
from scipy.io import wavfile
# import librosa
# import librosa.display
# import IPython.display as ipd

sample_rate, samples = wavfile.read('Songs\eminem-lose_yourself001.wav')
samples=samples[0:60*sample_rate]
spectro, freqs, time, img = plt.specgram(samples, NFFT=None, Fs=sample_rate)
print(spectro)
plt.show()
# x , sr = librosa.load("Songs\eminem-lose_yourself001.wav")

# librosa.display.waveplot(x, sr=sr)
#display Spectrogram
# X = librosa.stft(x)
# Xdb = librosa.amplitude_to_db(abs(X))
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(Xdb, sr=10000, x_axis='time', y_axis='hz') 
#If to pring log of frequencies  
#librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
# plt.colorbar()
# plt.show()
# print("load")
# print(type(x), type(sr))



# scipy
# frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
# plt.pcolormesh(times, frequencies, spectrogram)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')