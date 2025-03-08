# F_NameDetect.py - Detects names and gives personalized responses
def detect_name(message):
    names = ["Mohit", "Rahul", "Priya"]
    for name in names:
        if name.lower() in message.lower():
            return f"Hey {name}! How are you? 😊"
    return "I don't recognize that name. 🤔"

if __name__ == "__main__":
    user_input = input("Enter a message: ")
    print(detect_name(user_input))
