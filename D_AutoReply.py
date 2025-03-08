# D_AutoReply.py - Handles automatic replies for incoming messages
import time

def auto_reply(message):
    replies = {
        "hi": "Hello! How can I help you? 😊",
        "hello": "Hey there! Need any assistance? 👋",
        "bye": "Goodbye! Have a great day! 👋",
    }
    return replies.get(message.lower(), "I'm not sure how to respond to that. 🤔")

# Simulating incoming messages
if __name__ == "__main__":
    while True:
        user_msg = input("User: ")
        print("Bot:", auto_reply(user_msg))
