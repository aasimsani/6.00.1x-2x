def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    def seq(start, stop, step=1):
        n = int(round((stop - start)/float(step)))
        if n > 1:
            return([start + step*i for i in range(n)])
        else:
            return([])
    exposure = 0
    for n in seq(start,stop,step):
        y = f(n)
        exposure += (y*step)

    return exposure

print radiationExposure(0,3,0.1)
