# H_Main.py
import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import manual login function from our login module (assumed to be in B_FB_Login.py)
from B_FB_Login import get_session_manual

def open_messenger(driver):
    """
    Opens Facebook Messenger page.
    """
    print("🚀 Navigating to Messenger...")
    driver.get("https://www.facebook.com/messages")
    time.sleep(10)  # Wait for Messenger page to load

def mark_message_seen(driver):
    """
    Dummy function to mark a conversation as 'seen'.
    This function tries to click on an unread conversation.
    Note: XPath locator may need updates as Facebook UI changes.
    """
    try:
        # Example XPath: Conversation container with "unread" label (adjust as needed)
        unread_conversations = driver.find_elements(By.XPATH, "//div[contains(@aria-label, 'Unread') or contains(@class, 'unread')]")
        if unread_conversations:
            print("🔔 Unread conversation found. Clicking to mark as seen...")
            unread_conversations[0].click()
            time.sleep(5)  # Wait for conversation to load and mark as seen
            print("✅ Message marked as seen.")
        else:
            print("ℹ️ No unread messages found.")
    except Exception as e:
        print("⚠️ Error while marking message as seen:", e)

def send_reply(driver, reply_text):
    """
    Sends a reply in the currently open conversation.
    Note: The XPath used here is a sample. Facebook's DOM can change frequently.
    """
    try:
        # Example: Find the message input field. XPath may need adjustment.
        message_input = driver.find_element(By.XPATH, "//div[@aria-label='Message' and @role='textbox']")
        message_input.click()
        message_input.send_keys(reply_text)
        message_input.send_keys(Keys.RETURN)
        print(f"✅ Sent reply: {reply_text}")
    except Exception as e:
        print("⚠️ Error while sending reply:", e)

def main():
    print("🔥 Mohit Bot Starting...")

    # Step 1: Manual login via Firefox
    driver = get_session_manual()
    if not driver:
        print("❌ Login failed. Exiting...")
        sys.exit(1)
    else:
        print("✅ Login successful!")

    # Step 2: Navigate to Messenger
    open_messenger(driver)

    # Step 3: Mark an unread message as seen (dummy implementation)
    mark_message_seen(driver)

    # Step 4: Send an automated reply
    send_reply(driver, "Hello, this is an automated reply!")

    # Wait a bit before closing
    time.sleep(10)
    driver.quit()
    print("👋 Bot session ended.")

if __name__ == "__main__":
    main()
