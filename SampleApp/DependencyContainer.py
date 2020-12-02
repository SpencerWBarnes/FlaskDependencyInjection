from dependency_injector import containers, providers
from WorkerClass import WorkerClass
from WrapperClass import WrapperClass

class DependencyContainer(containers.DeclarativeContainer):

  config = providers.Configuration()

  workerObj = providers.ThreadSafeSingleton(
    WorkerClass,
    testData = config.testing.dummyData,
  )
  
  wrapperObj = providers.ThreadSafeSingleton(
    WrapperClass,
    workerReference = workerObj
  )