from typing import Any, List, Tuple, Union
from dataclasses import dataclass

from myAST import (
    Program, StatementList, Declaration, Assignment, Type, CompoundTypes, CompoundTypeAccess,
    FunctionCall, FunctionDefinition, ParameterList, OptionalParameterList, Condition, IfStatement, WhileStatement,
    Expression, BinaryOperator, Term, UnaryOperator, Factor, TryExcept, Print, Data, TrueFalse
)

def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator

class TreePrinter:
    @addToClass(Start)
    def printTree(self, indent=0):
        for stmt in self.statement_list:
            stmt.printTree(indent)

    @addToClass(StatementList)
    def printTree(self, indent=0):
        for _, statement in self.statements:
            statement.printTree(indent)

    @addToClass(Declaration)
    def printTree(self, indent=0):
        print("|  " * indent + f"{self.type_}")
        self.assignment.printTree(indent + 1)

    @addToClass(Assignment)
    def printTree(self, indent=0):
        print("|  " * indent + f"Assignment: {self.identifier} {self.assignment_operator}")
        self.value.printTree(indent + 1)

    @addToClass(Type)
    def printTree(self, indent=0):
        print("|  " * indent + f"Type: {self.type_}")

    @addToClass(CompoundTypes)
    def printTree(self, indent=0):
        print("|  " * indent + f"Compound Type: {self.compound_type} {self.identifier} {self.assignment_operator}")
        for data in self.data:
            data.printTree(indent + 1)

    @addToClass(CompoundTypeAccess)
    def printTree(self, indent=0):
        print("|  " * indent + f"Compound Type Access: {self.identifier}")
        if isinstance(self.compound_type_access, tuple):
            name, value = self.compound_type_access
            print("|  " * (indent + 1) + f"{name}:")
            value.printTree(indent + 2)
        else:
            print("|  " * (indent + 1) + f"{self.compound_type_access}")

    @addToClass(FunctionDefinition)
    def printTree(self, indent=0):
        print("|  " * indent + f"Function Definition: {self.identifier}")
        if self.parameter_list:
            self.parameter_list.printTree(indent + 1)
        for stmt in self.statement_list:
            stmt.printTree(indent + 1)
        print("|  " * indent + f"Return: {self.return_data}")

    @addToClass(FunctionCall)
    def printTree(self, indent=0):
        print("|  " * indent + f"Function Call: {self.identifier}")
        self.expression.printTree(indent + 1)

    @addToClass(ParameterList)
    def printTree(self, indent=0):
        print("|  " * indent + "Parameters:")
        for param in self.parameters:
            print("|  " * (indent + 1) + f"{param[0]}: {param[1]}")

    @addToClass(OptionalParameterList)
    def printTree(self, indent=0):
        if self.parameters:
            print("|  " * indent + "Optional Parameters:")
            for param in self.parameters:
                print("|  " * (indent + 1) + f"{param[0]}: {param[1]}")

    @addToClass(Condition)
    def printTree(self, indent=0):
        print("|  " * indent + f"Condition: {self.left} {self.comparison_operator} {self.right}")

    @addToClass(IfStatement)
    def printTree(self, indent=0):
        print("|  " * indent + "IF")
        self.condition.printTree(indent + 1)
        for stmt in self.if_statement:
            stmt.printTree(indent + 1)
        for elif_condition, elif_statement in self.elif_statement:
            print("|  " * indent + "ELIF")
            elif_condition.printTree(indent + 1)
            for stmt in elif_statement:
                stmt.printTree(indent + 1)
        if self.else_statement:
            print("|  " * indent + "ELSE")
            for stmt in self.else_statement:
                stmt.printTree(indent + 1)

    @addToClass(WhileStatement)
    def printTree(self, indent=0):
        print("|  " * indent + "WHILE")
        self.condition.printTree(indent + 1)
        for stmt in self.statement_list:
            stmt.printTree(indent + 1)

    # Define similar methods for other classes...

