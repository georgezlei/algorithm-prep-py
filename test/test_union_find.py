# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei
from unittest import TestCase
import algorithm_training as algo
import algorithm_training.classic.union_find as uf

class UnionFindTest(TestCase):
  def test_union_find(self):
    self.assertTrue(algo.test(uf.union_find, uf.test_cases))