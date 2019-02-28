from mockito import mock, verify
import unittest


class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        helloworld(out)

        verify(out).write("Hello world of Python\n")