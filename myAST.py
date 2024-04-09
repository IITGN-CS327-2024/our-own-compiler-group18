from dataclasses import dataclass
from typing import Any, List, Tuple, Union

@dataclass
class Start:
    statement_list: List[Any]

@dataclass
class StatementList:
    statements: List[Tuple[str, Any]]

@dataclass
class Declaration:
    type_: str
    assignment: Any

@dataclass
class Assignment:
    identifier: str
    assignment_operator: str
    value: Any

@dataclass
class Type:
    type_: str

@dataclass
class CompoundTypes:
    compound_type: str
    identifier: str
    assignment_operator: str
    data: Tuple[Any]

@dataclass
class CompoundTypeAccess:
    identifier: str
    compound_type_access: Union[str, Tuple[str, Any]]

@dataclass
class FunctionDefinition:
    identifier: str
    parameter_list: Union[Tuple[Tuple[str, str], Any], None]
    statement_list: List[Any]
    return_data: Any

@dataclass
class FunctionCall:
    identifier: str
    expression: Union[Tuple[Any, str, Any], Any]

@dataclass
class ParameterList:
    parameters: Tuple[Tuple[str, str], Any]

@dataclass
class OptionalParameterList:
    parameters: Union[Tuple[List[Tuple[str, Tuple[str, str]]], Any], None]

@dataclass
class Condition:
    left: Any
    comparison_operator: str
    right: Any

@dataclass
class IfStatement:
    condition: Any
    if_statement: List[Any]
    elif_statement: List[Tuple[Any, List[Any]]]
    else_statement: Union[List[Any]] 

@dataclass
class WhileStatement:
    condition: Any
    statement_list: List[Any]

@dataclass
class Pexpression:
    value: List[Any]

@dataclass
class Expression:
    expression: Union[Tuple[Any, str, Any], Any]

@dataclass
class BinaryOperator:
    operator: str

@dataclass
class Term:
    term: Union[Any, Tuple[Any, str]]

@dataclass
class UnaryOperator:
    operator: str

@dataclass
class Factor:
    factor: Union[str, int, Tuple[str, Any]]

@dataclass
class TryExcept:
    try_block: List[Any]
    except_block: List[Any]

@dataclass
class Print:
    print_statement: str
    value: Any

@dataclass
class Data:
    expressions: Tuple[Any]

@dataclass
class TrueFalse:
    value: bool