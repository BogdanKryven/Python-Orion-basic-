import logging
from logging import handlers

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.CRITICAL)
s_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
s_handler.setFormatter(s_format)
logger.addHandler(s_handler)

f_handler = logging.FileHandler(filename='log.log')
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(s_format)

logger.addHandler(f_handler)


logger.debug("debug msg")
logger.info("info msg")
logger.warning("warning msg")
logger.error("error msg")
logger.critical("critical msg")

