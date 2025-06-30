def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
    sample_number = 5
    print(f,"the factorial of{sample_number} is :" , factorial(sample_number))