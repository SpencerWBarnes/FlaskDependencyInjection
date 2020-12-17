import logging

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
    'filename': "testLogger.log",
    'format': "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    'datefmt': "%m/%d/%Y %I:%M:%S"
    # 'formatters': {
    #   'f': {
    #     'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    #   }
    # },
    # 'handlers': {
    #   'h': {
    #     'class': 'logging.StreamHandler',
    #     'formatter': 'f',
    #     'level': logging.DEBUG
    #   }
    # },
    # 'root': {
    #   'handlers': ['h'],
    #   'level': logging.DEBUG
    # }
  }
}