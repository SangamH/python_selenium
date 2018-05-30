import logging

def setLogger(app_name):
    filelog = logging.FileHandler(app_name + ".log")
    filelog.setFormatter(logging.Formatter('%(asctime)s [%(process)d]: %(levelname)s %(message)s'))
    logger = logging.getLogger(app_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(filelog)
    return logger