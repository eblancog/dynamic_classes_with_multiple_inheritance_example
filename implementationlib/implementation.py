from abc import ABC, abstractmethod


class Implementation(ABC):

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

