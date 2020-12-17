from dependency_injector import containers, providers
from WorkerClass import WorkerClass
from WrapperClass import WrapperClass

import logging
from logging.handlers import RotatingFileHandler

class DependencyContainer(containers.DeclarativeContainer):

  config = providers.Configuration()

  # logging.config.dictConfig(config.logging)
  # logger = logging.getLogger()
  # logging.basicConfig(format=config.logging.format.as_str(), datefmt=config.logging.datefmt.as_str())
  
  # WARNING: Running the server in debug mode breaks the log files since the debugger 
  #   does not release the files, making the file rotation's renaming throw an exception
  logger = logging.getLogger("Test Logger")
  handler = RotatingFileHandler(filename="testLogger.log", maxBytes=(1024), backupCount=2)
  formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
  handler.setFormatter(formatter)

  logger.addHandler(handler)
  logger.warning("logging?")
  # logger.basicConfig(filename="testLogger.log", level=logging.NOTSET, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
  
  # logger = logging.getLogger(__name__)
  # logger.error("Logging?")
  # # logger = providers.Object(loggingObject)

  workerObj = providers.ThreadSafeSingleton(
    WorkerClass,
    logger,
    testData = config.testing.dummyData
  )
  
  wrapperObj = providers.ThreadSafeSingleton(
    WrapperClass,
    workerReference = workerObj
  )