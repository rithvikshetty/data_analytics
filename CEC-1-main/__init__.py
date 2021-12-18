import optimizer as opt
import os
os.chdir("HYBRID/")
optimizer=["HYBRID"] 
objectivefunc=["F3","F4"]  
NumOfRuns=10  
params = {'PopulationSize' : 30, 'Iterations' : 10}
export_flags = {'Export_avg':True, 'Export_details':True, 'Export_convergence':True, 'Export_boxplot':True}


opt.run(optimizer,objectivefunc,NumOfRuns,params,export_flags)