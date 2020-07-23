def decorator(input_str):
    return f'({input_str})'


def decorator_as_fn(fn):
    def wrapper(*args, **kwargs):
        value = fn(*args, **kwargs)
        return f'({value})'
    return wrapper
