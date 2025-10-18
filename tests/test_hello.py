import unittest
from app.hello import say_hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, CI/CD World!")

if __name__ == "__main__":
    unittest.main()
