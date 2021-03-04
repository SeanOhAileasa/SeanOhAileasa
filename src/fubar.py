# repository ./E6985
def fFullScreen():
	"""Utilise full Jupyter notebook screen.

Input:
Process: (IPython.core.display.display; IPython.core.display.HTML)
Output:
"""
	from IPython.core.display import display,HTML
	display(HTML("<style>.container { width:100% !important; }</style>"))
# --- END ---
# repository ./E6985
def fDarkReader():
	"""Unable to determine plot ticks when using https://darkreader.org.

Input:
Process: (matplotlib.style.core.use)
Output:
"""
	from matplotlib.style.core import use
	use({"default"})
# --- END ---
# repository ./E6985
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
# repository ./E6985
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
