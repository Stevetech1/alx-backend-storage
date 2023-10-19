Requirements
All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All of your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
The first line of all your files should be exactly #!/usr/bin/env python3
Your code should use the pycodestyle style (version 2.5)
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions and methods should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
All your functions and coroutines must be type-annotated.
Install Redis on Ubuntu 18.04
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
Use Redis in a container
Redis server is stopped by default - when you are starting a container, you should start it with: service redis-server start

Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.

Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.

In this exercise we will create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

Remember to conserve the original Redis.get behavior if the key does not exist.

Also, implement 2 new methods: get_str and get_int that will automatically parametrize Cache.get with the correct conversion function.

The following code should not raise:

Familiarize yourself with the INCR command and its python equivalent.

In this task, we will implement a system to count how many times methods of the Cache class are called.

Above Cache define a count_calls decorator that takes a single method Callable argument and returns a Callable.

As a key, use the qualified name of method using the __qualname__ dunder method.

Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.

Remember that the first argument of the wrapped function will be self which is the instance itself, which lets you access the Redis instance.

Protip: when defining a decorator it is useful to use functool.wraps to conserve the original function’s name, docstring, etc. Make sure you use it as described here.

Decorate Cache.store with count_calls.

Familiarize yourself with redis commands RPUSH, LPUSH, LRANGE, etc.

In this task, we will define a call_history decorator to store the history of inputs and outputs for a particular function.

Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.

In call_history, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.

call_history has a single parameter named method that is a Callable and returns a Callable.

In the new function that the decorator will return, use rpush to append the input arguments. Remember that Redis can only store strings, bytes and numbers. Therefore, we can simply use str(args) to normalize. We can ignore potential kwargs for now.

Execute the wrapped function to retrieve the output. Store the output using rpush in the "...:outputs" list, then return the output.

Decorate Cache.store with call_history.

In this tasks, we will implement a replay function to display the history of calls of a particular function.

Use keys generated in previous tasks to generate the following output:

creating main file here
In this tasks, we will implement a get_page function (prototype: def get_page(url: str) -> str:). The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.

Start in a new file named web.py and do not reuse the code written in exercise.py.

Inside get_page track how many times a particular URL was accessed in the key "count:{url}" and cache the result with an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow response and test your caching.

Bonus: implement this use case with decorators.
