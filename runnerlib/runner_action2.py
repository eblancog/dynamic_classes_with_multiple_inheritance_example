from runnerlib import Runner
from abc import ABC, abstractmethod


class RunnerAction2(Runner, ABC):

    @abstractmethod
    def step1(self):
        # Should be overriden in subclass through multiple inheritance
        pass

    @abstractmethod
    def step2(self):
        # Should be overriden in subclass through multiple inheritance
        pass

    def run(self):
        print('Running Action2')
        self.step1()
        self.step2()


