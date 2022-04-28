import sys
import re
from math_library import MathFunctions


def parse_line(_line):
    _line = re.sub("\\s+", " ", _line.strip("\n"))

    if _line[0] == " ":
        _line = _line[1:]
    if _line[-1] == " ":
        _line = _line[:len(_line) - 1]

    return _line


def cnt_line_res(_data_cnt, _data_sum, _func_sum, _line):
    for number in _line.split(" "):
        number_flt = float(number)

        _data_cnt = Math.addition(_data_cnt, 1)
        _data_sum = Math.addition(_data_sum, number_flt)
        _func_sum = Math.addition(_func_sum, Math.power(number_flt, 2))

    return _data_cnt, _data_sum, _func_sum


Math = MathFunctions()

data_sum = 0
data_avg = 0
data_cnt = 0
func_sum = 0

for line in sys.stdin:
    line = parse_line(line)
    data_cnt, data_sum, func_sum = cnt_line_res(data_cnt, data_sum, func_sum, line)

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
