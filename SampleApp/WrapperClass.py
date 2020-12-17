# from WorkerClass import WorkerClass
# from DependencyContainer import DependencyContainer
# from dependency_injector.wiring import inject, Provide
# import dependency_injector

class WrapperClass:
  # @inject
  def __init__(self, logger, workerReference):
    self.logger = logger
    self.workerReference = workerReference
    
  def runTask(self):
    self.logger.debug("Executing the worker task")
    return self.workerReference.executeTask()