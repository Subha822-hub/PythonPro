def logging_decorator(function):
  def wrapper_function(*args):
    print(f"You called {function.__name__}{args}")
    result = function(args[0],args[1],args[2])
    print(f"It returned: {result}")
  return wrapper_function

# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(2, 3, 4)


# Output

# You called a_function(2, 3, 4)
# It returned: 24