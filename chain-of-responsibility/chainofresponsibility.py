from abc import ABC, abstractmethod


class Handler(ABC):
    _next: 'Handler'

    def __init__(self):
        self.next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, handler: 'Handler'):
        if handler is not None:
            if not isinstance(handler, Handler):
                raise TypeError(f'Given handler has to be subclass of Handler, {handler} was given.')
        self._next = handler

    def run(self, input_data):
        output = self.do_action(input_data)

        if self.next:
            return self.next.run(output)

        return output

    def stop_propagation(self):
        self.next = None

    @abstractmethod
    def do_action(self, input_data):
        pass
