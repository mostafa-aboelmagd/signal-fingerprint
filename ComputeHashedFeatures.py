import librosa
import numpy as np
import imagehash
from PIL import Image

# Extract features from the WAV file
def extractFeatures(loadedSound, samplingRate):    
    features = {
        "mfcc": librosa.feature.mfcc(y=loadedSound, sr=samplingRate), # Mel-Frequency Cepstral Coefficients represents power spectrum (timbre or quality) of the sound
        "chroma": librosa.feature.chroma_cqt(y=loadedSound, sr=samplingRate), # Represents harmonic content (energy distribution across 12 different pitch classes)
        "melSpectrogram": librosa.feature.melspectrogram(y=loadedSound, sr=samplingRate),
    }

    return features

# Normalize features and convert to a 2D array
def normalizeFeatures(features):
    featuresList = []
    # Normalize each feature between 0 and 255 as perceptual hashing will treat the features as an image object
    for key in features:
        currFeature = features[key]
        featuresList.append((currFeature - np.min(currFeature)) / (np.max(currFeature) - np.min(currFeature)) * 255)

    # Combine features into a 2D array (stack rows vertically)
    featuresMatrix = np.vstack(featuresList).astype(np.uint8)
    return featuresMatrix

# Compute the perceptual hash
def hashFeatures(featuresMatrix):
    image = Image.fromarray(featuresMatrix) # Converts an array into an image object
    hashedFeatures = imagehash.phash(image) # Creates a hash value that represents the visual (perceptual) content of an image ignoring slight variations that aren't percieved
    return str(hashedFeatures) # Hexadecimal representation of the hashing making it easier to store

# Process the hashed features
def processHash(loadedSound, samplingRate):
    features = extractFeatures(loadedSound, samplingRate)
    featuresMatrix = normalizeFeatures(features)
    featuresHash = hashFeatures(featuresMatrix)
    return featuresHash