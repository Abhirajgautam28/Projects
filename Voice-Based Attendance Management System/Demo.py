import speech_recognition as sr
import os
import keras
import librosa

def store_voice(student_id, voice_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(voice_file) as source:
        audio = recognizer.listen(source)

    try:
        present_phrase = recognizer.recognize_google(audio)
        if present_phrase == "present sir":
            print("Your voice has been stored.")
        else:
            print("Sorry, I didn't understand.")
    except:
        print("Sorry, I couldn't recognize your voice.")

    features = librosa.feature.mfcc(audio, sr=16000, n_mfcc=13)
    pickle.dump(features, open(f"{student_id}.pkl", "wb"))

def mark_attendance(student_id, voice_file):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say present sir.")
        audio = recognizer.listen(source)

    try:
        present_phrase = recognizer.recognize_google(audio)
        if present_phrase == "present sir":
            print("Your attendance has been marked.")
        else:
            print("Sorry, I didn't understand.")
    except:
        print("Sorry, I couldn't recognize your voice.")

    features = librosa.feature.mfcc(audio, sr=16000, n_mfcc=13)
    model = keras.models.load_model("model.h5")
    prediction = model.predict(features.tolist())

    if prediction[0] >= 0.5:
        print("Your attendance has been marked.")
    else:
        print("Sorry, I couldn't recognize your voice.")

def extract_features(audio):
    features = librosa.feature.mfcc(audio, sr=16000, n_mfcc=13)
    return features

if __name__ == "__main__":
    student_id = input("Enter your student ID: ")
    voice_file = f"{student_id}.wav"
    store_voice(student_id, voice_file)
    mark_attendance(student_id, voice_file)
