import os
import librosa
import numpy as np

def extract_features(file_path):
    try:
        audio, sr = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        return mfccs

    except Exception as e:
        print(f"Error encountered while parsing audio file: {file_path}")
        return None

def train_model():
    # Directory containing the voice samples
    voice_samples_dir = 'voice_samples'

    features = []
    labels = []

    # Iterate through the voice samples directory
    for root, dirs, files in os.walk(voice_samples_dir):
        for file in files:
            # Get the file path
            file_path = os.path.join(root, file)

            # Extract features from the audio file
            mfccs = extract_features(file_path)

            # Append the features and corresponding label
            if mfccs is not None:
                features.append(mfccs)
                labels.append(file.split('_')[0])  # Extract the student ID from the file name

    # Convert the features and labels to numpy arrays
    features = np.array(features)
    labels = np.array(labels)

    # Perform further steps for training your voice recognition model

# Usage
train_model()