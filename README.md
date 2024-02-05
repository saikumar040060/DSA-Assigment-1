# DSA-Assigment-1
## Programming Assignment # 01 Ordered Record Array




## Problem
Add a merge() method to the OrderedRecordArray class (Listing 2-8 and Listing 2-9) so that you can merge one ordered source array into that object’s existing OrderedArray.

The merge should occur only if both objects’ key functions are identical.

Your solution should create a new list big enough to hold the contents of the current (self) list and the merging array list.

Write tests for your class implementation that creates two arrays, inserts some random numbers into them, invokes merge() to add the contents of one to the other, and displays the contents of the resulting array.
The source arrays may hold different numbers of data items.

Your algorithm needs to compare the keys of the source arrays, picking the smallest one to copy to the destination.

You also need to handle the situation when one source array exhausts its contents before the other.

Note that, in Python, you can access a parameter’s private attributes in a manner similar to using self. If the parameter arr is an OrderedRecordArray object, you can access its number of items as arr.__nItems.


## Installation

Install my-Programming Assignment # 01 with npm

```bash
  git clone git clone https://github.com/your-username/ordered-record-array.git


```
    
## Overview
This Python code provides an implementation of an ordered array, allowing the insertion of elements while maintaining sorted order. Also, it includes the capability to merge two arrays with consideration for key functions. The OrderedRecordArray class offers methods for array manipulation and customization of key functions

## Contents
> Usage 
Methods used 

Testing

## Usage
To use the OrderedRecordArray class, import it into your Python script or interactive environment.
>__python__
```Python
from ordered_record_array import OrderedRecordArray

```

Create an instance of the class and utilize its methods for array manipulation:
```Python
# Example Usage
arr = OrderedRecordArray(10)
arr.insert(42)
arr.display()

```


## Methods
'___init_(self, maxSize)__'
>Description: Initializes an instance of the 'OrderedRecordArray' class.

>Parameters:
>maxSize: The maximum size of the array.
'__insert(self, value)__'
>Description: Inserts a new value into the array while maintaining sorted order.

>Parameters:
>value: The value to be inserted.
'__display(self)__'
>Description: Displays the elements of the array.

'__merge(self, arr)__'
>Description: Merges the current array with another array under certain conditions.

>Parameters:
>__'arr'__: The array to be merged.
'__set_key_funcn(self, key_funcn)__'
>Description: Sets a custom key function for the array.

>Parameters:
>__'key_funcn'__: The custom key function.
## Testing

The provided if __name__ == "__main__": block demonstrates how to test the implementation by creating two arrays, filling them with random numbers, displaying the contents, merging one array into another, and displaying the merged array.

```bash
  python your_script.py

```


## Contributing

Your Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this Programming Assignment # 01's `code of conduct`.





## Github Repository
#github-repository https://github.com/saikumar040060/DSA-Assigment-1
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.


## FAQ

#### Question 1
What is the purpose of the OrderedRecordArray class?
>Answer:The OrderedRecordArray class is designed to provide a simple implementation of an ordered array in Python. It allows you to insert elements while maintaining sorted order and provides functionality to merge two arrays with consideration for key functions.

#### Question 2
How can I set a custom key function for the array?
>Answer: Use the set_key_funcn(self, key_funcn) method to set a custom key function for the array. This allows you to define a function that extracts a key from each element, enabling the array to be sorted or merged based on the specified criteria.

#### Question 3
Can I merge two arrays with different key functions?
 >Answer:No, the merge operation requires both arrays to have the same key function. If you attempt to merge arrays with different key functions, the script will print a message indicating that arrays cannot be merged with different key functions.

 #### Question 4
 What is the license for this code?
 >Answer: This code  is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. See the LICENSE file for more details.
 
