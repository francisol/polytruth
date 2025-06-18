

from polytruth.operators.godel import GodelOperators
from polytruth.types import Computable
from . import Operators


class CombinationOperators(Operators):
    """
    Abstract base class for logic operators.
    """
    def __init__(self,t_norm=GodelOperators.tnorm, 
                 t_conorm=GodelOperators.tconorm, 
                 negation=GodelOperators.negation, 
                 implication=GodelOperators.implication):
        self.name = "Combination"
        self.__t_norm = t_norm
        self.__t_conorm = t_conorm
        self.__negation = negation
        self.__implication = implication

    def logic_or(self, a:Computable,b:Computable) -> Computable:
        """a \\\\/ a"""
        return self.__t_conorm(a, b)
    def logic_and(self,a:Computable,b:Computable)->Computable:
        """a /\\\\ b"""
        return self.__t_norm(a, b)
    def logic_not(self,a:Computable)->Computable:
        """~ a"""
        return self.__negation(a)
    def logic_implies(self,a:Computable,b:Computable)->Computable:
        """a-> b """
        return self.__implication(a, b)