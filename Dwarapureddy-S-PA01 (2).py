import random

class OrderedRecordArray:
    def __init__(self, maxSize):
        # Initialize the array, number of items, and the key function
        self._x = [None] * maxSize
        self._nItems = 0
        self._key_funcn = lambda a: a  # Initialize key_func to a default lambda function

    def size(self):
        # Return the number of items in the array
        return self._nItems

    def insert(self, value):
        # Insert a new value into the array while maintaining sorted order
        if self._nItems == 0:
            self._x[0] = value
            self._nItems += 1
        else:
            j = self._nItems
            while j > 0 and self._x[j-1] > value:
                self._x[j] = self._x[j-1]
                j -= 1
            self._x[j] = value
            self._nItems += 1

    def display(self):
        # Display the elements of the array
        for i in range(self._nItems):
            print(self._x[i], end=' ')
        print()

    def merge(self, arr):
        # Merge the current array with another array under certain conditions
        if self._nItems == 0:
            # If the current array is empty, copy the content of the other array
            self._x = arr._x.copy()
            self._nItems = arr._nItems
            return

        if self._nItems + arr._nItems > len(self._x):
            # If the combined size exceeds the capacity, print a message and return
            print("Arrays are too large to merge.")
            return

        if self._key_funcn != arr._key_funcn:
            # If key functions are different, print a message and return
            print("Cannot merge arrays with different key functions.")
            return

        # Initialize pointers for iteration and a new array for merging
        merged_array = [None] * (self._nItems + arr._nItems)
        i = j = k = 0

        while i < self._nItems and j < arr._nItems:
            # Merge the two arrays into a new array
            if self._x[i] < arr._x[j]:
                merged_array[k] = self._x[i]
                i += 1
            else:
                merged_array[k] = arr._x[j]
                j += 1
            k += 1

        while i < self._nItems:
            # Append remaining elements from the current array
            merged_array[k] = self._x[i]
            i += 1
            k += 1

        while j < arr._nItems:
            # Append remaining elements from the other array
            merged_array[k] = arr._x[j]
            j += 1
            k += 1

        # Update the current array with the merged array and adjust _nItems
        self._x = merged_array
        self._nItems += arr._nItems

    def set_key_funcn(self, key_funcn):
        # Set a custom key function
        self._key_funcn = key_funcn


# Testing the implementation
if __name__ == "__main__":
    def key_funcn(a):
        return a

    # Create two arrays and fill them with random numbers
    firstarray1 = OrderedRecordArray(10)
    secondarray2 = OrderedRecordArray(8)
    firstarray1.set_key_funcn(key_funcn)
    secondarray2.set_key_funcn(key_funcn)

    for i in range(5):
        firstarray1.insert(random.randint(1, 100))

    for j in range(5):
        secondarray2.insert(random.randint(1, 100))

    # Display the contents of the arrays before merging
    print("First Array 1:")
    firstarray1.display()
    print("Second Array :")
    secondarray2.display()

    # Merge array2 into array1
    firstarray1.merge(secondarray2)

    # Display the contents of the merged array
    print("Merged Array:")
    firstarray1.display()

