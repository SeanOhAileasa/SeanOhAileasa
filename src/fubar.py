def fFullScreen():
	"""Utilise full Jupyter notebook screen.
"""
	from IPython.core.display import display,HTML
	display(HTML("<style>.container { width:100% !important; }</style>"))

def fDarkReader():
	"""Unable to determine plot ticks when using https://darkreader.org [1][2].

[1] CptanPanic, "How to handle labels when using dark theme with jupyterlabs?," [github](https://web.archive.org/web/20201027100553/https://github.com/matplotlib/ipympl/issues/25), October 2017.
[2] Anaconda (use), "matplotlib.style.core," Docstring, June 2020.
"""
	from matplotlib.style.core import use
	use({"default"})

def fMagic(nPar):
	"""None.

Input: Function/Method etc.
Process: Using built-in: inspect.getmodule; type; __doc__ 
Output:	Function/Method etc additional information.
"""
	from inspect import getmodule
	print(getmodule(nPar))
	print(type(nPar))
	return nPar.__doc__

if __name__=="__main__":
	pass
else:
	fFullScreen()
