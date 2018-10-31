import logging

# print(logging.DEBUG)
LOG_FORMAT = "%(asctime)s -- %(levelname)s -- %(process)d -- %(processName)s -- %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="myLogging.log", format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.error("This is a error log.")