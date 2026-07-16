import logging

class create_log_object():
    def __init__(self,LOG_PATH):
 
        logging.basicConfig(
            filename=LOG_PATH,
            level=logging.INFO,
            format=(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(message)s"
            )
        )
        self.logger = logging.getLogger(__name__)
    

    def mensage(self,mensage):

        self.logger.info(
        mensage
    )
 