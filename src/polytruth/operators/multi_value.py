from . import Operators
from ..types import Computable

class MultiValuedOperators(Operators):
    """
    MultiValued logic operators
    """
    def __init__(self):
        super().__init__("MultiValued")
    def logic_or(self, a:Computable, b:Computable)->Computable:
        return a+b-a*b
    def logic_and(self,a:Computable,b:Computable)->Computable:
        return a*b
    def logic_not(self,a:Computable)->Computable:
        return 1-a
    def logic_implies(self,a:Computable,b:Computable)->Computable:
        return self.logic_or(self.logic_not(a),b) #1-a+b-a*b
    def logic_equiv(self,a:Computable,b:Computable)->Computable:
        return self.logic_and(self.logic_implies(a,b),self.logic_implies(b,a))
