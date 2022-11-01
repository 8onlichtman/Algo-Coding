
def f1(a: int, b: float, c: float, d):
    return a, b, c, d


def f2(a: int, b: int):
    return a * b


def f3(a, b):
    return a + b


def safe_call(f, **kwargs):
    """

    :param f:
    :param kwargs:
    :return function f with kwargs as parameters if the annotations are correct, if not we return an error:
    """

    """
    >>> safe_call(f1, a=4, b=5.2, c=36.9, d="hello")
    (4, 5.2, 36.9, 'hello')
    >>> safe_call(f1, a=4, b=5.2, c="matala", d="achat")
    Traceback (most recent call last):
    ...
    NameError: wrong annotations
    >>> safe_call(f2, a=7, b=2)
    14
    >>> safe_call(f3, a=2, b=30)
    32
    >>> safe_call(f3, a="whats", b="app")
    'whatsapp'
    """

    for key, value in kwargs.items():
        if ((f.__annotations__.get(key) != None) and (f.__annotations__.get(key) != type(value))):
            raise NameError('wrong annotations')
    return f(**kwargs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
