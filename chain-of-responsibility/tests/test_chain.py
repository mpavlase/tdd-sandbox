from chainofresponsibility import Handler
from pytest import raises, fixture

# unix like 'pipe' example

# even is 2, 4, ...
# produce_data | filter_even | count_numbers


@fixture
def empty_handler_class():
    class TestHandler(Handler):
        def do_action(self, input_data):
            pass

    return TestHandler


@fixture
def passthrough_handler_class():
    class TestHandler(Handler):
        def do_action(self, input_data):
            return input_data

    return TestHandler


@fixture
def not_implemented_handler_class():
    class TestHandler(Handler):
        pass

    return TestHandler


def test_not_implemented_handler(not_implemented_handler_class):
    with raises(TypeError):
        not_implemented_handler_class()


def test_set_invalid_handler(empty_handler_class):
    handler = empty_handler_class()
    with raises(TypeError):
        handler.next = object


def test_valid_handler(empty_handler_class):
    handler_a = empty_handler_class()
    handler_b = empty_handler_class()

    handler_a.next = handler_b


def test_chain_handlers(passthrough_handler_class, mocker):
    handler_a = passthrough_handler_class()
    handler_b = passthrough_handler_class()

    handler_a.next = handler_b

    mocker.spy(handler_b, 'run')

    assert handler_a.run('abc') == 'abc'
    assert handler_b.run.call_count == 1


def test_stop_propagation(passthrough_handler_class, mocker):
    handler_a = passthrough_handler_class()
    handler_b = passthrough_handler_class()

    handler_a.next = handler_b
    handler_a.stop_propagation()

    mocker.spy(handler_b, 'run')

    assert handler_a.run('abc') == 'abc'
    assert handler_b.run.call_count == 0
