

class WorkerClass:

  def __init__(self):
    self.value = 0
    print(str(self.value) + ":" + str(self))

  def executeTask(self):
    self.value += 1
    return "Success "+str(self.value)+str(self)
