import librosa
import numpy as np
import imagehash
from PIL import Image
import shutil
import json
from pathlib import Path

# Extract features from the WAV file
def extractFeatures(wavFile):
    loadedSound, samplingRate = librosa.load(wavFile, sr=None) # loadedSound is an array containing the amplitudes, sr is set to none so that it uses the original sampling rate
    features = {
        "mfcc": librosa.feature.mfcc(y=loadedSound, sr=samplingRate).mean(axis=1), # Mel-Frequency Cepstral Coefficients represents power spectrum (timbre) of the sound
        "chroma": librosa.feature.chroma_stft(y=loadedSound, sr=samplingRate).mean(axis=1), # Represents harmonic content (energy distribution across 12 different pitch classes)
        "spectralContrast": librosa.feature.spectral_contrast(y=loadedSound, sr=samplingRate).mean(axis=1), # Represents difference in amplitude between peaks and valleys
        # Measures the frequency below which a certain percentage (85%) of the total spectral energy lies, helpful for differentiating vocals from instrumental parts
        "spectralRollof": librosa.feature.spectral_rolloff(y=loadedSound, sr=samplingRate).mean(axis=1),
        "onsetStrength": librosa.onset.onset_strength(y=loadedSound, sr=samplingRate), # Measures the intensity (like beats) at each frame in the audio
    }
    # .mean(axis=1) gets us the average value across all the columns (time), resulting in a 1D array
    return features

# Normalize features and convert to a 2D array
def normalizeFeatures(features):
    # Concatenate the arrays containing the features into a 1D array
    featuresList = np.hstack([
        features["mfcc"],
        features["chroma"],
        features["spectralContrast"],
        features["spectralRollof"],
    ])
    # Scales the feature values so that the minimum becomes 0, and the maximum becomes 255, needed for perceptual hashing
    featuresList = (featuresList - np.min(featuresList)) / (np.max(featuresList) - np.min(featuresList)) * 255
    featuresList = featuresList.astype(np.uint8)
    return featuresList

# Compute the perceptual hash
def hashFeatures(featuresList):
    image = Image.fromarray(featuresList) # Converts an array into an image object
    hashedFeatures = imagehash.phash(image) # Creates a hash value that represents the visual (perceptual) content of an image ignoring slight variations that aren't percieved
    return str(hashedFeatures) # Hexadecimal representation of the hashing making it easier to store

# Process the hashed features
def processHash(wavFile):
    features = extractFeatures(wavFile)
    featuresList = normalizeFeatures(features)
    featuresHash = hashFeatures(featuresList)

    return featuresHash

# Save the hashed features locally
def saveHash(wavFile, featuresHash, outputDirectory):
    # Prepares the data to be saved in a JSON file
    result = {
        "featuresHash": featuresHash
    }

    # Creates the output directory
    outputDirectory.mkdir(parents=True, exist_ok=True)

    # Creates the output file path
    outputFile = outputDirectory / wavFile.with_suffix(".json").name # .name extract the file name part without the path (after it was changed from .wav to .json)

    with open(outputFile, "w") as f:
        json.dump(result, f, indent=4) # The indent=4 argument makes the JSON output pretty printed 
    
# Loop over our dataset and save the computed hashed features for each song file
inputDirectory = Path("./task5_data")
outputDirectory = Path("./task5_hashes")
if outputDirectory.exists():
        shutil.rmtree(outputDirectory)

for file in inputDirectory.glob("*.wav"):
    hashedFeatures = processHash(file)
    saveHash(file, hashedFeatures, outputDirectory)