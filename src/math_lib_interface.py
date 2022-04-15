##
# @file math_lib_interface.py
# @brief interface for GUI communication with math library
# @author Adam Pekný <xpekny00@vutbr.cz>
import json
import re

from src.math_library import MathFunctions


def _is_numeric(expression):
    try:
        float(expression)
        return True
    except ValueError:
        return False


def _save_int_float(expression):
    return float(expression) if float(expression) - int(float(expression)) != 0 else int(expression)


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
        if _is_numeric(expression):
            self.value = _save_int_float(expression)
            self.left = None
            self.right = None

        else:
            current_operator_idx = self.find_low_prio(expression)
            current_operator = expression[current_operator_idx]
            self.left = None
            self.right = None

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

    def eval_self(self, func):
        if _operators[self.value]["op_number"] == 2:
            if self.left and self.right:
                return func(self.left.eval_tree(), self.right.eval_tree())

        elif _operators[self.value]["op_number"] == 1:
            if _operators[self.value]["op_side"] == 'l':
                return func(self.left.eval_tree())

            elif _operators[self.value]["op_side"] == 'r':
                return func(self.right.eval_tree())

    def eval_tree(self):
        if _is_numeric(self.value):
            return self.value
        else:
            func_name = _operators[self.value]["func_name"]
            func = getattr(_Math, func_name)
            return self.eval_self(func)

    def print_tree(self):
        if self.value in _operators:
            print('(', end=" ")
        if self.left:
            self.left.print_tree()
        print(self.value, end=" ")
        if self.right:
            self.right.print_tree()
        if self.value in _operators:
            print(')', end=" ")


class MathLibInterface:

    @staticmethod
    def _validate_exp_syntax(expression):
        item_idx = 0
        for item in expression:
            if not (_is_numeric(item) or item in _operators or item == '.'):
                return False
            if item in _operators:

                if _operators[item]["op_number"] == 1:
                    if _operators[item]["op_side"] == 'r':
                        if item_idx >= len(expression) - 1:
                            return False
                        if not _is_numeric(expression[item_idx + 1]) and expression[item_idx + 1] != item:
                            return False
                    elif _operators[item]["op_side"] == 'l':
                        if item_idx <= 0:
                            return False
                        if not _is_numeric(expression[item_idx - 1]) and expression[item_idx - 1] != item:
                            return False

                elif _operators[item]["op_number"] > 1:
                    if item_idx == 0 or item_idx >= len(expression) - 1:
                        return False
                    if not _is_numeric(expression[item_idx - 1]) and _operators[expression[item_idx - 1]]["op_number"] != 1:
                        return False
                    if not _is_numeric(expression[item_idx + 1]) and _operators[expression[item_idx + 1]]["op_number"] != 1:
                        return False

            item_idx += 1
        return True

    @staticmethod
    def _sub_unary_minus(expression):
        idx = 0
        for item in expression:
            if item == '-' and (idx == 0 or not _is_numeric(expression[idx - 1])):
                expression = list(expression)
                expression[idx] = 'ˇ'
                expression = ''.join(expression)
            idx += 1

        return expression

    def calc_expression(self, expression):
        expression = self._sub_unary_minus(expression)

        if not self._validate_exp_syntax(expression):
            raise SyntaxError

        tree = _TreeNode(expression)

        return _save_int_float(tree.eval_tree())
