from dependency_injector import containers, providers
from WorkerClass import WorkerClass
from WrapperClass import WrapperClass
import config as configFile
import os

import logging
from logging.handlers import RotatingFileHandler

def buildLogger(format, datefmt, dirName, fileName, maxBytes, backupCount, severityLevel, name=""):
  logger = None
  if (name == ""):
    logger = logging.getLogger()
  else:
    logger = logging.getLogger(name)

  handler = RotatingFileHandler(filename=os.path.join(dirName, fileName), 
                                maxBytes=maxBytes,
                                backupCount=backupCount)
  formatter = logging.Formatter(format, datefmt=datefmt)
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.setLevel(severityLevel)
  return logger


class DependencyContainer(containers.DeclarativeContainer):

  config = providers.Configuration()
  
  # WARNING: Running the server in debug mode breaks the log files since the debugger 
  #   does not release the files, making the file rotation's renaming throw an exception
  
  # Since the values are being used immediately, easier to access the dict than the injected config
  _loggingConfig = configFile.config["logging"]

  # Get this file's parent DIR for consistent relative pathing
  dirName  = os.path.dirname(__file__)
  dirName = os.path.join(dirName, _loggingConfig["dir"])
  
  # Create desired dir (recurively is multiple do not exist)
  if not(os.path.exists(dirName)):
    os.makedirs(dirName)

  defaultLogger = buildLogger(
    name=_loggingConfig["streams"]["default"]["name"], 
    format=_loggingConfig["format"],
    datefmt=_loggingConfig["datefmt"],
    dirName=dirName,
    fileName=_loggingConfig["streams"]["default"]["file"],
    maxBytes=_loggingConfig["logSize"],
    backupCount=_loggingConfig["backupCopies"],
    severityLevel=_loggingConfig["level"]
  )

  testLogger = buildLogger(
    name=_loggingConfig["streams"]["testLog"]["name"], 
    format=_loggingConfig["streams"]["testLog"]["format"],
    datefmt=_loggingConfig["datefmt"],
    dirName=dirName,
    fileName=_loggingConfig["streams"]["testLog"]["file"],
    maxBytes=_loggingConfig["logSize"],
    backupCount=_loggingConfig["backupCopies"],
    severityLevel=_loggingConfig["level"]
  )

  workerObj = providers.ThreadSafeSingleton(
    WorkerClass,
    logger=testLogger,
    testData = config.testing.dummyData
  )
  
  wrapperObj = providers.ThreadSafeSingleton(
    WrapperClass,
    logger=testLogger,
    workerReference = workerObj
  )