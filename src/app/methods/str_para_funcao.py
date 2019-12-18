# imports do sympy
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy import Symbol

# vars de controle e transformacao para o sympy
x = Symbol('x')
transformations = (standard_transformations + (implicit_multiplication_application,))

# classe de expressao matematica generica
class expressao_generica:
    def __init__(self, str_expression):
        self.expression = parse_expr( str_expression, transformations = transformations)
    
    def f(self, val):
        '''
            Metodo que retorna o valor de f(val)
        '''
        return self.expression.evalf(subs={x:val})
    
    