import soundfile as sf

# Read audio file
audio, sample_rate = sf.read("temp_mic.wav")
audio, sample_rate = sf.read(r"data\test\TestAudio.wav")

# Extract properties
num_channels = audio.shape[1]
duration = audio.shape[0] / sample_rate
sample_width = audio.dtype.itemsize

# Print properties
print("Sample rate:", sample_rate)
print("Number of channels:", num_channels)
print("Duration:", duration, "seconds")
print("Sample width:", sample_width, "bytes")
