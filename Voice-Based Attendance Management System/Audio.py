import os
import pyaudio
import wave

data_folder = "voice_samples/"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

def record_voice_sample(file_name):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 3

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording voice sample for", file_name)
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wave_file_path = os.path.join(data_folder, file_name + ".wav")
    wf = wave.open(wave_file_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Example usage:
student_id = input("Enter student ID: ")
for i in range(6):
    record_voice_sample(student_id + "_" + str(i) + ".wav")
print("Voice samples recorded and saved for student:", student_id)
