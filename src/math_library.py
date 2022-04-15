##
# @file math_library.py
# @brief Mathematical library for calculator
# @author Michal Ľaš <xlasmi00@vutbr.cz>
#


class MathFunctions:

    ##
    # @brief function for adding 2 numbers
    # @param num1 first number
    # @param num2 second number
    # @return addition of num1 and num2 (num1 + num2)
    #
    def addition(self, num1: float, num2: float):
        return round(num1 + num2, 14)

    ##
    # @brief function for subtracting 2 number 
    # @param num1 first number
    # @param num2 second number
    # @return subtraction of num1 and num2 (num1 - num2)
    #
    def subtraction(self, num1: float, num2: float):
        return round(num1 - num2, 14)

    ##
    # @brief function for multiplying two numbers
    # @param num1 first number
    # @param num2 second number
    # @return multiplication of num1 and num2 (num1 * num2)
    #
    def multiplication(self, num1: float, num2: float):
        return round(num1 * num2, 14)

    ##
    # @brief function for dividing two numbers
    # @param num1 is dividend
    # @param num2 is divisor
    # @return division of num1 and num2 (num1 / num2)
    # @exception num2 cannot be 0 -> ZeroDivisionError
    #
    def division(self, num1: float, num2: float):
        try:
            return round(num1 / num2, 14)
        except ZeroDivisionError:
            raise ZeroDivisionError
            
    ##
    # @brief function for making factorial from number
    # @param num1 is the number that factorial comes from
    # @return factorial from number num1 (num1!)
    # @exception num1 cannot be negative number -> ValueError
    # @exception num1 cannot be decimal number -> ValueError
    #
    def factorial(self, num1: int):
        if num1 < 0 or isinstance(num1, float):
            raise ValueError("Factorial can be made only from integers and positive numbers.")
        else:
            fact = 1
            for i in range(1, num1+1):
                fact *= i
            return round(fact, 14)

    ##
    # @brief function to power 2 numbers
    # @param num1 will be raised to the power of to_the_power
    # @param to_the_power is the power that num1 is raised to
    # @return num1 raised to power of to_the_power
    # @exception to_the_power cannot be negative number -> ValueError
    # @exception to_the_power cannot be decimal number -> ValueError
    #
    def power(self, num1: float, to_the_power: int):
        if to_the_power < 0 or isinstance(to_the_power, float):
            raise ValueError("Power to function supports only integers and positive numbers.")
        else:
            return round(num1 ** to_the_power, 14)

    ##
    # @brief function root 2 numbers
    # @param num1 number of which root is calculated
    # @param root is na exponent of root
    # @return root of num1
    # @exception root cannot be 0 -> ZeroDivisionError
    # @exception if num1 is negative number and root % 2 is 0 -> ValueError
    #
    def root(self, root: float, num1: float):
        if num1 < 0 and (root % 2) == 0:
            raise ValueError("Root function only support real numbers (no complex numbers).")
        elif num1 == 0 and root <= 0:
            raise ZeroDivisionError
        else:
            try:
                if num1 >= 0:
                    return round(num1 ** (1 / root), 14)
                else:
                    return round(-((-num1) ** (1 / root)), 14)
            except ZeroDivisionError:
                ZeroDivisionError

    ##
    # @brief function for modulo dividing
    # @param @param num1 is dividend
    # @param num2 is divisor (can not be 0)
    # @return modulo division of num1 and num2 (num1 % num2)
    # @exception num2 cannot be 0 -> ZeroDivisionError
    #
    def modulo(self, num1: float, num2: float):
        try:
            return round(num1 % num2, 14)
        except ZeroDivisionError:
            raise ZeroDivisionError

    def unary_minus(self, num1: float):
        return -num1
