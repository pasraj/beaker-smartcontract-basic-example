from smartcontract import Calculator
import json

calc = Calculator()
print(calc.approval_program)
print(calc.clear_program)
print(json.dumps(calc.contract.dictify()))