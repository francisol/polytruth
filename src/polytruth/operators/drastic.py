

import numpy as np

from . import Operators


class DrasticOperators(Operators):
    """
    Drastic logic operators
    """
    
    def __init__(self):
        super().__init__("Drastic")
    
    @staticmethod
    def tnorm(**kwargs):
        """Drastic t-norm"""
        return lambda a,b: np.minimum(a, b) if np.equal(a,1) or np.equal(b,1) else 0
    
    @staticmethod
    def tconorm(**kwargs):
        """Drastic t-conorm"""
        return lambda a,b: np.maximum(a, b) if np.equal(a,0) and np.equal(b,0) else 1
    

    
    @staticmethod
    def implication(**kwargs):
        """Drastic implication"""
        return lambda a,b: 1 if a <= b else 0