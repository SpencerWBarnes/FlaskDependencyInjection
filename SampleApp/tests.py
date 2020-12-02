import unittest
from unittest.mock import Mock

import app
from WorkerClass import WorkerClass
from WrapperClass import WrapperClass

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
    expectedData = b"test"
    expectedCode = 200
    workerMock.executeTask.return_value = expectedData

    # Execute
    with self.app.container.workerObj.override(workerMock):
      result = self.client.get("/api/tester")

    # Evaluate
    self.assertEqual(result.get_data(), expectedData)
    self.assertEqual(result.status_code, expectedCode)
    workerMock.executeTask.assert_called_once()

  def test_EndpointApiTester_StandardCall_200(self):
    # Input
    wrapperMock = Mock(WrapperClass)
    expectedData = b"test"
    expectedCode = 200
    wrapperMock.runTask.return_value = expectedData

    workerMock = Mock(WorkerClass)
    workerMock.executeTask.return_value = b"Bad call"
    self.app.container.workerObj.override(workerMock)

    # Execute
    with self.app.container.wrapperObj.override(wrapperMock):
      result = self.client.get("/api/tester")

    # Evaluate
    self.assertEqual(result.get_data(), expectedData)
    self.assertEqual(result.status_code, expectedCode)

    wrapperMock.runTask.assert_called_once() # wrapper was hit
    workerMock.executeTask.assert_not_called() # underlying worker was not hit

if (__name__ == "__main__"):
  unittest.main()