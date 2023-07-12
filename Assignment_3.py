#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.


# In[ ]:


The keyword used to create a function in Python is "def". 


# In[8]:


def odd_numbers():
    odd_list = []
    for i in range(1, 26):
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list
odd_numbers()
        
        
    


# In[ ]:


Q2 Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
to demonstrate their use.


# In[ ]:


kwargs are used in functions to allow them to accept a varying number of arguments. *args is used to send a non-keyworded variable length argument list to the function. It allows you to pass a variable number of arguments to a function, which will be received as a tuple. kwargs is used to pass keyworded variable length of arguments to a function, which will be received as a dictionary. Here's an example of how you can use args and *kwargs in a function:


# In[10]:


def print_args(*args):
    print("Arguments passed as *args:", args)
    
def print_kwargs(**kwargs):
    print("Arguments passed as **kwargs:", kwargs)


# In[ ]:


Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
16, 18, 20].


# In[ ]:


An iterator in Python is an object that implements the iterator protocol, which consists of two methods: iter() and next(). The iter() method is used to initialize the iterator object, and the next() method is used for iteration.


# In[11]:


numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

class FiveNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            number = numbers[self.counter]
            self.counter += 1
            return number
        else:
            raise StopIteration

print("The first 5 numbers:")
for number in FiveNumbers(5):
    print(number)


# In[ ]:


Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.


# In[ ]:


A generator function in Python is a function that returns a generator iterator. The yield keyword is used to return a value from a generator function and pause the function's execution. When the generator function is called again, it resumes execution from where it left off, using the saved state from the last call to yield.


# In[12]:


# A simple generator for Fibonacci Numbers
def fib(limit):
	
	# Initialize first two Fibonacci Numbers
	a, b = 0, 1

	# One by one yield next Fibonacci Number
	while a < limit:
		yield a
		a, b = b, a + b

# Create a generator object
x = fib(5)

# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
	print(i)


# In[ ]:


Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers.


# In[13]:


def prime_numbers():
    yield 2
    primes = [2]
    candidate = 3
    while candidate < 1000:
        is_prime = True
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 2

primes = prime_numbers()

print("The first 20 prime numbers:")
for i in range(20):
    print(next(primes))


# In[ ]:


Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.


# In[14]:


a, b = 0, 1
count = 0

while count < 10:
    print(a)
    a, b = b, a + b
    count += 1


# In[ ]:


Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']


# In[15]:


string = 'pwskills'
characters = [char for char in string]
print(characters)


# In[ ]:


Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.


# In[ ]:


def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return original == reverse

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


# In[ ]:


Write a code to print odd numbers from 1 to 100 using list comprehension.


# In[17]:


# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
i = 0

# using while loop
while(i < len(list1)):

	# checking condition
	if list1[i] % 2 != 0:
		print(list1[i], end=" ")

	# increment i
	i += 1



# In[ ]:




