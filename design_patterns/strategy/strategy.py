# Strategy (with Inheritance, but no contract)

class Sort:
    def __init__(self, description):
        self.description = description

    def sort(self):
        return f'sort generic {self.description}'

class QuickSort(Sort):
    def __init__(self):
        super().__init__("QuickSort")

    def sort(self):
        return f'sorting with {self.description}'

class BubbleSort(Sort):
    def __init__(self):
        super().__init__("BubbleSort")

    def sort(self):
        return f'sorting with {self.description}'

class HeapSort(Sort):
    def __init__(self):
        super().__init__("HeapSort")

    def sort(self):
        return f'sorting with {self.description}'   

class SortingAlgorithm:
    def __init__(self, sorting_algorithm):
        self.sorting_algorithm  = sorting_algorithm

    def sort(self):
        return self.sorting_algorithm.sort()

def main():
    print('sortings..')

    bs = SortingAlgorithm(BubbleSort())
    qs = SortingAlgorithm(QuickSort())
    hs = SortingAlgorithm(HeapSort())
    
    print(bs.sort())
    print(qs.sort())
    print(hs.sort())

    sorting = SortingAlgorithm(HeapSort())
    print(sorting.sort())

if __name__ == "__main__":
    main()