

class WorkerClass:
  # No need to inject since this object is handled in the dependency container
  def __init__(self, logger, testData):
    self.testData = testData
    self.value = 0
    self.logger = logger
    self.logger.debug(f'Instantiating [{self}]')

  def executeTask(self):
    self.value += 1
    self.logger.debug(f'[{self}] with value {self.value}')
    return f"{self.testData} {self.value}"
