# Algorithm name
Heap sort of integer values

## Author
Damián Bicocchi (2026-03-23)

## Algorithm description
Heap Sort is a comparison-based sorting algorithm based on the Binary Heap data structure.

* It is an optimized version of selection sort.
* The algorithm repeatedly finds the maximum (or minimum) element and swaps it with the last (or first) element.
* Using a binary heap allows efficient access to the max (or min) element in O(log n) time instead of O(n).
* The process is repeated for the remaining elements until the array is sorted.
* Overall, Heap Sort achieves a time complexity of O(n log n).

## Model used to create the base code
GPT-5.3

### Prompt
```
Write a Python 3.12 implementation of algorithm Heap Sort. The function "heap_sort" has as a parameter "array" which is a list of integers, and a boolean value "ascending" which takes a default value of `true`. The function must return a new list sorted in ascending order if the argument "ascending" was `true`, descending order otherwise
Requirements
* Provide docstring adjusting to PEP-8 standards
* Do not use libraries
* Provide explanatory english comments
```

## Obfuscated version
manually obfuscated