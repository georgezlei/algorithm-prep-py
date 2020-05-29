Algorithm Prep provides an easy way to practise algorithms for programmers and students. It includes the ready-to-use test cases for user to test the algorithm, and the reference implementations to benchmark the performance of the user's algorithms.

## Installation

```
$ pip install algorithm-prep
```

## Usage

### Test your own algorithm

Let's take sorting algorithm as an example. You can create your own algorithm in a function, then add a main block to test your function.

```
from algorithm_prep import test
from algorithm_prep.classic.sort import test_cases

def my_sort_function(arr):
    # my implementation
    return arr
    
test(my_sort_function, test_cases)
```

### Benchmark your algorithm against reference implementations

```
from algorithm_prep import benchmark
from algorithm_prep.classic.sort import algorithms, test_cases

def my_sort_function(arr):
    # my implementation
    return arr
    
benchmark(my_sort_function, algorithms, test_cases)
```

## Supported Algorithms

There are a few algorithms implemented in algorithm-prep. 

### Sorting

First include following import statements in your code

```
from algorithm_prep import test, benchmark
from algorithm_prep.classic.sort import test_cases, algorithms
```

Then write your sorting function

```
def your_sort_algorithm(arr):
	"""
    :type arr: List[int]
    :rtype: List[int]
    """
```

To test the function

```
test(your_sort_algorithm, test_cases)
```

Or to benchmark your algorithm

```
benchmark(your_sort_algorithm, algorithms, test_cases)
```

Following reference algorithms are implemented for benchmark

* Bubble Sort
* Insertion Sort
* Merge Sort
* Quick Sort
* Heap Sort
* Radix Sort

### String Search

First make following import statement

```
from algorithm_prep import test, benchmark
from algorithm_prep.classic.string_search import algorithms, test_cases
```

Then write your own string search algorithm

```
def your_string_search(string, target):
	"""Search target in string, and return the index of first occurance, or return -1 if not found.
	:type string: str
	:type target: str
	:rtype: int
	"""
```

Now you can test your algorithm

```
test(your_string_search, test_cases)
```

Or benchmark its performance

```
benchmark(your_string_search, algorithms, test_cases)
```

The reference implementations of string search algorithms include

* Brute force search algorithm
* str.find() in Python
* KMP algorithm
* Rabin-Karp algorithm

### Binary Search

First import following codes

```
from algorithm_prep import test, benchmark
from algorithm_prep.classic.binary_search import algorithms, test_cases
```

Then add your search algorithm

```
def your_search_algorithm(arr, target):
	"""Search target in arr and return the index, or return -1 if target not found.
	:type arr: list[int]
	:type target: int
	:rtype: int
	"""
```

At last your can test your algorithm

```
test(your_search_algorithm, test_cases)
```

Or run benchmark

```
benchmark(your_search_algorithm, algorithms, test_cases)
```

### Union Find

First make import statement

```
from algorithm_prep import test, benchmark
from algorithm_prep.classic.union_find import algorithms, test_cases
```

Then add your algorithm

```
def your_union_find(vertices, edges):
	"""Find the number of the components in a graph. The graph is represented in the number of vertices (the vertices will be [0,1,...,n-1]) and list of edges [(i, j), (k, l),..]
	:type vertices: int
	:type edges: list[tuple(int)]
	:rtype: int
	"""
```

At last you can test your algorithm

```
test(your_union_find, test_cases)
```

Or you run benchmark

```
benchmark(your_union_find, algorithms, test_cases)
```

### Topological Sort

First make import statement

```
from algorithm_prep import test, benchmark
from algorithm_prep.classic.topological_sort import algorithms, test_cases
```

Then add your algorithm

```
def your_topological_sort(vertices, edges):
	"""Find the topological order of vertices in a graph. The graph is represented in the number of vertices (the vertices will be [0,1,...,n-1]) and list of edges [(i, j), (k, l),..]
	:type vertices: int
	:type edges: list[tuple(int)]
	:rtype: list[int]
	"""
```

At last you can test your algorithm

```
test(your_topological_sort, test_cases)
```

Or you run benchmark

```
benchmark(your_topological_sort, algorithms, test_cases)
```

### 