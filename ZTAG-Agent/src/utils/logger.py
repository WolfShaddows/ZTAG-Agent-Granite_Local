import logging
import os

# Asegurar que la carpeta logs existe
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/monday_audit.log',
    level=logging.INFO,
    format='%(asctime)s - [MONDAY-ZTAG-ALERT] - %(message)s'
)

def log_event(event_type, details):
    logging.info(f"TYPE: {event_type} | DETAILS: {details}")