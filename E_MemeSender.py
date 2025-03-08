# E_MemeSender.py - Sends memes in response to messages
import random
import os

meme_folder = "data/memes"

def send_meme():
    memes = os.listdir(meme_folder)
    if not memes:
        return "⚠️ No memes found!"
    return os.path.join(meme_folder, random.choice(memes))

if __name__ == "__main__":
    print("Sending meme:", send_meme())
