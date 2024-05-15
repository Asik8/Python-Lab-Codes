# The finally block, if specified, will be executed regardless if the try block raises an error or not.
x = 100
try:
    print(x)
except NameError:
    print("Variable is not defined")
except:
    print("Something went Wrong!")
finally:
    print("Try Except Segment Ended!")