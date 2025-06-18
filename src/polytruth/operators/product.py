

from . import Operators


class ProductOperators(Operators):
    """
    Product logic operators
    """
    
    def __init__(self):
        super().__init__("Product")
    
    @staticmethod
    def tnorm(**kwargs):
        """
        T-norm
        """
        return lambda a,b:  a * b
    @staticmethod
    def tconorm(**kwargs):
        """
        T-conorm
        """
        return lambda a,b:  a + b - a * b
    @staticmethod
    def implication(**kwargs):
        """
        Implication
        """
        return lambda a,b:  1 if a <= b else b