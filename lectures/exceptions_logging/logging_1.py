import logging

template = "%(levelname)s: %(filename)s: %(asctime)s - %(message)s"

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="a", format=template)

logging.debug("debug msg")
logging.info("info msg")
logging.warning("warning msg")
logging.error("error msg")
logging.critical("critical msg")
