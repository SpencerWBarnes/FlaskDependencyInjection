# import logging

class WorkerClass:

  def __init__(self, logger, testData):
    self.testData = testData
    self.value = 0
    self.logger = logger
    self.logger.error(str(self.value) + ":" + str(self))

  def executeTask(self):
    self.value += 1
    self.logger.error("logging")
    return f"{self.testData} {self.value}"
