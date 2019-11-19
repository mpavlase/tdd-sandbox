from abc import ABC, abstractmethod
from typing import Iterable, AnyStr, Set


class IPublisher(ABC):
    @abstractmethod
    def get_subscribers(self) -> Iterable:
        pass

    @abstractmethod
    def subscribe(self, subscriber: 'ISubscriber'):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: 'ISubscriber'):
        pass

    @abstractmethod
    def send_notification(self, message: AnyStr):
        pass


class ISubscriber(ABC):
    @abstractmethod
    def on_notification(self, message: AnyStr):
        pass


class Publisher(IPublisher):
    _subscribers: Set[ISubscriber]

    def __init__(self):
        self._subscribers = set()

    def subscribe(self, subscriber: 'ISubscriber'):
        self._subscribers.add(subscriber)

    def send_notification(self, message: AnyStr):
        for subscriber in self._subscribers:
            subscriber.on_notification(message)

    def get_subscribers(self) -> Iterable:
        return self._subscribers

    def unsubscribe(self, subscriber: 'ISubscriber'):
        self._subscribers.discard(subscriber)


class Subscriber(ISubscriber):
    def on_notification(self, message: AnyStr):
        pass
        #print(message)
