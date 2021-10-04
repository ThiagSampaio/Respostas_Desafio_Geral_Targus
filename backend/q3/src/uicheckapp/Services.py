
import logging

logger = logging.getLogger(__name__)  # the __name__ resolve to "uicheckapp.services"
                                      # This will load the uicheckapp logger

class EchoService:
    def __init__(self,msg):
        self.msg = msg

    def echo(self):
        logger.info("echoing something from the uicheckapp logger")
        print(self.msg)