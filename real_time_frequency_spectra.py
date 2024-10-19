import numpy as np
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq

# Audio settings
fs = 8000  # Sample rate in Hz
duration = 10  # Duration of audio capture in seconds
cutoff_frequency = 300  # Low-pass filter cutoff frequency in Hz
order = 10  # Filter order

# File names for saving
input_audio_file = 'input_audio.wav'
filtered_audio_file = 'filtered_audio.wav'

# Low-pass filter design
sos = signal.butter(order, cutoff_frequency, 'low', fs=fs, output='sos')

# Buffer to store captured audio data
audio_data = []

# Callback function to capture audio input
def audio_callback(indata, frames, time, status):
    if status:
        print(f"Error: {status}")
    audio_data.extend(indata[:, 0])  # Collect audio data

# Start capturing the audio from the microphone for 10 seconds
print(f"Recording for {duration} seconds...")
with sd.InputStream(callback=audio_callback, channels=1, samplerate=fs):
    sd.sleep(duration * 1000)  # Record for 10 seconds

# Convert the recorded data to a numpy array
audio_data = np.array(audio_data)

# Save the input audio to a file
sf.write(input_audio_file, audio_data, fs)
print(f"Input audio saved to {input_audio_file}")

# Apply low-pass filtering
filtered_audio = signal.sosfilt(sos, audio_data)

# Save the filtered audio to a file
sf.write(filtered_audio_file, filtered_audio, fs)
print(f"Filtered audio saved to {filtered_audio_file}")

# Visualize the frequency spectra
def plot_frequency_spectrum(signal, sample_rate, title):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / sample_rate)[:N // 2]
    plt.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
    plt.grid()
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')

# Plot all four: input and filtered signals and their frequency spectra
plt.figure(figsize=(12, 10))

# Time-domain plot of input audio
plt.subplot(4, 1, 1)
plt.plot(np.linspace(0, duration, len(audio_data)), audio_data)
plt.title('Input Audio (Time Domain)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

# Frequency spectrum of input audio
plt.subplot(4, 1, 2)
plot_frequency_spectrum(audio_data, fs, 'Input Audio (Frequency Spectrum)')

# Time-domain plot of filtered audio
plt.subplot(4, 1, 3)
plt.plot(np.linspace(0, duration, len(filtered_audio)), filtered_audio)
plt.title('Filtered Audio (Time Domain)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

# Frequency spectrum of filtered audio
plt.subplot(4, 1, 4)
plot_frequency_spectrum(filtered_audio, fs, 'Filtered Audio (Frequency Spectrum)')

plt.tight_layout()
plt.show()

# Play back the original and filtered audio for comparison
print("Playing the original audio...")
sd.play(audio_data, fs)
sd.wait()  # Wait until playback is finished

print("Playing the filtered audio...")
sd.play(filtered_audio, fs)
sd.wait()  # Wait until playback is finished

print("Audio playback complete!")
