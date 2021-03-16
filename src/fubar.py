# repository ./OhAileasa
def fFullScreen():
	"""Utilise full Jupyter notebook screen.

Input:
Process: (IPython.core.display.display; IPython.core.display.HTML)
Output:
"""
	from IPython.core.display import display,HTML
	display(HTML("<style>.container { width:100% !important; }</style>"))
# --- END ---
# repository ./OhAileasa
def fDarkReader():
	"""Unable to determine plot ticks when using https://darkreader.org.

Input:
Process: (matplotlib.style.core.use)
Output:
"""
	from matplotlib.style.core import use
	use({"default"})
# --- END ---
# repository ./OhAileasa
def fMagic(nPar):
	"""None.

Input: Function/Method etc.
Process: (inspect.getmodule; type; __doc__) 
Output:	Function/Method etc additional information.
"""
	from inspect import getmodule
	print(getmodule(nPar))
	print(type(nPar))
	return nPar.__doc__
# --- END ---
# repository ./OhAileasa
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
# repository ./fubar-python
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
