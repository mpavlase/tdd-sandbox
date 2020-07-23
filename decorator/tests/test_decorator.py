from decorator.decorator import decorator
from pytest import fixture


@fixture
def input_str():
    return 'abc'


def test_returned_instance_has_same_subtype_as_original(input_str):
    assert type(decorator(input_str)) == type(input_str)


def test_without_decorator(input_str):
    assert input_str == 'abc'


def test_decorated_text(input_str):
    assert decorator(input_str) == '(abc)'


def test_multiple_decorated_text(input_str):
    assert decorator(decorator(input_str)) == '((abc))'
