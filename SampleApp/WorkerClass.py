

class WorkerClass:

  def __init__(self, testData):
    self.testData = testData
    self.value = 0
    print(str(self.value) + ":" + str(self))

  def executeTask(self):
    self.value += 1
    return f"{self.testData} {self.value}"
