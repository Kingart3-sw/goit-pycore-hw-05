def caching_fibonacci():
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]
    return fibonacci

if __name__ == "__main__":
    print(" ")
    fib = caching_fibonacci()
    print(f"fib(10) -> Очікувано: 55  | Отримано: {fib(10)}")
    print(f"fib(15) -> Очікувано: 610 | Отримано: {fib(15)}")
    print(f"fib(35) -> Отримано: {fib(35)}")