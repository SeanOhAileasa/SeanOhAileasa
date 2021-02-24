# a_S_tandard_L_ibrary-imports
import inspect
# define function fGetModuleType
def fGetModuleType(np):
    print(inspect.getmodule(np))
    print(type(np))