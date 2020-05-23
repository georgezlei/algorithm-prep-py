# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei
from unittest import TestCase
import algorithm_prep as algo
import algorithm_prep.classic.union_find as uf

class UnionFindTest(TestCase):
  def test_union_find(self):
    self.assertTrue(algo.test(uf.union_find, uf.test_cases))