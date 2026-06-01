import math
import sys
from pathlib import Path

toolbox_path = Path.cwd() / "support_material" / "input" / "exams"
if str(toolbox_path) not in sys.path:
    sys.path.insert(0, str(toolbox_path))

import exam_tools
from sympy import *
from exam_tools import *

print(f"Klar: {len(exam_tools.__all__)} offentlige navne inkl. fysiske konstanter")

R = 8.314



# opg 30

mCH4 = 5
H = -890

nCH4 = mCH4/molar_mass("CH4")






print(- nCH4 * H)
