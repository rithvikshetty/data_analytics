
import numpy as np
from opfunu.cec.cec2013.unconstraint import Model as MD1
from opfunu.cec.cec2013.unconstraint2 import Model as MD2

problem_size = 100
solution = np.random.uniform(-1, 1, problem_size)

obj1 = MD1(problem_size)
print(obj1.F28(solution))
print(obj1.F25(solution))
print(obj1.F24(solution))

obj2 = MD2(solution)
print(obj2.F1(), obj2.F2(), obj2.F3())


