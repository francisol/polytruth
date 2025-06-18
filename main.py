from polytruth.operators.godel import GodelOperators
from polytruth.core import And, Not, Or, Var
from polytruth.operators.multi_value import MultiValuedOperators
from polytruth import LogicSystem
import numpy as np

from polytruth.parser import parse_file

def main():
    logic_system= LogicSystem(GodelOperators())
    parse_file("data.logic",logic_system)
    print(logic_system.rules)

    a=logic_system.new_variable("a",np.array([0.3,0.7]))
    b=logic_system.new_variable("b",np.array([0.5,0.5]))
    rule= And(And(a,b),Not(b))
    logic_system.add_rule("apple",rule)
    logic_system.add_rule("banana",a|b)
    logic_system.set_variable_values({"is(a,c)":np.array([0.5,0.9]),"b":0.8})
    print(logic_system.compute())
    print(logic_system.compute("apple"))
    print(logic_system.variables)


if __name__ == "__main__":
    main()
