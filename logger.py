<<<<<<< HEAD
import logging
import sys
from config import LOG_FILENAME

def setup_logger():
    logger = logging.getLogger('Organizer')
    logger.setLevel(logging.INFO)
    
    # Comun format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # File driver
    fh = logging.FileHandler(LOG_FILENAME, encoding = 'utf-8')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    
    # console driver
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
=======
import logging
import sys
from config import LOG_FILENAME

def setup_logger():
    logger = logging.getLogger('Organizer')
    logger.setLevel(logging.INFO)
    
    # Comun format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # File driver
    fh = logging.FileHandler(LOG_FILENAME, encoding = 'utf-8')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    
    # console driver
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
>>>>>>> 54b05133cd9a9bbcaa8f51ab228ce816d717c5e7
    return logger