from xunit import *


class WasRun(TestCase):
    """
    A helper class to test the behavior of the `TestCase` class.
    """

    def __init__(self, name):
        # A flag to check if the test method was run.
        self.wasRun = False

        # A log to record the order of method calls.
        self.log = ""

        # Call the parent constructor passing itself as class instance, allowing to keep track of the TestCase behavior.
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = True
        self.log = self.log + "testMethod "

    def testBrokenMethod(self):
        raise Exception

    def tearDown(self):
        self.log = self.log + "tearDown "


class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert test.log == "setUp testMethod tearDown "

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 0 failed"

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert self.result.summary() == "1 run, 1 failed"

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert self.result.summary() == "2 run, 1 failed"

    def testTearDownAfterFail(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"
        assert test.log == "setUp tearDown "

    def testFailedSetUpResult(self):
        test = WasRun("testMethod")
        test.setUp = test.testBrokenMethod
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed"


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testSuite"))
    suite.add(TestCaseTest("testTearDownAfterFail"))
    suite.add(TestCaseTest("testFailedSetUpResult"))

    result = TestResult()
    suite.run(result)

    print(result.summary())  # output: `7 run, 0 failed`
