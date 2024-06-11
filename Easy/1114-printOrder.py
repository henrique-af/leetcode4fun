from typing import Callable


class Foo:
    def __init__(self):
        self.counter = 0

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        self.counter = 1

    def second(self, printSecond: "Callable[[], None]") -> None:
        while self.counter != 1:
            pass
        printSecond()
        self.counter = 2

    def third(self, printThird: "Callable[[], None]") -> None:
        while self.counter != 2:
            pass
        printThird()