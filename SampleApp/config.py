

config = {
  'app': {
    'host': "0.0.0.0",
    'port': 8080,
    'env': "prod"
  },
  'testing': {
    'dummyData': "Test Data"
  },
  'logging': {
    'dir': "../Logs",
    'format': "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    'datefmt': "%m/%d/%Y %I:%M:%S",
    'level': 0,
    'logSize': (1024*1024), #1MB
    'backupCopies': 1,
    'streams': {
      'testLog': {
        'file': "testLogger.log",
        'format': "%(asctime)s %(levelname)-8s %(message)s",
        'name': "Test-logger"
      },
      'default': {
        'file': "allLogs.log",
        'name': ""
      }
    }
  }
}