def create_handlers(callback):
    for step in range(5):
        yield lambda: callback(step)


def execute_handlers(handlers):
    for handler in handlers:
        print(handler())


def add_one(number):
    return number+1


execute_handlers(create_handlers(add_one))
