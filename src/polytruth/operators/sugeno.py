

from . import Operators


class SugenoOperators(Operators):
    """
    Sugeno logic operators
    """
    
    def __init__(self,
                 negation_q=1,
                 t_norm=None, 
                 t_conorm=None, 
                 implication=None):
        super().__init__("Sugeno")
        self.__negation = SugenoOperators.negation(negation_q) 
        self.__t_norm = t_norm
        self.__t_conorm = t_conorm
        self.__implication = implication
    
    def logic_and(self, a, b):
        if self.__t_norm:
            return self.__t_norm(a, b)
        else:
            raise NotImplementedError("T-norm not implemented")    
    def logic_or(self, a, b):
        if self.__t_conorm:
            return self.__t_conorm(a, b)
        else:
            raise NotImplementedError("T-conorm not implemented")
    def logic_implies(self, a, b):
        if self.__implication:
            return self.__implication(a, b)
        else:
            raise NotImplementedError("Implication not implemented")
    
    def logic_not(self, a):
        if self.__negation:
            return self.__negation(a)
        else:
            raise NotImplementedError("Negation not implemented")
    
    @staticmethod
    def negation(q):
        """Sugeno negation"""
        return lambda a: (1 - a) / (1 + q * a)