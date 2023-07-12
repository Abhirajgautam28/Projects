import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say your name...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
    except sr.RequestError as e:
        print(f"Speech recognition request error: {e}")

    return None

def mark_attendance(student_name):
    with open("attendance.txt", "a") as file:
        file.write(f"{student_name}\n")
    print(f"{student_name} is marked present.")

while True:
    input("Press Enter to start marking attendance (or 'q' to quit): ")

    name = recognize_speech()
    if name is not None:
        mark_attendance(name)

    quit_program = input("Press 'q' to quit or any other key to continue: ")
    if quit_program.lower() == "q":
        break
