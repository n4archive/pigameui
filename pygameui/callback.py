import collections


class Signal(object):
    "A simple signal - slot mechanism"

    # TODO use weak refs? really?

    def __init__(self):
        self.slots = []

    def connect(self, slot):
        "slot: is a function / method"

        assert isinstance(slot, collections.Callable)
        self.slots.append(slot)

    def __call__(self, *args, **kwargs):
        "Fire the signal to connected slots"

        for slot in self.slots:
            slot(*args, **kwargs)
