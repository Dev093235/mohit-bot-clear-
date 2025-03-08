# H_Main.py - The main script that runs the bot and integrates all functions
import D_AutoReply
import E_MemeSender
import F_NameDetect
import G_VoiceReply

def main():
    print("🤖 Mohit Bot is now running... Type 'exit' to stop.")

    while True:
        user_msg = input("User: ")
        if user_msg.lower() == "exit":
            print("👋 Goodbye!")
            break

        reply = D_AutoReply.auto_reply(user_msg)
        name_response = F_NameDetect.detect_name(user_msg)

        if name_response != "I don't recognize that name. 🤔":
            reply = name_response

        print("Bot:", reply)
        G_VoiceReply.voice_reply(reply)

if __name__ == "__main__":
    main()
