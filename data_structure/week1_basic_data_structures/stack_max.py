#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_stack = []
        self.Max_num=-float('inf')

    def Push(self, a):
        self.__stack.append(a)
        if a >= self.Max_num:
            self.max_stack.append(self.Max_num)
            self.Max_num = a

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack.pop() == self.Max_num:
            self.Max_num=self.max_stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.Max_num


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
