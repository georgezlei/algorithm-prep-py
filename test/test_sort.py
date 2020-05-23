from unittest import TestCase
# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei
import algorithm_prep as algo
import algorithm_prep.classic.sort as sort

class TestSort(TestCase):
  def test_bubble_sort(self):
    self.assertTrue(algo.test(sort.bubble_sort, sort.test_cases))

  def test_insert_sort(self):
    self.assertTrue(algo.test(sort.insert_sort, sort.test_cases))

  def test_heap_sort(self):
    self.assertTrue(algo.test(sort.heap_sort, sort.test_cases))

  def test_merge_sort(self):
    self.assertTrue(algo.test(sort.merge_sort, sort.test_cases))

  def test_quick_sort(self):
    self.assertTrue(algo.test(sort.quick_sort, sort.test_cases))

  def test_radix_sort(self):
    self.assertTrue(algo.test(sort.radix_sort, sort.test_cases))