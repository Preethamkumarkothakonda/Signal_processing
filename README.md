# Signal_processing
# DSP Project: Real-Time Audio Processing and Filtering

This project demonstrates real-time audio processing, including capturing audio, visualizing signals, and applying a low-pass filter. The project captures audio input from a microphone, applies a filter, and visualizes the input and filtered signals in both the time and frequency domains. The filtered audio can also be played back for comparison.

## Project Phases

### 1. Signal Generation
- Audio is captured from the microphone and stored as input for further processing.

### 2. Fourier Transform and Analysis
- The frequency spectrum of the captured audio is analyzed using the Fast Fourier Transform (FFT).
- The input audio and its frequency spectrum are visualized.

### 3. Filtering and Signal Processing
- A low-pass filter is applied to the input audio to remove frequencies above a certain threshold.
- The filtered audio is saved and visualized.

### 4. Visualization
- Four graphs are generated:
  1. Input audio (time-domain).
  2. Input audio frequency spectrum.
  3. Filtered audio (time-domain).
  4. Filtered audio frequency spectrum.
- The audio can be played back for comparison between the original and filtered audio.

## Features
- **Real-Time Audio Capture**: Captures live audio input from the microphone.
- **Fourier Analysis**: Performs FFT to analyze and visualize the frequency spectrum of the input signal.
- **Low-Pass Filtering**: Applies a Butterworth low-pass filter to remove high-frequency components.
- **Visualization**: Plots the time-domain and frequency-domain signals for both input and filtered audio.
- **Audio Playback**: Plays back both the input and filtered audio for easy comparison.

## Requirements

To run this project, you'll need to install the following Python libraries:

- `numpy`
- `matplotlib`
- `scipy`
- `sounddevice`
- `soundfile`

You can install them using `pip`:

```bash
pip install numpy matplotlib scipy sounddevice soundfile
