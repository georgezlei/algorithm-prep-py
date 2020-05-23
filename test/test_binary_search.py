# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei
from unittest import TestCase
import algorithm_prep as algo
import algorithm_prep.classic.binary_search as bis

class BiSearchTest(TestCase):
  def test_list_index(self):
    self.assertTrue(algo.test(bis.list_index, bis.test_cases))

  def test_python_bisect(self):
    self.assertTrue(algo.test(bis.python_bisect, bis.test_cases))

  def test_binary_search(self):
    self.assertTrue(algo.test(bis.bisearch, bis.test_cases))

