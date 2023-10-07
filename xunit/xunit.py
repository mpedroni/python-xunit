class TestResult:
    """
    Collects the results of running a test.
    """

    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)


class TestCase:
    """
    The base class for all tests. It provides a template method `run` that
    runs the test and collects the results. It also provides methods
    `setUp` and `tearDown` that may be overridden to do fixture setup and teardown operations.
    """

    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted()

        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        self.tearDown()

        return result


class TestSuite(TestCase):
    """
    A collection of tests that can be run together.
    Using the Composite pattern to be able to treat a single test the same way as a collection of tests.
    """

    def __init__(self) -> None:
        self.tests: list[TestCase] = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


def run(testCase: TestCase):
    """
    A helper function to run a test case and print the results.
    """
    result = TestResult()
    testCase.run(result)

    print(result.summary())
