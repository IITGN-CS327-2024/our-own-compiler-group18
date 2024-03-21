from ply import lex
import sys
from pprint import pprint

# Define tokens
tokens = [
    'ID',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'COMMA',
    'LSPAREN',
    'RSPAREN',
    'DOT',
    'ASSIGN',
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'MUL',
    'DIV',
    'REM',
    'EQEQ',
    'NOTEQ',
    'GT',
    'LT',
    'SUBSTR',
    'GTEQ',
    'LTEQ',
    'STRING',
    'VAR',
    'INT',
    'BOOL',
    'BEGIN',
    'END',
    'IF',
    'ELIF',
    'ELSE',
    'WHILE',
    'ZOUT',
    'STR',
    'FUNC',
    'RETURN',
    'CON',
    'TUPLE',
    'LIST',
    'SIZE',
    'DELETE',
    'FRONT',
    'REAR',
    'TRY',
    'EXCEPT',
    'TRUE',
    'FALSE',
    'ADD',
]

# Define keywords and reserved words
keywords = {
    'var': 'VAR',
    'int': 'INT',
    'bool': 'BOOL',
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'while': 'WHILE',
    'zout': 'ZOUT',
    'str': 'STR',
    'func': 'FUNC',
    'return': 'RETURN',
    'con': 'CON',
    'tuple': 'TUPLE',
    'list': 'LIST',
    'substr':'SUBSTR',
    'size': 'SIZE',
    'delete': 'DELETE',
    'front': 'FRONT',
    'add'  : 'ADD',
    'rear': 'REAR',
    'try': 'TRY',
    'except': 'EXCEPT',
    'true': 'TRUE',
    'false': 'FALSE'
}

# Tokens with associated regular expressions
t_ignore = ' \t'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_LSPAREN = r'\['
t_RSPAREN = r'\]'
t_DOT = r'\.'
t_STRING = r'\".*?\"'

t_ASSIGN = r'='
t_PLUS = r'\+'
t_PLUSPLUS = r'\+\+'
t_MINUS = r'-'
t_MINUSMINUS = r'--'
t_MUL = r'\*'
t_DIV = r'/'
t_REM = r'%'
t_EQEQ = r'=='
t_NOTEQ = r'!='
t_GT = r'>'
t_LT = r'<'
t_GTEQ = r'>='
t_LTEQ = r'<='


def t_NUMBER(t):
  r'-?\d+'
  t.value = int(t.value)
  return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value.lower(), 'ID')
    return t

def t_COMMENT(t):
    r'@.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

'''
text = open("test_cases/test4.zeva","r").read()
lexer.input(text)
for token in lexer:
    print(token)'''


precedence = (
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV' ,'REM'),
    ('nonassoc','EQEQ','NOTEQ','GT','LT','GTEQ','LTEQ'),
    ('right','PLUSPLUS','MINUSMINUS')
    )

