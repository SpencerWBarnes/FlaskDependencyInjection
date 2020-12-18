

class WrapperClass:
  # No need to inject since this object is handled in the dependency container
  def __init__(self, logger, workerReference):
    self.logger = logger
    self.workerReference = workerReference
    
  def runTask(self, portNumber):
    self.logger.debug(f"Executing the worker task on port {portNumber}")
    return self.workerReference.executeTask()