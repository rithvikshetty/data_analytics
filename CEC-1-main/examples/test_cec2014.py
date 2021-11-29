

import numpy as np
from opfunu.cec.cec2014.function import *
from opfunu.cec.cec2014.unconstraint2 import Model as MD2
from opfunu.cec.cec2014.unconstraint import Model as MD

problem_size = 10
epoch = 500
solution = np.random.uniform(0, 1, problem_size)


result1 = F1(solution)
print(result1)

result2 = MD2(solution)
print(result2.F1())

result3 = MD(problem_size)
print(result3.F1(solution))

func = MD(10).F2
from mealpy.swarm_based.WOA import BaseWOA
from mealpy.swarm_based.SpaSA import BaseSpaSA
from mealpy.evolutionary_based.GA import BaseGA
from mealpy.swarm_based.GWO import BaseGWO
from mealpy.human_based.TLO import BaseTLO
from mealpy.human_based.QSA import ImprovedQSA
from mealpy.physics_based.EFO import BaseEFO

temp1 = BaseTLO(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
temp1._train__()

temp1 = BaseSpaSA(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
temp1._train__()

temp2 = BaseEFO(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
temp2._train__()

temp2 = ImprovedQSA(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
temp2._train__()


























