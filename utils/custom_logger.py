import logging
import colorlog
class Logger:

    @staticmethod
    def log_gen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        # formatter = logging.Formatter(
        #     "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        #     datefmt="%Y-%m-%d %H:%M:%S"
        # )
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            log_colors={
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
            }
        )
        console_handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(console_handler)
        logger.propagate=False
        return logger
