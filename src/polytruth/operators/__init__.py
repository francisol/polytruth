from abc import ABC, abstractmethod

from polytruth.types import Computable


class Operators(ABC):
    """
    Abstract base class for logic operators.
    """
    def __init__(self, name: str):
        self.name = name


    def logic_or(self, a:Computable,b:Computable) -> Computable:
        """a \\\\/ a"""
        return self.tconorm()(a, b)
    def logic_and(self,a:Computable,b:Computable)->Computable:
        """a /\\\\ b"""
        return self.tnorm()(a, b)
    def logic_not(self,a:Computable)->Computable:
        """~ a"""
        return self.negation()(a)
    def logic_implies(self,a:Computable,b:Computable)->Computable:
        """a-> b """
        return self.implication()(a, b)

    @staticmethod
    @abstractmethod
    def tnorm(**kwargs):
        pass
    
    @staticmethod
    @abstractmethod
    def tconorm(**kwargs):
        pass
    
    @staticmethod
    def negation(**kwargs):
        return lambda a: 1-a
    
    @staticmethod
    @abstractmethod
    def implication(**kwargs):
        pass
    def __repr__(self):
        return f"Operator({self.name})"

