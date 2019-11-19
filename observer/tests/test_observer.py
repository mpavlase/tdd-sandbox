from observer import observer
import pytest
from pytest_mock import mocker


@pytest.fixture
def publisher():
    pub = observer.Publisher()
    return pub


@pytest.fixture
def subscriber():
    sub = observer.Subscriber()
    return sub


@pytest.fixture
def subscriber_factory():
    def wrapper():
        return observer.Subscriber()

    return wrapper


def test_empty_subscriber_list(publisher, subscriber):
    subscribers = publisher.get_subscribers()
    assert len(subscribers) == 0


def test_subscribe_one(publisher, subscriber):
    publisher.subscribe(subscriber)

    subscribers = publisher.get_subscribers()
    assert len(subscribers) == 1
    assert subscriber in subscribers


def test_send_notification_to_empty_subscribers(publisher):
    publisher.send_notification('tu kabel')


def test_send_notification_to_one_subscriber(publisher, subscriber, mocker):
    publisher.subscribe(subscriber)

    mocker.spy(subscriber, 'on_notification')
    publisher.send_notification('tu kabel')

    assert subscriber.on_notification.call_count == 1


def test_send_notification_to_many_subscriber(publisher, subscriber_factory, mocker):
    subscribers = []
    for _ in range(3):
        subscriber = subscriber_factory()
        subscribers.append(subscriber)
        publisher.subscribe(subscriber)
        mocker.spy(subscriber, 'on_notification')

    publisher.send_notification('tu kabel')

    for subscriber in subscribers:
        assert subscriber.on_notification.call_count == 1


def test_unsubscribe(publisher, subscriber, mocker):
    publisher.subscribe(subscriber)
    mocker.spy(subscriber, 'on_notification')
    publisher.send_notification('tu gabel')

    assert subscriber.on_notification.call_count == 1

    publisher.unsubscribe(subscriber)
    publisher.send_notification('tu gabel')

    assert subscriber.on_notification.call_count == 1
