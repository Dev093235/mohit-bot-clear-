# G_VoiceReply.py - Converts text replies into voice
import pyttsx3

def voice_reply(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    user_msg = input("Enter a message: ")
    voice_reply(user_msg)
