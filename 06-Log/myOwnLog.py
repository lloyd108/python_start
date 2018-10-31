import logging
import logging.handlers
import datetime

# logger
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight',  \
                                                       interval=1, backupCount=7, \
                                                       atTime=datetime.time(0, 0, 0, 0))
RF_LOG_FORMAT = "%(asctime)s -- %(levelname)s -- %(process)d -- %(processName)s -- %(message)s"
rf_handler.setFormatter(logging.Formatter(RF_LOG_FORMAT))

F_LOG_FORMAT = "%(asctime)s==%(levelname)s==%(processName)s==%(message)s"
f_handler = logging.FileHandler('error.log')
f_handler.setFormatter(logging.Formatter(F_LOG_FORMAT))
f_handler.setLevel(logging.ERROR)

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')