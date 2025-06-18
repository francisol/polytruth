import warnings
from .product import ProductOperators
from . import Operators
from ..types import Computable

class MultiValuedOperators(ProductOperators):
    """MultiValuedOperators is deprecated. Use ProductOperators instead."""
    
    def __init__(self):
        warnings.warn("`MultiValuedOperators` is deprecated. Use `ProductOperators` instead.", DeprecationWarning)
        super().__init__()

        
  