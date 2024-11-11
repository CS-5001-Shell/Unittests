from stack import Stack
import unittest

class StackTest(unittest.TestCase):

	def test_constructor(self):
		stack = Stack(10)
		self.assertEqual(stack.max_size, 10)
		self.assertEqual(len(stack.items), 0)

	"""
	Implement at least two tests for each of the following
	methods: push, pop, size. You will submit at least six
	test cases in total.

	Hint: take a look at the documentation for unittest
	https://docs.python.org/3/library/unittest.html
	and consider how you might use the assertRaises method
	"""

def main():
	unittest.main()

if __name__ == '__main__':
	main()