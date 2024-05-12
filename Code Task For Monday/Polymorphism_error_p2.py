def divide(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please provide two numeric values.")

print(divide(10, 2))
print(divide(5, 0))
print(divide('a', 2))
