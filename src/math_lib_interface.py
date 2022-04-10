##
# @file math_lib_interface.py
# @brief interface for GUI communication with math library
# @author Adam Pekný <xpekny00@vutbr.cz>
import json

from src.math_library import MathFunctions

##
# @var _Math
# @brief Instance of class containing math methods
#
_Math = MathFunctions()

file = open('../dependencies/operators.json')
##
# @var _operators
# @brief Dictionary containing information about operators loaded from operators.json file in dependencies
#
_operators = json.load(file)

file.close()

##
# Class _TreeNode
# @brief Private class used to create a binary expression tree and containing methods for operations above the tree
#


class _TreeNode:
    ##
    # Constructor
    # @brief Creates binary expression tree from expression stored in string via recursion
    # @param self The instance of class
    # @param expression The expression stored in string
    # Attributes:
    #   value -> can be either operand or operator
    #   left -> left child node
    #   right -> right child node
    # Functionality:
    #   First it checks whether the expression is digit, if yes it means it is leaf node and expression can be stored to
    #   value attribute with no further processing.
    #   If it is not it finds index of operator with the lowest priority and divides expression into two parts around
    #   this index. Then calls constructor on the child nodes passing respective parts of expression.
    #   For highest priority operators first operator found is considered as breaking point (for others last)
    # Example:
    #   tree = _TreeNode("5+2")
    #   Attribute values:
    #       tree.value -> "+" (root)
    #       tree.left -> _TreeNode object (value = "5", left = None, right = None) (leaf)
    #       tree.right -> _TreeNode object (value = "2", left = None, right = None) (leaf)
    #
    def __init__(self, expression):
        if expression.isdigit():
            self.value = expression
            self.left = None
            self.right = None

        else:
            current_operator_idx = self.find_low_prio(expression)
            current_operator = expression[current_operator_idx]

            if _operators[current_operator]["op_side"] != "r":
                self.left = _TreeNode(expression[0:current_operator_idx])

            if _operators[current_operator]["op_side"] != "l":
                self.right = _TreeNode(expression[current_operator_idx + 1:])

            self.value = current_operator

    ##
    # Method find_low_prio
    # @brief Method used to find index of lowest
    # @param expression The expression stored as string
    #
    @staticmethod
    def find_low_prio(expression):
        lowest = -1
        lowest_idx = 0
        current_idx = 0
        for item in expression:
            if item in _operators:
                if lowest == 0:
                    if _operators[item]["priority"] > lowest:
                        lowest = _operators[item]["priority"]
                        lowest_idx = current_idx
                else:
                    if _operators[item]["priority"] >= lowest:
                        lowest = _operators[item]["priority"]
                        lowest_idx = current_idx

            current_idx += 1
            
        return lowest_idx

    def eval_node(self, func):
        if _operators[self.value]["op_number"] == 2:
            if self.left and self.right:
                return func(int(self.left.eval()), int(self.right.eval()))

        elif _operators[self.value]["op_number"] == 1:
            if _operators[self.value]["op_side"] == 'l':
                return func(int(self.left.eval()))

            elif _operators[self.value]["op_side"] == 'r':
                return func(int(self.right.eval()))

    def eval(self):
        if self.value.isdigit():
            return self.value
        else:
            func_name = _operators[self.value]["func_name"]
            func = getattr(_Math, func_name)

            return self.eval_node(func)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.value)


class MathLibInterface:

    @staticmethod
    def _sub_unary_minus(expression):
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
        tree = _TreeNode(expression)
        print(f"expression recieved: {expression}")

        return tree.eval()
