import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# Initially set log_switch to True (logging enabled)
log_switch = False

# Function to disable logging
def disable_logging():
    global log_switch
    log_switch = False
    logger.disabled = True  # Disable the logger instance

# Function to enable logging
def enable_logging():
    global log_switch
    log_switch = True
    logger.disabled = False  # Enable the logger instance

# Example usage
logger.info("Application started.")

# Conditional logging based on log_switch flag
if log_switch:
    logger.debug("Debug message that will be logged.")
else:
    logger.debug("Logging is disabled. This message won't be logged.")

# Disable logging
disable_logging()

# Now logging is disabled, so this debug message won't be logged
logger.debug("Debug message that won't be logged when logging is disabled.")

# Enable logging again
enable_logging()

# Now logging is enabled, so this debug message will be logged again
logger.debug("Debug message that will be logged after enabling logging.")
