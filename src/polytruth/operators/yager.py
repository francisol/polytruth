

import numpy as np

from polytruth.operators import Operators


class YagerOperators(Operators):
    """
    Yager logic operators
    """
    
    def __init__(self,tnorm_q=1,tconorm_q=1,negation_q=1,implication=None):
        super().__init__("Yager")
        self.implication = implication
        self.__tnorm = YagerOperators.tnorm(tnorm_q)
        self.__tconorm_q = YagerOperators.tconorm(tconorm_q)
        self.__negation_q = YagerOperators.negation(negation_q)
    def logic_not(self, a):
        """Negation operator"""
        if self.__negation_q is None:
            raise NotImplementedError("Negation operator not implemented")
        return self.__negation_q(a)
    def logic_and(self, a, b):
        """T-norm operator"""
        if self.__tnorm is None:
            raise NotImplementedError("T-norm operator not implemented")
        return self.__tnorm(a, b)
    def logic_or(self, a, b):
        """T-conorm operator"""
        if self.__tconorm_q is None:
            raise NotImplementedError("T-conorm operator not implemented")
        return self.__tconorm_q(a, b)
    def logic_implies(self, a, b):
        if self.implication is None:
            raise NotImplementedError("Implication operator not implemented")
        return self.implication(a, b)
    @staticmethod
    def tnorm(q):
        """Yager t-norm"""
        return  lambda a,b: np.maximum(1-np.sqrt(np.sqrt((1-a),q)+np.sqrt((1-b),q),1/q), 0)
    
    @staticmethod
    def tconorm(q):
        """Yager t-conorm"""
        return  lambda a,b: np.minimum(np.sqrt(np.sqrt((a),q)+np.sqrt((b),q),1/q), 1)

    
    @staticmethod
    def negation(p):
        """Yager negation"""
        return lambda a: (1 - a**p)**(1/p)
    
