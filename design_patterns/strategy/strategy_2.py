# Strategy 2 (with Abstract Class)

from abc import ABC, abstractmethod

class Sort(ABC):
    @abstractmethod
    def sort(self):
       pass

class QuickSort(Sort):
    def sort(self):
        return 'sorting with QuickSort'

class BubbleSort(Sort):
    def sort(self):
        return 'sorting with BubbleSort'

class HeapSort(Sort):
    def sort(self):
        return 'sorting with HeapSort'   

class AnotherSort(Sort):
    def sort(self):
        return 'another'

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

def main():
    context = Context(QuickSort())
    print(context.strategy.sort())

    context2 = Context(BubbleSort())
    print(context2.strategy.sort())

    context3 = Context(AnotherSort())
    print(context3.strategy.sort())







if __name__ == "__main__":
    main()