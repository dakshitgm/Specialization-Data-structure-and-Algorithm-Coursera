# python3
def heapify(data, n, i, swaps):
    smallest = i
    left_child = (i * 2) + 1
    right_child = (i * 2) + 2

    if left_child < n and data[left_child] < data[smallest]:
        smallest = left_child

    if right_child < n and data[right_child] < data[smallest]:
        smallest = right_child

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        heapify(data, n, smallest, swaps)


def build_heap(data, n):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in reversed(range(n // 2)):
        heapify(data, n, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data, n)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
