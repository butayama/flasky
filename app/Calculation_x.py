"""  Calculation.py

     test output with jinja2"""

from math import radians, atan2, sqrt, tan, degrees, sin, cos, acos
from ansimarkup import ansiprint
from os import system, getcwd
from os.path import join
import sys
from app.file_handling import text_file_object

class CalculateAngles:


    def calculate(c_a_d, s_a_d, t_a_d):
        # filename = f"result/single_cut_rotational_osteotomy_{c_a_d}" + "_" + f"{s_a_d}" + "_" + f"{t_a_d}" + ".txt"
        input: {{ c_a_d, s_a_d, t_a_d }}
        # c_a = radians(c_a_d)
        # s_a = radians(s_a_d)
        # t_a = radians(t_a_d)
        #
        # h1 = sqrt(tan(c_a) * tan(c_a) + tan(s_a) * tan(s_a))
        # a_tad = atan2(h1, 1)
        # a_oa = atan2(tan(s_a), tan(c_a))
        # a_azi = atan2(-(sin(a_oa) + sin(a_oa - t_a)), (cos(a_oa) + cos(a_oa - t_a)))
        # a_ele = atan2(2 * sin(a_tad) * cos(0.5 * t_a), sin(t_a) * (1 + cos(a_tad)))
        # a_aor = acos(0.5 * (cos(t_a) + cos(a_tad) + cos(t_a) * cos(a_tad) - 1))
        # return filename, c_a_d, s_a_d, t_a_d, c_a, s_a, t_a, a_tad, a_oa, a_azi, a_ele, a_aor


    # if __name__ == "__main__":
    #     filename, c_a_d, s_a_d, t_a_d, c_a, s_a, t_a, a_tad, a_oa, a_azi, a_ele, a_aor = calculate()
    #     screen_out(filename, c_a_d, s_a_d, t_a_d, c_a, s_a, t_a, a_tad, a_oa, a_azi, a_ele, a_aor)
    #     txt_out(filename, c_a_d, s_a_d, t_a_d, c_a, s_a, t_a, a_tad, a_oa, a_azi, a_ele, a_aor)
