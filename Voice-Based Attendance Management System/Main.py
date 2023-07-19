import speech_recognition as sr
import pandas as pd


def mark_attendance(student_id):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say present sir.")
        audio = recognizer.listen(source)

    try:
        present_phrase = recognizer.recognize_google(audio)
        if present_phrase == "present sir":
            sheet = pd.DataFrame({"Student ID": [student_id], "Attendance": ["Present"]})
            sheet.to_excel("attendance.xlsx")
            print("Your attendance has been marked.")
        else:
            print("Sorry, I didn't understand.")
    except:
        print("Sorry, I couldn't recognize your voice.")


if __name__ == "__main__":
    student_id = input("Enter your student ID: ")
    mark_attendance(student_id)
