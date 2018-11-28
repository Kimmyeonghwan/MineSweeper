from abc import ABCMeta, abstractmethod


class Observer(object):
    """ Abstract Observer class"""
    metaclass = ABCMeta

    @abstractmethod
    def update(self, observable):
        pass
