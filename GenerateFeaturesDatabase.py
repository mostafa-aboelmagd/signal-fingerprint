import ComputeHashedFeatures
import shutil
import json
from pathlib import Path
import librosa

# Save the hashed features locally
def saveHash(wavFile, featuresHash, outputDirectory):
    # Creates the output directory
    outputDirectory.mkdir(parents=True, exist_ok=True)

    # Creates the output file path
    outputFile = outputDirectory / wavFile.with_suffix(".json").name # .name extract the file name part without the path (after it was changed from .wav to .json)

    with open(outputFile, "w") as f:
        json.dump(featuresHash, f, indent=4) # The indent=4 argument makes the JSON output pretty printed 
    
# Loop over our dataset and save the computed hashed features for each song file
inputDirectory = Path("./task5_data")
outputDirectory = Path("./task5_hashes")
if outputDirectory.exists():
        shutil.rmtree(outputDirectory)

for file in inputDirectory.glob("*.wav"):
    loadedSound, samplingRate = librosa.load(file, sr=None) # loadedSound is an array containing the amplitudes, sr is set to none so that it uses the original sampling rate
    hashedFeatures = ComputeHashedFeatures.processHash(loadedSound, samplingRate)
    saveHash(file, hashedFeatures, outputDirectory)