#Grammar rules
def p_start(p):
    'start : statement_list'
    # Handle the start symbol here
    p[0] = ('start',p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement SEMICOLON
                      | empty'''
    # Handle the list of statements here
    if len(p) == 4:
      p[0] = (p[1] ,[p[2]],p[3])
    else:
      p[0] = None

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | if_stmnt
                 | while_stmt
                 | function_call
                 | expression
                 | compound_types
                 | compound_type_access
                 | try_except
                 | print'''

    p[0] = p[1]

def p_declaration(p):
    '''declaration : VAR type assignment'''
    p[0] = ('declaration',p[1],p[2], p[3])


def p_assignment(p):
    '''assignment :  ID ASSIGN L'''
    p[0] = ('assignment', p[1],p[2], p[3])

def p_L(p):
  '''L : statement
       | ID LPAREN data RPAREN'''
  if len(p) == 5:
    p[0] =  (p[1], p[3])
  else:
    p[0] = p[1]
  
def p_type(p):
    '''type : INT
            | BOOL
            | STR'''

    p[0] = p[1]

def p_compound_types(p):
    '''compound_types : A ID ASSIGN LPAREN data RPAREN'''

    p[0] = ('compound_types', p[1], p[2],p[3],p[4], p[5],p[6])

def p_A(p):
    '''A : TUPLE
         | LIST'''
    p[0] = p[1]

def p_data(p):
    '''data : expression data
            | COMMA data
            | empty'''
    if len(p) == 3:
      p[0] = [p[1]] + p[2]
    else:
      p[0] = []
def p_compound_type_access(p):
    '''compound_type_access : ID DOT F 
                            | ID LSPAREN expression RSPAREN'''
    if p[2] == '.':
      p[0] = ('compound_type_access_dot', p[1],p[2], p[3])
    else:
      p[0] = ('compound_type_access_index', p[1], p[3])



def p_F(p):
    '''F : CON LPAREN factor RPAREN
         | FRONT
         | ADD LPAREN factor RPAREN
         | REAR
         | SIZE
         | DELETE
         | SUBSTR LPAREN factor COMMA factor RPAREN
         | empty'''
    if len(p) == 5:
      p[0] = ('F_con_add', p[1],p[2],p[3],p[4])
    elif len(p) == 3:
      p[0] = ('F_front' if p[1] == 'FRONT' else 'F_rear')
    elif len(p) == 2:
      p[0] = ('F_' + p[1].lower())
    else:
      p[0] = ('F_substr', p[3], p[5])

def p_if_stmnt(p):
    '''if_stmnt : IF LPAREN condition RPAREN  BEGIN  statement_list END T'''
    p[0] = ('if_statement',p[1],p[2], p[3],p[4],p[5],p[6],p[7],p[8])

def p_T(p):
    '''T :  ELIF LPAREN condition RPAREN BEGIN  statement_list END K
         |  empty'''
    if len(p) == 9:
      p[0] = ('T_elif', p[1],p[2], p[3],p[4],p[5],p[6],p[7],p[8])
    else:
      p[0] = None

def p_K(p):
    '''K : ELSE BEGIN statement_list END 
         | empty'''
    if len(p) == 5:
      p[0] = ('K_else', p[1],p[2],p[3],p[4])
    else:
      p[0] = None

def p_while_stmt(p):
    '''while_stmt : WHILE LPAREN condition RPAREN BEGIN statement_list END'''
    p[0] = ('while_statement',p[1], p[2],p[3],p[4],p[5],p[6],p[7])

def p_function_call(p):
    '''function_call : FUNC ID LPAREN parameter_list RPAREN BEGIN statement_list  RETURN data SEMICOLON END'''
    p[0] = ('function_call', p[1],p[2],p[3], p[4],p[5],p[6], p[7],p[8], p[9],p[10],p[11])

def p_parameter_list(p):
  '''parameter_list : type ID optional_parameter_list
                    | empty'''
  if len(p) == 4:
    p[0] = [(p[1], p[2])] + p[3]
  else:
    p[0] = None

def p_optional_parameter_list(p):
  '''optional_parameter_list : COMMA type ID optional_parameter_list
                              | empty'''
  if len(p) == 5:
    p[0] = [(p[2], p[3])] + p[4]
  else:
    p[0] = []

def p_condition(p):
    '''condition : expression  comparison_operator  expression'''
    p[0] = (p[1],p[2],  p[3])

def p_comparison_operator(p):
    '''comparison_operator : EQEQ 
                           | NOTEQ 
                           | LT 
                           | GT 
                           | LTEQ 
                           | GTEQ '''
    p[0] = p[1]

def p_expression(p):
    '''expression : expression binary_operator expression
                  | expression unary_operator
                  | factor'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('expression_unop',p[1], p[2])
    else:
        p[0] = ('expression_binop', p[1], p[2], p[3])


def p_binary_operator(p):
  '''binary_operator  : MINUS 
                      | MUL 
                      | PLUS
                      | DIV 
                      | REM '''
  p[0] = p[1]

def p_unary_operator(p):
    ''' unary_operator : PLUSPLUS 
                       | MINUSMINUS '''
    p[0] = p[1]

def p_factor(p):
    ''' factor :  ID 
               | NUMBER 
               | STRING
               | TRUE
               | FALSE 
               | LPAREN expression RPAREN'''
    if len(p) == 4:
      p[0] = ('factor_expression', p[2])
    else:
      p[0] = p[1]

def p_try_except(p):
    '''try_except : BEGIN TRY statement_list EXCEPT statement_list END'''
    p[0] = ('try_except',p[1],p[2], p[3],p[4], p[5],p[6])

def p_print(p):
    '''print : ZOUT LPAREN y RPAREN'''
    p[0] = ('print', p[1],p[2], p[3],p[4])

def p_y(p):
    '''y : expression
         | compound_type_access'''
    p[0] = p[1]

def p_empty(p):
    '''empty : '''
    p[0] = None

def find_column(input, p):
    line_start = input.rfind('\n', 0, p.lexpos) + 1
    return (p.lexpos - line_start) + 1

def p_error(p):
    if p is not None:
        column = find_column(text, p)        
        print("Found unexpected character '%s' at line '%s' and column '%s'" % (p.value, p.lineno, column))
    else:
        print("Unexpected end of input!Empty file or syntax error at EOF!")

import ply.yacc as yacc

parser = yacc.yacc()

try:
        text = open("test_cases/test14.zeva","r").read()
        p = parser.parse(text)
        pprint(p)
  

except EOFError:
    print("File could not be opened!")