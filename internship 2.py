import speech_recognition as sr
import tkinter as tk
import pyttsx3

# Initialize components
recognizer = sr.Recognizer()
engine = pyttsx3.init()
root = tk.Tk()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle button click
def on_button_click():
    user_input = recognize_speech()
    respond_to_command(user_input)

# Function to respond to voice commands
def respond_to_command(command):
    if "hello" in command.lower():
        speak("Hello! How can I help you?")
    elif "how are you" in command.lower():
        speak("I'm doing well, thank you!")
    elif "goodbye" in command.lower():
        speak("Goodbye! Have a great day.")
        root.destroy()  # Close the GUI
    else:
        speak("Sorry, I didn't understand that command.")

# Create GUI
root.title("Voice Assistant")
root.geometry("300x200")

button = tk.Button(root, text="Click to Speak", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()
