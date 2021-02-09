# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1

    maxP=0
    for i in range(pivot_element.row, len(a)):
        if(abs(a[i][pivot_element.column])>abs(maxP)):
            maxP=a[i][pivot_element.column]
            pivot_element.row=i

    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def scale_pivot(a, b, pivot_element):
    divisor = a[pivot_element.row][pivot_element.column]

    for j in range(pivot_element.column, len(a)):
        a[pivot_element.row][j] /= divisor

    b[pivot_element.row] /= divisor

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    multiple = 0

    scale_pivot(a, b, pivot_element)

    for i in range(pivot_element.row+1, len(a)):
        multiple=a[i][pivot_element.column];
        for j in range(pivot_element.column, len(a)):
            a[i][j] -= (a[pivot_element.row][j] * multiple)

        b[i] -= (b[pivot_element.row] * multiple)
    
def back_substitution(a, b):
    for i in reversed(range(0, len(a))):
        v=b[i]
        for j in range(0, i):
            b[j] -= a[j][i] * v
            a[j][i] = 0

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    back_substitution(a, b)

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
