def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

def main():
    # Sample usage of the functions
    name = "Vignesh"
    print(greet(name))

    num1 = 5
    num2 = 7
    print(f"The sum of {num1} and {num2} is {add_numbers(num1, num2)}")

if __name__ == "__main__":
    main()
