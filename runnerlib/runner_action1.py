from runnerlib import Runner
from abc import ABC, abstractmethod


class RunnerAction1(Runner, ABC):

    @abstractmethod
    def step1(self):
        # Should be overriden in subclass through multiple inheritance
        pass

    @abstractmethod
    def step2(self):
        # Should be overriden in subclass through multiple inheritance
        pass

    def run(self):
        print('Running Action1')
        self.step1()
        self.step2()

