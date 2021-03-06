import math
import numpy
import random
import time
from solution import solution
    

def BAT(objf,lb,ub,dim,N,Max_iteration, k, points, metric):
    
    n=N;      # Population size
    #lb=-50
    #ub=50
    
    N_gen=Max_iteration  # Number of generations
    
    A=0.5;      # Loudness  (constant or decreasing)
    r=0.5;      # Pulse rate (constant or decreasing)
    
    Qmin=0         # Frequency minimum
    Qmax=2         # Frequency maximum
    
    
    d=dim           # Number of dimensions 
    
    # Initializing arrays
    Q=numpy.zeros(n)  # Frequency
    v=numpy.zeros((n,d))  # Velocities
    Convergence_curve=[];
    
    # Initialize the population/solutions
    Sol=numpy.random.rand(n,d)*(ub-lb)+lb
    labelsPred=numpy.zeros((n,len(points)))
    Fitness=numpy.zeros(n)

    S=numpy.zeros((n,d))
    S=numpy.copy(Sol)
    
    
    # initialize solution for the final results   
    s=solution()
    print("BAT is optimizing  \""+objf.__name__+"\"")    
    
    # Initialize timer for the experiment
    timerStart=time.time() 
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    
    #Evaluate initial random solutions
    for i in range(0,n):
        startpts = numpy.reshape(Sol[i,:], (k,(int)(dim/k)))
        if objf.__name__ == 'SSE' or objf.__name__ == 'SC' or objf.__name__ == 'DI':
            fitnessValue, labelsPredValues=objf(startpts, points, k, metric) 
        else:
            fitnessValue, labelsPredValues=objf(startpts, points, k) 
        Fitness[i] = fitnessValue
        labelsPred[i,:] = labelsPredValues
    
    
    # Find the initial best solution
    fmin = min(Fitness)
    I=numpy.argmin(Fitness)
    best=Sol[I,:]
    bestLabelsPred=labelsPred[I,:]
       
    # Main loop
    for t in range (0,N_gen): 
        
        # Loop over all bats(solutions)
        for i in range (0,n):
          Q[i]=Qmin+(Qmin-Qmax)*random.random()
          v[i,:]=v[i,:]+(Sol[i,:]-best)*Q[i]
          S[i,:]=Sol[i,:]+v[i,:]
          
          # Check boundaries
          Sol=numpy.clip(Sol,lb,ub)

    
          # Pulse rate
          if random.random()>r:
              S[i,:]=best+0.001*numpy.random.randn(d)
          
    
          # Evaluate new solutions
          startpts = numpy.reshape(S[i,:], (k,(int)(dim/k)))

          if objf.__name__ == 'SSE' or objf.__name__ == 'SC' or objf.__name__ == 'DI':
              fitnessValue, labelsPredValues=objf(startpts, points, k, metric) 
          else:
              fitnessValue, labelsPredValues=objf(startpts, points, k) 
              
          Fnew = fitnessValue
          LabelsPrednew = labelsPredValues
          
          # Update if the solution improves
          if ((Fnew != numpy.inf) and (Fnew<=Fitness[i]) and (random.random()<A) ):
                Sol[i,:]=numpy.copy(S[i,:])
                Fitness[i]=Fnew
                labelsPred[i,:]=LabelsPrednew
           
    
          # Update the current best solution
          if Fnew != numpy.inf and Fnew<=fmin:
                best=numpy.copy(S[i,:])
                fmin=Fnew
                bestLabelsPred=LabelsPrednew
                
        #update convergence curve
        Convergence_curve.append(fmin)        

        if (t%1==0):
            print(['At iteration '+ str(t)+ ' the best fitness is '+ str(fmin)])
    
    
    timerEnd=time.time()  
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=Convergence_curve
    s.optimizer="BAT"   
    s.objfname=objf.__name__
    s.labelsPred = numpy.array(bestLabelsPred, dtype=numpy.int64)
    s.bestIndividual = best
    
    
    
    return s
