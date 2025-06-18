
from . import Operators
import numpy as np

class NilpotentOperators(Operators):
    def __init__(self):
        self.name = "Nilpotent"
    
    @staticmethod
    def tnorm(**kwargs):
        """
        Nilpotent t-norm
        """
        return lambda a,b:  np.where(a + b <= 1, 0, np.minimum(a, b))
    @staticmethod
    def tconorm(**kwargs):
        """
        Nilpotent t-conorm
        """
        return lambda a,b:  np.where(a + b >= 1, 0, np.maximum(a, b))
    
    @staticmethod
    def implication(**kwargs):
        """
        Nilpotent negation
        """
        return lambda a,b:  np.where((1-a)+b, 1, np.max(1-a,b))