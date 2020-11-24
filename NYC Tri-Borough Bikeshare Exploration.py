# Getting Libraries & Functions
# install the pint function which works with units in python
# The modsimpy is needed for State and flip functions
!pip install modsimpy
!pip install pint

# import functions from the modsim library
from modsim import *

# Initializing values for 5 boroughs
bikeshare = State(Brooklyn=30, Bronx=30, Manhattan=30, Queens=30, StatenIsland=30)

# Defining Functions
def step(state, p1, p2, p3, p4, p5):
    '''
    Simulate one minute of time.
    
    state: bikeshare State object
    p1: probability of a bike coming to Brooklyn
    p2: probability of a bike coming to Bronx
    p3: probability of a bike coming to Queens
    p4: probability of a bike coming to Manhattan
    p5: probability of a bike coming to Staten Island
    '''

    # The flip(p1=0.20) means that it has 20% chance the function will come True and 
    #     80% chance it will come fFalse 
    if flip(p1):
        bike_to_Brooklyn(state)
    
    if flip(p2):
        bike_to_Bronx(state)
        
    if flip(p3):
        bike_to_Queens(state)

    if flip(p4):
        bike_to_Manhattan(state)

    if flip(p5):
        bike_to_StatenIsland(state)
        
        
 def bike_to_Brooklyn(state):
    '''
    Move a bike from Queens to Brooklyn or
    Move a bike from Bronx to Brooklyn or
    Move a bike from Manhattan to Brooklyn or
    Move a bike from Staten Island to Brooklyn
      
    state: bikeshare State object
    '''
    
    if state.Queens == 0:
        return
    state.Queens -= 1
    state.Brooklyn += 1
    
    if state.Bronx == 0:
        return
    state.Bronx -= 1
    state.Brooklyn += 1

    if state.Manhattan == 0:
        return
    state.Manhattan -= 1
    state.Brooklyn += 1

    if state.StatenIsland == 0:
        return
    state.StatenIsland -= 1
    state.Brooklyn += 1
 
def bike_to_Bronx(state):
    '''
    Move a bike from Brooklyn to Bronx or
    Move a bike from Queens to Bronx or
    Move a bike from Manhattan to Bronx or
    Move a bike from Staten Island to Bronx

    state: bikeshare State object
    ''' 
    
    if state.Brooklyn == 0:
        return
    state.Brooklyn -= 1
    state.Bronx += 1
    
    if state.Queens == 0:
        return
    state.Queens -= 1
    state.Bronx += 1

    if state.Manhattan == 0:
        return
    state.Manhattan -= 1
    state.Bronx += 1

    if state.StatenIsland == 0:
        return
    state.StatenIsland -= 1
    state.Bronx += 1
    
 
def bike_to_Queens(state):
    '''
    Move a bike from Bronx to Queens or
    Move a bike from Brooklyn to Queens or
    Move a bike from Manhattan to Queens or
    Move a bike from Staten Island to Queens

    state: bikeshare State object
    '''

    if state.Bronx == 0:
        return
    state.Bronx -= 1
    state.Queens += 1
    
    if state.Brooklyn==0:
        return
    state.Brooklyn -= 1
    state.Queens += 1

    if state.Manhattan == 0:
        return
    state.Manhattan -= 1
    state.Queens += 1

    if state.StatenIsland == 0:
        return
    state.StatenIsland -= 1
    state.Queens += 1
    
  
def bike_to_Manhattan(state):
    '''
    Move a bike from Bronx to Manhattan or
    Move a bike from Brooklyn to Manhattan or
    Move a bike from Manhattan to Manhattan or
    Move a bike from Staten Island to Manhattan

    state: bikeshare State object
    '''

    if state.Bronx == 0:
        return
    state.Bronx -= 1
    state.Manhattan += 1
    
    if state.Brooklyn == 0:
        return
    state.Brooklyn -= 1
    state.Manhattan += 1

    if state.Queens == 0:
        return
    state.Queens -= 1
    state.Manhattan += 1

    if state.StatenIsland == 0:
        return
    state.StatenIsland -= 1
    state.Manhattan += 1
    
    
   
def bike_to_StatenIsland(state):
    '''
    Move a bike from Bronx to StatenIsland or
    Move a bike from Brooklyn to StatenIsland or
    Move a bike from Manhattan to StatenIsland or
    Move a bike from Staten Island to StatenIsland

    state: bikeshare State object
    '''

    if state.Bronx == 0:
        return
    state.Bronx -= 1
    state.StatenIsland += 1
    
    if state.Brooklyn == 0:
        return
    state.Brooklyn -= 1
    state.StatenIsland += 1

    if state.Queens == 0:
        return
    state.Queens -= 1
    state.StatenIsland += 1

    if state.Manhattan == 0:
        return
    state.Manhattan -= 1
    state.StatenIsland += 1
    
    
   
def run_simulation(state, p1, p2, p3, p4, p5, num_steps):
    '''
    Simulate the given number of time steps.
    
    p1: probability of a customer's arrival at Brooklyn
    p2: probability of a customer's arrival at Bronx
    p3: probability of a customer's arrival at Queens
    p4: probability of a bike coming to Manhattan
    p5: probability of a bike coming to Staten Island

    num_steps: number of time steps
    '''

    resultsBrooklyn = TimeSeries(state.Brooklyn)    
    resultsBronx = TimeSeries(state.Bronx)
    resultsQueens = TimeSeries(state.Queens) 
    resultsManhattan = TimeSeries(state.Manhattan) 
    resultsStatenIsland = TimeSeries(state.StatenIsland) 

    for i in range(num_steps):
        step(state, p1, p2, p3, p4, p5)
        resultsBrooklyn[i] = state.Brooklyn
        resultsBronx[i] = state.Bronx
        resultsQueens[i] = state.Queens
        resultsManhattan[i] = state.Manhattan
        resultsStatenIsland[i] = state.StatenIsland

    plt.plot(resultsBrooklyn, label='Brooklyn')
    plt.plot(resultsBronx, label='Bronx')
    plt.plot(resultsQueens, label='Queens')
    plt.plot(resultsManhattan, label='Manhattan')
    plt.plot(resultsStatenIsland, label='Staten Island')

    decorate(title='NYC Five-Borough Bikeshare Exploration',
             xlabel='Time(hrs)', 
             ylabel='Number of bikes')
    
    
   
#running the run_simulation(...) function with defined state, probabilities and time steps
run_simulation(bikeshare, 0.20, 0.20, 0.20, 0.20, 0.20, 100)
