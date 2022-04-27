import sys
import re
from math_library import MathFunctions

Math = MathFunctions()

data_sum = 0
data_avg = 0
data_cnt = 0
func_sum = 0
data = []

for line in sys.stdin:
    line = re.sub("\\s+", " ", line.strip("\n"))

    if line[0] == " ":
        line = line[1:]
    if line[-1] == " ":
        line = line[:len(line) - 1]

    for number in line.split(" "):
        number_flt = float(number)

        data_cnt = Math.addition(data_cnt, 1)
        data_sum = Math.addition(data_sum, number_flt)
        func_sum = Math.addition(func_sum, Math.power(number_flt, 2))

data_avg = Math.division(data_sum, data_cnt)

result = Math.root(2,
                   Math.division(
                       Math.subtraction(
                           func_sum,
                           Math.multiplication(
                               data_cnt,
                               Math.power(data_avg, 2)
                           )
                       ),
                       Math.subtraction(data_cnt, 1)
                   )
                   )

print(result)
