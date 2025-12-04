# Example: Generator function to yield squares of numbers

def square_generator(n):
    """
    Generator that yields the square of numbers from 0 to n-1.
    """
    for i in range(n):
        yield i * i

# Example of using the generator
gen = square_generator(5)
print("Squares using generator:")
for sq in gen:
    print(sq)

# Example: Simple iterator class that iterates over a list in reverse

class ReverseListIterator:
    """
    An iterator that returns the elements of a list in reverse order.
    """
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.lst[self.index]
        self.index -= 1
        return value

# Example of using the iterator
my_list = [10, 20, 30, 40]
rev_iter = ReverseListIterator(my_list)
print("Reversed list using iterator:")
for item in rev_iter:
    print(item)

    # Generators and iterators are two related concepts in Python for dealing with sequences of data:
    # 
    # - A *generator* is a special kind of function that returns an iterator object, which we can iterate over one value at a time. 
    #   Instead of returning all the values at once (like a list), a generator yields values one at a time, only when requested with `next()`.
    #   This makes generators especially useful for working with large data sets or streams where storing all values in memory isn't practical.
    #   Generator functions look like regular functions, but use the `yield` keyword to return values one at a time.
    # 
    # - An *iterator* is any object that implements the `__iter__()` and `__next__()` methods. When you use a `for` loop over something,
    #   Python gets an iterator from it (if possible), and repeatedly calls `__next__()` to retrieve each item, stopping with a `StopIteration` exception.
    #   You can make your own iterators by creating a class with these methods, like the `ReverseListIterator` above.
    # 
    # In summary:
    # - Generators are a simple way to write iterators using functions and `yield`.
    # - Iterators are more general: any object with `__iter__()` and `__next__()` can act as an iterator.
    # Both tools help us write memory-efficient, lazy-processing code that works with sequences of data.
