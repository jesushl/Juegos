import heapq
from heapq import heappush, heappop


def heap_sort(iterables: list) -> list:
    h = []
    for element in iterables:
        heappush(h, element)
    return [heappop(h) for i in range(len(h))]


if __name__ == '__main__':
    a = [7,2,80,9,55]
    _h = heapq.heapify(a)
    print(a)
    print(_h)
    heapq.heappush(a, 10)
    heapq.heappush(a, 1)
    print(a)
    print(heap_sort(a))
