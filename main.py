from polytruth.core import And, Implies, Not, Or, Var
from polytruth.operator import MultiValuedOperators
from polytruth import LogicSystem
import numpy as np

from polytruth.parser import parse_file


def exmaple_for_multvalued():
    import numpy as np
    from polytruth import LogicSystem, MultiValuedOperators,And, Not

    # Initialize logic system with poly-valued operators
    logic_system = LogicSystem(MultiValuedOperators())

    # Create variables with multi-dimensional truth values
    a = logic_system.new_variable("a", np.array([0.3, 0.7]))  
    b = logic_system.new_variable("b", np.array([0.5, 0.5]))  

    # Add logical rules
    rule1 = And(And(a, b), Not(b))
    logic_system.add_rule("rule1", rule1)
    logic_system.add_rule("rule2", ~a & (b | a))

    # Set variable values
    logic_system.set_variable_values({
        "b": np.array([0.5, 0.9]),  
        "b": 0.8  
    })

    # Compute all rules
    print("All rule computations:")
    print(logic_system.compute())

    # Compute specific rule
    print("\nSingle rule computation:")
    print(logic_system.compute("rule1"))

    # View all variables
    print("\nSystem variables:")
    print(logic_system.variables)
    ## View all rules
    print("\nSystem rules:")
    print(logic_system.rules)

def exmaple_for_file():
    logic_system = LogicSystem(MultiValuedOperators())
    parse_file("data.logic",logic_system)
    print(logic_system.rules)

def main():
    exmaple_for_multvalued()
    exmaple_for_file()


if __name__ == "__main__":
    main()
