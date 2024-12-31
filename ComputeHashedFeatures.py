import librosa
import numpy as np
import imagehash
from PIL import Image

# Extract features from the WAV file
def extractFeatures(loadedSound, samplingRate):
    melSpectrogram = librosa.feature.melspectrogram(y=loadedSound, sr=samplingRate, n_mels=128, fmax=8000) # Computes mel spectrogram, which is designed to mimic human hearing
    # Most audio content does not typically need frequencies higher than 8 kHz, therefore we chose it to limit unneccesary computations
    
    features = {
        "mfcc": librosa.feature.mfcc(y=loadedSound, sr=samplingRate), # Mel-Frequency Cepstral Coefficients represents power spectrum (timbre or quality) of the sound
        "chroma": librosa.feature.chroma_stft(y=loadedSound, sr=samplingRate), # Represents harmonic content (energy distribution across 12 different pitch classes)
        "spectralContrast": librosa.feature.spectral_contrast(y=loadedSound, sr=samplingRate), # Represents difference in amplitude between peaks and valleys
        "spectralRollof": librosa.feature.spectral_rolloff(y=loadedSound, sr=samplingRate), # Measures the frequency below which a certain percentage (85%) of the total spectral energy lies
        "zcr": librosa.feature.zero_crossing_rate(y=loadedSound), # Measure of how often the signal changes sign
        "melSpectrogram": librosa.power_to_db(melSpectrogram, ref=np.max), # Converts the mel spectrogram to log scale, compressing loud values and making the quieter parts more visible
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