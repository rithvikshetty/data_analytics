
- The implimentation uses the fast array manipulation using [`NumPy`] (http://www.numpy.org/).
- Matrix support using [`SciPy`'s] (https://www.scipy.org/) package.
- Simple and efficient tools for prediction using [`sklearn`] (https://scikit-learn.org/stable/)
- File data analysis and manipulation tool using [`pandas`] (https://pandas.pydata.org/)
- Plot interactive visualizations using [`matplotlib`] (https://matplotlib.org/)

 
 

## Installation
- Python 3.xx is required.

Run

    pip3 install -r requirements.txt

(possibly with `sudo`)

That command above will install  `NumPy`, `SciPy`, `sklearn`, `pandas`, and `matplotlib` for you.


## Get the source

Clone the Git repository from GitHub

    git clone https://github.com/ashugowda/CLUSTERING.git



## Select framework parameters

Select optimizers from the list of available ones: "SSA","PSO","GA","BAT","FFA","GWO","WOA","MVO","MFO","CS". For example:

        optimizer=["SSA","PSO","GA"]

Select objective function from the list of available ones:"SSE","TWCV","SC","DB","DI". For example:

        objectivefunc=["SSE","TWCV"] 

Select data sets from the list of available ones
The folder datasets in the repositoriy contains 30 datasets (All of them are obtained from Scikit learn, UCI, School of Computing at University of Eastern Finland, ELKI, KEEL, and Naftali Harris Blog).

To add new dataset:
- Put your dataset in a csv format (No header is required, labels are at the last column)
- Place the new datset files in the datasets folder.
- Add the dataset to the datasets list in the optimizer.py (Line 19).
  
For example, if the dastaset name is seed, the new line  will be like this:

        datasets=["aggregation", "seeds"]

Select number of repetitions for each experiment. 
To obtain meaningful statistical results, usually 30 independent runs are executed for each algorithm.

        NumOfRuns=30

Select general parameters for all optimizers (population size, number of iterations) ....

        params = {'PopulationSize' : 30, 'Iterations' : 50}

Choose whether to Export the results in different formats

        export_flags = {'Export_avg':True, 'Export_details':True, 'Export_details_labels':True, 'Export_convergence':True, 'Export_boxplot':True}

run the framework

        run(optimizer, objectivefunc, dataset_List, NumOfRuns, params, export_flags)

Now your experiment is ready to go. Enjoy!  

The results will be automaticly generated ina folder which is concatnated with the date and time of the experiment. this folder consists of three csv files and two types of plots:
- experiment.csv
- experiment_details.csv
- experiment_details_Labels.csv
- Convergence plot
- Box plot

The experiment and the experiment_details files contain the following measures:

    Optimizer: The name of the used optimizer
    Dataset: The name of the dataset.
    objfname: The objective function/ Fitness function
    Experiment: Experiment ID/ Run ID.
    startTime: Experiment's starting time
    EndTime: Experiment's ending time
    ExecutionTime : Experiment's executionTime (in seconds)
    SSE
    Purity
    Entropy
    HS
    CS
    VM
    AMI
    ARI
    Fmeasure
    TWCV
    SC
    Accuracy
    DI
    DB
    STDev
    Iter1	Iter2 Iter3 Iter4... : Convergence values (The bjective function values after every iteration).	






