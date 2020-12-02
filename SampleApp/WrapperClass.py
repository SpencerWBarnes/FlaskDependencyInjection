# from WorkerClass import WorkerClass
# from DependencyContainer import DependencyContainer
# from dependency_injector.wiring import inject, Provide
# import dependency_injector

class WrapperClass:
  # @inject
  def __init__(self, workerReference):
              # workerReference = DependencyContainer.workerObj()):
              # workerReference = Provide[DependencyContainer.workerObj]):
    # print(f"\tType: {type(workerReference.provider)}\tObj: {workerReference.provider}")
    # print(f"\tType: {type(workerReference().provider)}\tObj(): {workerReference().provider}")

    self.workerReference = workerReference

  # def __init__(self):
  #   self.workerReference = WorkerClass()
    
  def runTask(self):
    return self.workerReference.executeTask()