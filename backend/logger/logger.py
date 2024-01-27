import logging

def configure_logging():
    logging.basicConfig(level=logging.ERROR,format='%(asctime)s - %(levelname)s - %(message)s')