def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
print(f"{next(fib)}\n{next(fib)}\n{next(fib)}\n{next(fib)}\n{next(fib)}\n{next(fib)}\n{next(fib)}\n{next(fib)}")

