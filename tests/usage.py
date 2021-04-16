import logging
from kublog import get_logger

logger = get_logger(level=logging.DEBUG)
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
