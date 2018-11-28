class Observable(object):
    """ Observable class"""

    def __init__(self):
        self.observers = []

    def register(self, *observer):
        for item in observer:
            if item in self.observers:
                continue
            self.observers.append(item)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers():
            observer.update(self)
