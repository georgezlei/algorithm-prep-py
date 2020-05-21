#Algorithm Training for Python

This project is for programmers and students to practice the programming of algorithms. The test cases and example implementation are included and ready to use.

## Installation

```
$ pip install algorithm-training
```

## Usage

### Test your own algorithm

Let's take sorting algorithm as an example. You can create your own algorithm in a function, then add a main block to test your function.

```
from algorithm_training import test
from algorithm_training.classic.sort import test_cases

def my_sort_function(arr):
    # my implementation
    return arr
    
if __name__ == '__main__':
    test(my_sort_function, test_cases)
```

### Benchmark your algorithm against reference implementations

```
from algorithm_training import benchmark
from algorithm_training.classic.sort import algorithms, test_cases

def my_sort_function(arr):
    # my implementation
    return arr
    
if __name__ == '__main__':
    benchmark(my_sort_function, algorithms, test_cases)
```

## Implemented Algorithms

### Sort

The signature of a sort function should be like below

```
def sort(arr):
```

Argument `arr` is an list of integers `[int]`
Return value is the sorted list of integers `[int]`



