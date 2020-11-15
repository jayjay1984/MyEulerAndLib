import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np


fig, ax = plt.subplots(nrows=1, sharex=True, sharey=True)

y, sr = librosa.load("test_sound.wav", duration=10)
#y, sr = librosa.load(librosa.ex('choice'), duration=15)

librosa.display.waveplot(y, sr=sr, ax=ax)
ax.set(title='test')
ax.label_outer()

fig2, ax2 = plt.subplots(nrows=2, ncols=1, sharex=True)
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
                               sr=sr, ax=ax2[0])
ax2[0].set(title='Linear-frequency power spectrogram')
ax2[0].label_outer()

hop_length = 1024
D = librosa.amplitude_to_db(np.abs(librosa.stft(y, hop_length=hop_length)),
                            ref=np.max)
librosa.display.specshow(D, y_axis='log', sr=sr, hop_length=hop_length,
                         x_axis='time', ax=ax2[1])
ax2[1].set(title='Log-frequency power spectrogram')
ax2[1].label_outer()
fig2.colorbar(img, ax=ax2, format="%+2.f dB")

plt.show()
