import time
import copy

def test(func, test_cases):
  '''Test your algorithm function against the test cases. It is recommend to use
  the test cases given in the package. However you can use your own test cases
  as long as they are in the same format.

  Example: test(your_sort_func, algorithm_training.classic.sort.test_cases)
  '''

  passed = True
  print('Test Case Name\t\t\tStatus\tTime')
  print('-------------------------------------------------')
  for case in test_cases:
    input = copy.deepcopy(case['in'])
    time0 = time.time()
    out = func(*input)
    time1 = time.time()
    timeUsed = (time1 - time0) * 1000

    if out == case['out']:
      print('{:30}passed{:9.2f} ms'.format(case['name'], timeUsed))
    else:
      print('{:30}:failed. Expects\n{}\nbut get\n{}'.format(case['name'], case['out'], out))
      passed = False

  return passed


def benchmark(your_algorithm, benchmark_algorithms, test_cases):
  '''Run benchmark on your algorithm function together with some other
  algorithms. It is recommend that you use the pre-coded algorithms and test
  cases given in this package.

  Example: benchmark(your_sort_func, algorithm_training.classic.sort.all_algorithms, algorithm_training.classic.sort.test_cases)
  '''

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