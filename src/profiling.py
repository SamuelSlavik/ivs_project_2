## @file profiling.py
# @brief program calculating standard deviation from samples on stdin
# @author Adam Pekný <xpekny00>

import sys
import re
from math_library import MathFunctions

## parse_line
# @brief function formatting line by removing unnecessary white characters and replacing them whit one space
# @param _line is line passed as a string
# @return _line which is the formatted line
def parse_line(_line):
    _line = re.sub("\\s+", " ", _line.strip("\n"))

    if _line[0] == " ":
        _line = _line[1:]
    if _line[-1] == " ":
        _line = _line[:len(_line) - 1]

    return _line


## cnt_line_res
# @brief function that calculates number of samples in line, their sum and sum of samples squared
# @param _data_cnt is current total number of samples
# @param _data_sum is current sum of all samples
# @param _func_sum is current sum of squares of samples
# @param _line is line passed as a string
# @return _data_cnt, _data_sum, _func_sum which are results after processing line
def cnt_line_res(_data_cnt, _data_sum, _func_sum, _line):
    for number in _line.split(" "):
        number_flt = float(number)

        _data_cnt = Math.addition(_data_cnt, 1)
        _data_sum = Math.addition(_data_sum, number_flt)
        _func_sum = Math.addition(_func_sum, Math.power(number_flt, 2))

    return _data_cnt, _data_sum, _func_sum

## @var Math
# Instance of class MathFunctions which provides functions from math library
Math = MathFunctions()

data_sum = 0  # sum of samples
data_avg = 0  # average of samples
data_cnt = 0  # count of samples
func_sum = 0  # sum of samples squared

# for each line on stdin format line and calculate needed information
for line in sys.stdin:
    line = parse_line(line)
    data_cnt, data_sum, func_sum = cnt_line_res(data_cnt, data_sum, func_sum, line)

# calculate average of samples
data_avg = Math.division(data_sum, data_cnt)

# calculate standard deviation - sqrt( (func_sum - data_cnt * data_avg**2) / (data_cnt - 1) )
result = Math.root(2,
                   Math.division(
                       Math.subtraction(
                           func_sum,
                           Math.multiplication(
                               data_cnt,
                               Math.power(data_avg, 2)
                           )  # end of multiplication function (data_cnt * data_avg**2)
                       ),  # end of subtraction function (func_sum - data_cnt * data_avg**2)
                       Math.subtraction(data_cnt, 1)  # end of subtraction function (data_cnt - 1)
                   )  # end of division function (func_sum - data_cnt * data_avg**2) / (data_cnt - 1)
                   )  # end of root function sqrt( (func_sum - data_cnt * data_avg**2) / (data_cnt - 1) )

# print result to stdout
print(result)

# end of file
