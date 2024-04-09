import myAST
import Symboltable
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, List, Tuple, Union

from myAST import (
    Start, StatementList, Declaration, Assignment, Type, CompoundTypes, CompoundTypeAccess,
    FunctionCall, ParameterList, OptionalParameterList, Condition, IfStatement, WhileStatement,
    Expression, BinaryOperator, Term, UnaryOperator, Factor, TryExcept, Print, Data, TrueFalse
)

@dataclass
class ArrayT:
    dims: int
    eltype: any
    size: any

    def __hash__(self):
        return hash((self.dims, self.eltype, self.size))

AnyT = 'any'
IntT = 'int'
FloatT = 'float'
StringT = 'string'
RangeT = 'range'
BoolT = 'bool'

aaa = defaultdict(
    lambda: defaultdict(
        lambda: defaultdict(
            lambda: AnyT
        ))
)


for op in '+-*/':
    aaa[op][IntT][IntT] = IntT
    aaa[op][IntT][FloatT] = FloatT
    aaa[op][FloatT][IntT] = FloatT
    aaa[op][FloatT][FloatT] = FloatT

for op in ['<', '<=', '>', '>=', '!=', '==']:
    aaa[op][IntT][IntT] = BoolT
    aaa[op][IntT][FloatT] = BoolT
    aaa[op][FloatT][FloatT] = BoolT
    aaa[op][FloatT][FloatT] = BoolT

for op in ['==', '!=']:
    aaa[op][StringT][StringT] = BoolT

class myASTVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, myAST.Node):
                            self.visit(item)
                elif isinstance(child, myAST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    # def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)

class Symbol(object):
    def __init__(self, name, type=None):
        self.name = name
        self.type = type
        self.category = category

class BuiltinTypeSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<{class_name}(name='{name}')>".format(
            class_name=self.__class__.__name__,
            name=self.name,
        )

class VarSymbol():
            def __init__(self, name, type):
                super().__init__(name, type)

            def __str__(self):
                return "<{class_name}(name='{name}', type='{type}')>".format(
                    class_name=self.__class__.__name__,
                    name=self.name,
                    type=self.type,
                )

            __repr__ = __str__

class Type_checker(myAST):

        # Define visit methods for each type of node in your AST
        def __init__(self):
            self.symtab = Symboltable()

        def visit_start(self, start: 'Start'):
            self.visit_statement_list(start.statement_list)

        def visit_statement_list(self, statement_list: List[Any]):
            for statement in statement_list:
                self.visit_statement(statement)

        def visit_Declaration(self, node):
            type_name = node.type_node.value
            type_symbol = self.symtab.lookup(type_name)

            # We have all the information we need to create a variable symbol.
            # Create the symbol and insert it into the symbol table.
            var_name = node.var_node.value
            var_symbol = VarSymbol(var_name, type_symbol)

            if self.symtab.lookup(var_name) is not None:
                raise Exception(
                    "Error: Duplicate identifier '%s' found" % var_name
                )
            
            self.symtab.insert(var_symbol)
            
        def visit_Assignment(self, node):
            var_name = node.value
            var_symbol = self.symtab.lookup(var_name)
            if var_symbol is None:
                raise Exception(
                    "Error: Symbol(identifier) not found '%s'" % var_name
                )
    # Define visit methods for other types of nodes...

'''Instantiate the visitor and use it to traverse the AST
visitor = myAST()
visitor.visit(Start)'''
