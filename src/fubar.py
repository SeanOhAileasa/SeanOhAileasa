# repository ./SeanOhAileasa
def fFile(nParPath):
    """Start a file with its associated application.

Input: nParPath
Process: (os.path.realpath; os.startfile)
Output: file opened with associated application
"""
    from os import path,startfile
    return startfile(path.realpath(nParPath))
# --- END ---
# repository ./SeanOhAileasa
def fFullScreen():
    """Utilise full Jupyter notebook screen.

Input:
Process: (IPython.core.display.display; IPython.core.display.HTML)
Output:
"""
    from IPython.core.display import display,HTML
    display(HTML("<style>.container { width:100% !important; }</style>"))
# --- END ---
# repository ./SeanOhAileasa
def fDarkReader():
    """Unable to determine plot ticks when using https://darkreader.org.

Input:
Process: (matplotlib.style.core.use)
Output:
"""
    from matplotlib.style.core import use
    use({"default"})
# --- END ---
# repository ./SeanOhAileasa
def fMagic(nPar):
    """None.

Input: function/method etc.
Process: (inspect.getmodule; type; __doc__) 
Output:	function/method etc additional information
"""
    from inspect import getmodule
    print(getmodule(nPar))
    print(type(nPar))
    return nPar.__doc__
# --- END ---
# repository ./SeanOhAileasa
if __name__=="__main__":
    pass
else:
    # repository *.ipynb
    fFullScreen()
# --- END ---
# repository ./fubar-python
def fIsObject(nParSomething):
    """Everything in python is an object.
    
Input: nParSomething
Process: (isinstance)
Output: boolean True or False
"""
    return isinstance(nParSomething,object)
# --- END ---
# repository ./fubar-python
def fImmutableMutable(nParObject):
    """Immutable objects (int; float; bool; complex; frozenset; str; tuple)
    cannot be changed whereas mutable objects (list; set; dict) can be changed.

Input: nParObject
Process: (id)
Output: i) object identity (memory address); ii) object itself  
"""
    print("<id> : {}".format(id(nParObject)))
    return nParObject 
# --- END ---
# repository ./cta-recursion
def fCount(nParIndex):
    """Recursive process.

Input: nParIndex
Process: print Input; if Input<2 then call fCount passing Input+1
Output: sequence 0, 1, 2
"""
    print(nParIndex)
    if nParIndex<2:
        fCount(nParIndex+1)
# -- END ---
# repository ./cta-recursion
def fInfinite(nParInteger):
    """Recursive process without a base case.

Input: nParInteger
Process: Input-1
Output: never stops making recursive calls regardless of Input
"""
    fInfinite(nParInteger-1)
# -- END ---
# repository ./cta-recursion
def fCircular(nParInteger):
    """Recursive process not making progress toward a base case.

Input: nParInteger
Process: if Input==1 then call fCircular passing Input+1;
    otherwise make call to fCircular passing Input-1
Output: keeps going back and forth when Input==1
"""
    if nParInteger==1:
        fCircular(nParInteger+1)
    fCircular(nParInteger-1)
# -- END ---
# repository ./cta-sorting
def fAddBarLabels(nParCollection):
    """Add text (s) to the axes at coordinates x and y.

Input: nParCollection
Process: (len; range; matplotlib.pyplot.text) 
Output:
"""
    from matplotlib.pyplot import text
    for nIndex in range(len(nParCollection)):
        text(x=nIndex,y=nParCollection[nIndex],
             s=nParCollection[nIndex],
             ha="center",va="bottom",fontsize=12)
    return nParCollection
# --- END ---
# repository ./cta-sorting
def fAddPlot(nParCollection,nParColor):
    """Make a bar plot at coordinate x with dimension height.
    Bars coloured based on some criteria.

Input: nParCollection; nParColor
Process: (matplotlib.pyplot.box,yticks,bar; len; range)
Output:
"""
    from matplotlib.pyplot import box,yticks,bar
    box(False); # remove plot box
    yticks([]) # remove y-axis ticks
    bar(x=range(len(nParCollection)), # x-axis collection indices
        height=nParCollection, # y-axis actual collection
        color=nParColor, # bar color 
        tick_label=range(len(nParCollection))) # ticks represent indices
# --- END ---
# repository ./cta-searching
def fLinearSearch(nParCollection,nParTarget):
    """Linear search implementation.
    
Input: nParCollection; nParTarget
Process: iterate element by element through Input=nParCollection comparing Input=nParTarget
Output: index of the target element or -1
"""
    for nIndex in range(len(nParCollection)):
        if nParCollection[nIndex]==nParTarget:
            return nIndex
    return -1
# --- END ---
# repository ./cta-searching
def fBinarySearchIterative(nParCollection,nParTarget):
    """Binary search iterative implementation.
    
Input: nParCollection; nParTarget
Process: chopping Input=nParCollection in half comparing element to Input=nParTarget 
Output: index of the target element or -1
"""
    nLeft,nRight=0,len(nParCollection)-1
    while(nRight>=nLeft):
        nMidpoint=(nLeft+nRight)//2
        if (nParCollection[nMidpoint]==nParTarget):
            return nMidpoint
        if (nParCollection[nMidpoint]<nParTarget):
            nLeft=nMidpoint+1 # chopping right partition
        if (nParCollection[nMidpoint]>nParTarget):
            nRight=nMidpoint-1 # chopping left partition
    return -1
# --- END ---
# repository ./fda-monty-hall-problem
def fSimulateMontyHall(nParStay=True):
    """ Simulate the Win a Car game (known as the Monty Hall problem).
    Query is if the contestant wishes to stay with the nPick or move to nNotOpenPick.
    See how ofen the contestant wins.
    
Input: nParStay (default True)
Process: (random.choice)
    1. pick a door to put the car behind (nCar);
    2. have the contestant pick a door (nPick);
    3. have the show host open one of the other doors to reveal a goat (nShow);
    4. ask the contestant if they want to switch (nParStay default to True)
Output: return list of two items (nPick and nNotOpenPick) using True or False as an index
"""    
    from random import choice
    nDoors=["red","green","blue"] # probability of 1/3
    nCar=choice(nDoors) # car pick door
    nPick=choice(nDoors) # contestant pick door
    nShow=choice([nEachDoor for nEachDoor in nDoors if nEachDoor!=nCar and nEachDoor!=nPick]) # door with goat
    nNotOpenPick=[nEachDoor for nEachDoor in nDoors if nEachDoor!=nPick and nEachDoor!=nShow][0] # remaining unopened door
    return (nCar==[nPick,nNotOpenPick][not nParStay]) # picked or unopened
# -- END ---
