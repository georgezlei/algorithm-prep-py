# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei

import time
import copy

def test(func, test_cases):
  '''Test your algorithm function against the test cases. It is recommend to use
  the test cases given in the package. However you can use your own test cases
  as long as they are in the same format.

  Example: test(your_sort_func, algorithm_training.classic.sort.test_cases)
  '''

  passed = True
  # print header
  print('{:30}{:7}{:9}'.format('Test Case Name', 'Status', 'Time'))
  print('-' * 42)

  for case in test_cases:
    input = copy.deepcopy(case['in'])
    time0 = time.time()
    out = func(*input)
    time1 = time.time()
    timeUsed = (time1 - time0) * 1000

    # case['out'] is the expected output. It can be a simple Python data
    # structure or a function taking real output as argument and return True
    # or False and failure reason.
    expected = case['out']
    if callable(expected):
      passed, fail_reason = expected(out)
    else:
      passed = expected == out
      if passed:
        fail_reason = None
      else:
        # build fail_reason string
        actual = out
        if isinstance(expected, (str, list, tuple, dict, set)) and \
            len(str(expected)) > 10:
          expected = '\n' + str(expected) + '\n'
        if isinstance(actual, (str, list, tuple, dict, set)) and \
            len(str(actual)) > 10:
          actual = '\n' + str(actual)
        fail_reason = 'Expects {} but get {}'.format(expected, actual)

    if passed:
      print('{:30}passed{:9.2f} ms'.format(case['name'], timeUsed))
    else:
      print('{:30}Failed. {}'.format(case['name'], fail_reason))
      passed = False

  return passed


def benchmark(your_algorithm, benchmark_algorithms, test_cases):
  '''Run benchmark on your algorithm function together with some other
  algorithms. It is recommend that you use the pre-coded algorithms and test
  cases given in this package.

  Example: benchmark(your_sort_func, algorithm_training.classic.sort.all_algorithms, algorithm_training.classic.sort.test_cases)
  '''
  # print header
  print('{:32}{:9}'.format('Algorithm', 'Time'))
  print('-' * 40)
  
  algorithms = [('Your algorithm', your_algorithm)] + benchmark_algorithms
  for name, func in algorithms:
    cases = copy.deepcopy(test_cases)
    time0 = time.time()
    for case in cases:
      func(*case['in'])
    time1 = time.time()
    timeUsed = (time1 - time0) * 1000

    print('{:27}{:9.2f} ms'.format(name, timeUsed))