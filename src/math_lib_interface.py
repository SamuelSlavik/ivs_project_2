##
# @file math_lib_interface.py
# @brief interface for GUI communication with math library
# @author Adam Pekný <xpekny00@vutbr.cz>

from src.math_library import MathFunctions

Math = MathFunctions()


class _Operator:
    def __init__(self, symbol, op_num, op_side, priority):
        self.symbol = symbol
        self.op_num = op_num
        self.op_side = op_side
        self.priority = priority


class _Operators:
    def __init__(self):
        self.addition = _Operator('+', 2, 'b', 3)
        self.subtraction = _Operator('-', 2, 'b', 3)
        self.multiplication = _Operator('*', 2, 'b', 2)
        self.division = _Operator('/', 2, 'b', 2)
        self.modulo = _Operator('%', 2, 'b', 1)
        self.power = _Operator('^', 2, 'b', 0)
        self.root = _Operator('~', 2, 'b', 0)
        self.factorial = _Operator('!', 1, 'l', 0)
        self.minus_unary = _Operator('ˇ', 1, 'r', 0)

        self.ops_number = 9


class _BinExpTree:
    def __init__(self, expression):
        if expression.isdigit():
            self.value = expression
            self.left = None
            self.right = None
        else:
            if expression[self.find_low_prio(expression)] != "ˇ":
                self.left = _BinExpTree(expression[0:self.find_low_prio(expression)])
            if expression[self.find_low_prio(expression)] != "!":
                self.right = _BinExpTree(expression[self.find_low_prio(expression) + 1:])
            self.value = expression[self.find_low_prio(expression)]

    ops = _Operators()
    operators = {
        'ˇ': {
            "priority": 0,
            "side": 'r'
        },
        '^': {
            "priority": 0,
            "side": 'b'
        },
        '~': {
            "priority": 0,
            "side": 'b'
        },
        '!': {
            "priority": 0,
            "side": 'l'
        },
        '%': {
            "priority": 1,
            "side": 'b'
        },
        '*': {
            "priority": 2,
            "side": 'b'
        },
        '/': {
            "priority": 2,
            "side": 'b'
        },
        '+': {
            "priority": 3,
            "side": 'b'
        },
        '-': {
            "priority": 3,
            "side": 'b'
        }
    }

    def find_low_prio(self, expression):
        lowest = -1
        lowest_idx = 0
        idx = 0
        for item in expression:
            if item in self.operators:
                if lowest == 0:
                    if self.operators[item]["priority"] > lowest:
                        lowest = self.operators[item]["priority"]
                        lowest_idx = idx
                else:
                    if self.operators[item]["priority"] >= lowest:
                        lowest = self.operators[item]["priority"]
                        lowest_idx = idx
            idx += 1
        return lowest_idx

    def eval(self):
        if self.value.isdigit():
            return self.value
        elif self.value == '+':
            if self.left and self.right:
                return Math.addition(int(self.left.eval()), int(self.right.eval()))
        elif self.value == '-':
            if self.left and self.right:
                return Math.subtraction(int(self.left.eval()), int(self.right.eval()))
        elif self.value == '*':
            if self.left and self.right:
                return Math.multiplication(int(self.left.eval()), int(self.right.eval()))
        elif self.value == '/':
            if self.left and self.right:
                return Math.division(int(self.left.eval()), int(self.right.eval()))
        elif self.value == '%':
            if self.left and self.right:
                return Math.modulo(int(self.left.eval()), int(self.right.eval()))
        elif self.value == '~':
            if self.left and self.right:
                return Math.root(int(self.right.eval()), int(self.left.eval()))
        elif self.value == '!':
            if self.left:
                return Math.factorial(int(self.left.eval()))
        elif self.value == '^':
            if self.left and self.right:
                return Math.power(int(self.left.eval()), int(self.right.eval()))
        elif self.value == 'ˇ':
            if self.right:
                return int('-'+self.right.eval())

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.value)


class MathLibInterface:

    def _sub_unary_minus(self, expression):
        idx = 0
        for item in expression:
            if item == '-' and not expression[idx - 1].isdigit():
                expression = list(expression)
                expression[idx] = 'ˇ'
                expression = ''.join(expression)
            idx += 1

        return expression

    def calc_expression(self, expression):
        expression = self._sub_unary_minus(expression)
        tree = _BinExpTree(expression)
        # tree.print_tree()
        print(f"expression recieved: {expression}")

        return tree.eval()
