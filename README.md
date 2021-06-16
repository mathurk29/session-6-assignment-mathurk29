# EPAI Session 6

# Revision

The default arguments to a function are evaluated when the module is loaded. Hence beware of using mutable object as value to default arguments in function.

**First-class objects**:
- can be sent as function argument
- can be returned by a function
- can be assigned to a variable
- can be stored in data structures
- ex: int, float, string, tuple, list, **functions**

**Higher order functions**:
- take function as argument
and/or
- return function

**Docstring**:

- The string/multi-line string present in the first line of the function is called Docstring.
- help() returns Docstring 
- stored in \__doc__ property

**Annotations**:

- **expressions** about arguments and return value
- stored in __annotations__ property

<br>

# Lambda Expressions / Anonymous Functions

```python 
def func_name(parameter_list):
    return single_line_expression
```
can be written in shorthand as:

```python
lambda parameter_list: single_line_expression
```

Notice the keywords **_def_** and **_return_** are <u>_removed_</u> and **_lambda_** is introduced.
Note: We can not use assignment in single_line_expression

- The 'body' of lambda can have a single expression.

<br>

# Functional Introspection

In Python, everything is an object! So are functions!


Functions are first class objects. They have several attributes that comprises of all info that makes up the function definition and other properties.

Also there is an `inspect` builtin Python module which is used learn about properties of python objects.

A `function's attributes` and `inspect` module together comprises `Functional Introspection`

## 1. Function's attributes

An important builint to check attributes available to an object is **dir()** function

> Few important attributes are:
>
>\_\_**doc**__
>
>\_\_**annotations**__
>
>\_\_**name**__  name of function 
>
>\_\_**defaults**__ tuple containing positional parameter defaults 
>
>\_\_**kwdefaults**__ dictionary containing keyword-only parameter defaults 
>
>\_\_**code**__  an object with several attributes about the definition
>
>\_\_**code**__.**varnamess**  a tuple having parameters first, followed by  local >variables
>
>\_\_**code**__.**argcount** number of fixed params (does not count *args, **kwargs)


We can also attach our own attributes.
```python
def my_func(a,b):
    return a+b

my_func.att1 = "My attribute"
````

## 2. Inspect Module 

In a class, we can define functions in two ways:
1. For calling, we have to create an instance of the class.
2. We can call directly

If we define a function using 1, the function is called a <u>method</u>.

`Method`: An _**instance method**_ or simply a **_method_** IS a function that is bound to some object. 

Note: Classes are not the only way of binding a function to some object.


```python
class MyClass:
    # instance method: bounded to the OBJ of the MyClass
    def f_instance(self):
        pass

    # class method: bounded to the Class MyClass (and by inheritance to its objects too)
    @classmethod
    def f_class(cls):
        pass

    # static methods: are bounded neither to the class or its instance 
    @staticmethod
    def f_static():
        pass

# Accessing using class name:
inspect.isfunction(MyClass.f_instance), inspect.ismethod(MyClass.f_instance)
> (True, False)

inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class)
> (False, True)

inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static)
> (True, False)

```

```python
my_obj = MyClass()

# Accessing using class instance:
inspect.isfunction(my_obj.f_instance), inspect.ismethod(my_obj.f_instance)
> (False, True)

inspect.isfunction(my_obj.f_class), inspect.ismethod(my_obj.f_class)
> (False, True)

inspect.isfunction(my_obj.f_static), inspect.ismethod(my_obj.f_static)
> (True, False)

```




## Callable
Callable is an object that can be called using () and it **returns** a value.
Diff types of callables:

- classes instances having \_\_call__ implemented
- classes - cz calling class_name() in turns calls \_\_init__() - which is callable - it is callabe bcz it *returns* reference of an instance of the class
- class methods
- user-defined: def/lambda
- built-in: len()



## Reducing Functions - Take a list and return a single value

```python
from functools import reduce
```
1. Apply a function (or callable) to the first two items in an iterable and generate a partial result.
2. Use that partial result, together with the third item in the iterable, to generate another partial result.
3. Repeat the process until the iterable is exhausted and then return a single cumulative value.

For ex: max(), sum(), min(), any(), all() etc.

all() - True if every elements are Truthy

any() - True if any element is Truthy

```python
#implementing any using reduce

from functools import reduce

reduce(lambda a,b: bool(a) or bool(b), l)  
```

# Partial Functions
```python
from functools import partial

def pow(base,exponent):
    return base**exponent

square = partial(pow, exponent=2)

exp = 3
cube = partial(pow, exponent=exp) #3 is baked into exponent.

exp=4
cube = partial(pow, exponent=exp) #3 is baked into exponent, exp is not reevaluated

```


# part1.py 

The logic of poker game and the wrapper function to call is provided in the part1.py file. 

The wrapper function ***play_poker*** takes the hands of two players as it's two arguments. 

<u>The hands should be a list of cards, where the cards are tuples of format ('\<suit of the card>', '\<rank of the card>')</u>

This file comprises of these functions:

*Validations*:

1. Checking if card belongs to the deck.
2. Verify format of the input arguments.
3. Cross check if a card is present more than once in the dealt cards.

*convert_faces_to_numbers*: 

Modify cards of input hands to integral values for easy computation of their comparisons.

*find_hand_type*:

Returns the type of hand. This is called by find_winner for each player to determine the type of hand owned by the players.

*compare_hands*: 

Compare the two hands owned by the players and tell which has an upper hand. This is able to compare the 10 types of poker hands with each other, as well as two hands of same type.

*play_poker*:

The wrapper function which calls the above utility functions and retrun a tuple ('type of hand', 'the hand which won').

# test_part1.py

All the test cases are self-explanatory. Additional inline comments are provided wherever deemed required.