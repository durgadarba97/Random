def fibonacci(f):
    if(f <= 1):
        return f
    return fibonacci(f - 2) + fibonacci(f - 1)


for i in range(20):
    print(fibonacci(i))

