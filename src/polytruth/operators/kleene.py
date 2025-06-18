


import numpy as np

from . import Operators


class KleeneOperator(Operators):
    """
    Kleene logic operators
    """
    
    def __init__(self,t_norm=None, 
                 t_conorm=None, 
                 negation=None):
        super().__init__("Kleene")
        self.__t_norm = t_norm
        self.__t_conorm = t_conorm
        self.__negation = negation

    def logic_not(self, a):
        """!a"""
        if self.__negation is None:
            raise NotImplementedError("Negation operator not implemented")
        return self.__negation()(a)
    def logic_or(self, a,b):
        """tconorm"""
        if self.__t_conorm is None:
            raise NotImplementedError("T-Conorm operator not implemented")
        return self.__t_conorm()(a,b)
    def logic_and(self, a,b):
        """tnorm"""
        if self.__t_norm is None:
            raise NotImplementedError("T-Norm operator not implemented")
        return self.__t_norm()(a,b)
    

    
    @staticmethod
    def implication(**kwargs):
        """Kleene implication"""
        return lambda a,b: np.maximum(1 - a, b)