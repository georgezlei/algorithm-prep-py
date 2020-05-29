# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei

from unittest import TestCase
import algorithm_prep as algo
import algorithm_prep.classic.topological_sort as ts

class TopologicalSortTest(TestCase):
  def test_topological_sort(self):
    self.assertTrue(algo.test(ts.topological_sort, ts.test_cases))

