import logging
import os


class LogGen():
    @staticmethod
    def loggen():
        # 1. Get the directory where customLogger.py is located (.../utilities)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 2. Step back one folder to the root, then navigate to the logs folder
        path = os.path.join(current_dir, '..', 'logs', 'automation.log')

        # 3. Apply the config with force=True to bypass pytest's default logger
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)  # <-- This is the magic keyword for Pytest

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
