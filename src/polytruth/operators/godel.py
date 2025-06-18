from ..types import Computable
from . import Operators
import numpy as np


class GodelOperators(Operators):
    """Gödel """
    
    def __init__(self):
        super().__init__("Gödel")
    
    @staticmethod
    def tnorm(**kwargs):
        """Gödel t-norm"""
        return lambda a,b:  np.minimum(a, b)
    
    @staticmethod
    def tconorm(**kwargs):
        """Gödel t-conorm"""
        return lambda a,b:  np.maximum(a, b)
    
    @staticmethod
    def negation(**kwargs):
        """Gödel """
        # 在 Gödel 逻辑中，否定定义为：
        # ¬a = 1 if a=0 else 0
        # 但更通用的实现是使用标准否定
        return lambda a,b:  1 - a
    
    @staticmethod
    def implication(**kwargs):
        """Gödel implication"""
        # a → b = 1 if a ≤ b else b
        return lambda a,b:  1 if a <= b else b
    
    # @staticmethod
    # def quantifier_exists(values):
    #     """存在量词 (上确界)"""
    #     return max(values)
    
    # @staticmethod
    # def quantifier_forall(values):
    #     """全称量词 (下确界)"""
    #     return min(values)