import inspect
import logging





def log_generator():
    log_name = inspect.stack()[1][3]  # runtime -getting filepath -class -method
    logger = logging.getLogger(log_name)
    logfile = logging.FileHandler("C:\\Fremework projects\\nopcommerce\\nopcommerce_framework\\Logs\\nop_log.log")
    log_format = logging.Formatter(
        "%(asctime)s: %(lineno)d: %(levelname)s : %(name)s : %(funcName)s : %(message)s ")
    logfile.setFormatter(log_format)
    logger.addHandler(logfile)
    logger.setLevel(logging.INFO)
    return logger


