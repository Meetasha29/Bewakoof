"""
Metaprogramming - It is a code which basically manipulated code. For example decorators - they implement another code on the
method and return the method object on runtime. For example the @property decorator.

In python all the variables, methods, classes are objects. Each object in python has a type which is defined by the class creating it.
For example int is created by int class and hence the type id INT. Since the class is also an object its type is type i.e a class is
created by another class called type(Metaclass).

So in the same way we modify our other objects such as int we can also modify our classes and methods during run time.
Methods as discussed are done by decorators and for classes also we can add  or remove fields or methods.

Here is an example to show how we can create our own metaclass to create a new method in a class during run time.
"""


def added_method():
    print("this is a new method")

