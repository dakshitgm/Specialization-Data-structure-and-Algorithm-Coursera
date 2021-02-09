# python3
class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.max_stack = []
        self.Max_num = -float("inf")

    def Push(self, a):
        self.__stack.append(a)
        if a >= self.Max_num:
            self.max_stack.append(self.Max_num)
            self.Max_num = a

    def Pop(self):
        assert len(self.__stack)
        pop_elem = self.__stack.pop()
        if pop_elem == self.Max_num:
            self.Max_num = self.max_stack.pop()
        return pop_elem

    def Max(self):
        return self.Max_num

    def is_empty(self):
        return len(self.__stack) == 0


class window_que:
    def __init__(self):
        self.stack_1 = StackWithMax()
        self.stack_2 = StackWithMax()

    def enque(self, key):
        self.stack_1.Push(key)

    def deque(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.Push(self.stack_1.Pop())
        return self.stack_2.Pop()

    def get_max(self):
        return max(self.stack_1.Max(), self.stack_2.Max())


def max_sliding_window_naive(sequence, m):
    maximums = []
    que = window_que()
    for i in range(0, m):
        que.enque(sequence[i])
    maximums.append(que.get_max())
    for i in range(m, len(sequence)):
        que.deque()
        que.enque(sequence[i])
        maximums.append(que.get_max())
    return maximums


if __name__ == "__main__":
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

