import unittest
from unittest.mock import Mock

from flask import Response

import app
from WorkerClass import WorkerClass
from WrapperClass import WrapperClass
"""
Major difficulty with imports encountered. ref https://exceptionshub.com/relative-imports-in-python-3.html
Current solution is to place the tests in the same dir as the tested material.
"""


class TestTest(unittest.TestCase):
  app = None

  def setUp(self):
    self.app = app.buildApp()
    self.client = self.app.test_client()

  def tearDown(self):
    pass

  def test_WrapperRunTask_StandardCall_200(self):
    # Input
    workerMock = Mock(WorkerClass)
    expectedData = "test"
    expectedCode = 200
    workerMock.executeTask.return_value = expectedData

    # Execute
    with self.app.container.workerObj.override(workerMock):
      result: Response = self.client.get("/api/tester")

    # Evaluate
    self.assertEqual(result.get_data(as_text=True), expectedData)
    self.assertEqual(result.status_code, expectedCode)
    workerMock.executeTask.assert_called_once()

  def test_EndpointApiTester_StandardCall_200(self):
    # Input
    wrapperMock = Mock(WrapperClass)
    expectedData = "test"
    expectedCode = 200
    wrapperMock.runTask.return_value = expectedData

    workerMock = Mock(WorkerClass)
    workerMock.executeTask.return_value = "Bad call"
    self.app.container.workerObj.override(workerMock)

    # Execute
    with self.app.container.wrapperObj.override(wrapperMock):
      result = self.client.get("/api/tester")

    # Evaluate
    self.assertEqual(result.get_data(as_text=True), expectedData)
    self.assertEqual(result.status_code, expectedCode)

    wrapperMock.runTask.assert_called_once() # wrapper was hit
    workerMock.executeTask.assert_not_called() # underlying worker was not hit

  def test_ConfigData_StandardCall_200(self):
    # Input
    expectedDataPrefix = "expected"
    expectedData = expectedDataPrefix + " 1"
    expectedCode = 200
    configOverride = {'testing': {'dummyData': expectedDataPrefix}}
    
    # Execute
    with self.app.container.config.override(configOverride):
      result = self.client.get("/api/tester")

    # Evaluate
    self.assertEqual(result.get_data(as_text=True), expectedData)
    self.assertEqual(result.status_code, expectedCode)

if (__name__ == "__main__"):
  unittest.main()