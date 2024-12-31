import librosa
import numpy as np
import imagehash
from PIL import Image

# Extracts features from the WAV file
def extractFeatures(loadedSound, samplingRate):    
    features = {
        "mfcc": librosa.feature.mfcc(y=loadedSound, sr=samplingRate), # Mel-Frequency Cepstral Coefficients represents power spectrum (timbre or quality) of the sound
        "chroma": librosa.feature.chroma_cqt(y=loadedSound, sr=samplingRate), # Represents harmonic content (energy distribution across 12 different pitch classes)
        "melSpectrogram": librosa.feature.melspectrogram(y=loadedSound, sr=samplingRate),
    }

    return features

# Normalizes features and convert to a 2D array
def normalizeFeatures(features):
    featuresList = []
    # Normalizes each feature between 0 and 255 as perceptual hashing will treat the features as an image object
    for key in features:
        currFeature = features[key]
        featuresList.append((key, (currFeature - np.min(currFeature)) / (np.max(currFeature) - np.min(currFeature)) * 255))

    return featuresList

# Computes the perceptual hash
def hashFeatures(featuresList):
    hashedFeaturesDict = {}
    for key, normalizedFeature in featuresList:
        image = Image.fromarray(normalizedFeature) # Converts individual feature into an image object
        hashedFeature = imagehash.phash(image, hash_size=16) # Creates a hash value that represents the visual (perceptual) content of an image ignoring slight variations that aren't percieved
        hashedFeaturesDict[key] = str(hashedFeature) # Hexadecimal representation of the hashing making it easier to store
    
    return hashedFeaturesDict

# Processes the hashed features
def processHash(loadedSound, samplingRate):
    features = extractFeatures(loadedSound, samplingRate)
    featuresList = normalizeFeatures(features)
    featuresHash = hashFeatures(featuresList)
    return featuresHash