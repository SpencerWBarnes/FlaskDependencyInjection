from WorkerClass import WorkerClass

class WrapperClass:
  def __init__(self):
    self.workerReference = WorkerClass()
    
  def runTask(self):
    return self.workerReference.executeTask()