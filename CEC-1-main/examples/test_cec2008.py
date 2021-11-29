

import numpy as np
from opfunu.cec.cec2008.F7 import Model

t1 = Model()

temp = np.array([0.5, 1, 1.5, 2, 3, 0.9, 1.2, 2, 1, 5])

result = t1._main__(temp)

print(result)
