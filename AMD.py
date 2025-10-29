import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#load the .wav file here
FILE_NAME = 'frontMid_e.wav'

try:
    fs, data = wavfile.read(FILE_NAME) 
except FileNotFoundError:
    print(f"Error: Audio Not Found '{FILE_NAME}'")
    exit()

if data.ndim > 1:
    data = data[:, 0]
data = data.astype(float)


#Analysis


#Forcing the search between 120-160 Hz to avoid "Double Pitch"
minFreq = 120  # Hz
maxFreq = 140  # Hz

minLag = int(fs / maxFreq)
maxLag = int(fs / minFreq)
frameLength = 1024



#Select an Audio Frame
#Find the start time in Audacity (e.g., 0.75s)
# and multiply by 44100 to get startSample.
startSample = 33075 


endSample = startSample + frameLength + maxLag

if endSample > len(data):
    print(f"Error: The audio file is too short({startSample}) is too close to the end.")
    print(f"File length is {len(data)} samples, but analysis needs to read up to {endSample}.")
    print("choose an earlier start_sample.")
    exit()

segment = data[startSample:endSample]
x1 = segment[0 : frameLength]

#Calculating the AMD Function
lags = range(minLag, maxLag)
amd_values = []

#method given in the notes of lecture “ST Analysis of Speech Signal”
print(f"Calculating AMD for lags {minLag} to {maxLag}...")
for k in lags:
    x2 = segment[k : k + frameLength]
    diff = x1 - x2
    amd_avg = np.sum(np.abs(diff)) / frameLength
    amd_values.append(amd_avg)

amd_values = np.array(amd_values)

# Pitch
valley_index = np.argmin(amd_values)
period_in_samples = lags[valley_index]
pitch_hz = fs / period_in_samples

#Plotting the Results
print(f"Calculation complete.")
print(f"Found AMD minimum at lag = {period_in_samples} samples.")
print(f"Calculated Pitch (F0) = {pitch_hz:.2f} Hz")

plt.figure(figsize=(10, 5))
plt.title("Average Magnitude Difference (AMD) Function")
plt.plot(lags, amd_values, label='AMD Values')
plt.xlabel("Lag (in samples)")
plt.ylabel("Average Magnitude Difference")
plt.axvline(x=period_in_samples, color='red', linestyle='--', 
            label=f"Pitch Period (T0) = {period_in_samples} samples")
plt.legend()
plt.grid(True)
plt.show()