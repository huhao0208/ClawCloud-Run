import logging
import os

# Set up debug logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Check for essential environment variables
required_env_vars = ['TELEGRAM_TOKEN', 'CHAT_ID']
for var in required_env_vars:
    if var not in os.environ:
        logging.error(f'Missing required environment variable: {var}')
        raise EnvironmentError(f'Missing required environment variable: {var}')
    else:
        logging.debug(f'Environment variable {var} is set.')

# Example function to send Telegram notifications with debug logging

def send_telegram_notification(message):
    logging.debug('Preparing to send notification...')
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
    try:
        response = requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data={'chat_id': chat_id, 'text': message})
        response.raise_for_status()
        logging.info('Notification sent successfully!')
    except Exception as e:
        logging.error(f'Failed to send notification: {e}')
