
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer:
    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))


class DecimalViewer:
    def update(self, subject):
        print('DecimalViewer: Subject %s has data %d' % (subject.name, subject.data))


def main():
    data1 = Data('Data1')

    decimal_viewer = DecimalViewer()
    hexadecimal_viewer = HexViewer()

    data1.attach(decimal_viewer)
    data1.attach(hexadecimal_viewer)

    data1.data = 100

    data1.detach(hexadecimal_viewer)
    data1.data = 50


if __name__ == "__main__":
    main()