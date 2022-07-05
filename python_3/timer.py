from datetime import datetime

def timer_ms(func):
    def wrapper(*args, **kargs):
        start_time = datetime.now()
        result = func(*args, **kargs)
        spent_time = datetime.now() - start_time
        print(result)
        return f'Execution time for {func.__module__}.{func.__name__} is {spent_time.microseconds} ms'
    return wrapper


