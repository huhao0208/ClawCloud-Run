import logging
import requests

# Set up debug logging
logging.basicConfig(level=logging.DEBUG)

TELEGRAM_API_URL = 'https://api.telegram.org/bot<token>/sendMessage'

def send_telegram_message(chat_id, message):
    try:
        payload = {'chat_id': chat_id, 'text': message}
        logging.debug(f"Sending message to {chat_id}: {message}")
        response = requests.post(TELEGRAM_API_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        logging.debug(f"Message sent successfully: {response.json()}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send message to Telegram: {e}")
        logging.debug(f"Response: {response.content}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage: send_telegram_message('<chat_id>', 'This is a test message.')