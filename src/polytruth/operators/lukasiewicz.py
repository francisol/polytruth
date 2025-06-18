
from . import Operators
import numpy as np

class LukasiewiczOperators(Operators):
    """
    Lukasiewicz logic operators
    """
    def _init__(self):
        super().__init__("Lukasiewicz")
    
    
    @staticmethod
    def tnorm(**kwargs):
        """Lukasiewicz t-norm"""
        return lambda a,b:  np.maximum(0, a + b - 1)
    
    @staticmethod
    def tconorm(**kwargs):
        """Lukasiewicz t-conorm"""
        return lambda a,b:  np.minimum(1, a + b)
    

    
    @staticmethod
    def implication(**kwargs):
        """Lukasiewicz implication"""
        return lambda a,b:  np.minimum(1, 1 - a + b)