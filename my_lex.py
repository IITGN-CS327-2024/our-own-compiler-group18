from ply import lex
import sys

# Define tokens
tokens = [
    'EOF',
    'ID',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'SEMI',
    'COMMA',
    'LSPAREN',
    'RSPAREN',
    'DOT',
    'ASSIGN',
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MUL',
    'DIV',
    'REM',
    'EQEQ',
    'NOTEQ',
    'GT',
    'LT',
    'GTEQ',
    'LTEQ',
    'AND',
    'OR',
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
    'FOR',
    'CON',
    'TUPLE',
    'LIST',
    'ADD',
    'SIZE',
    'DELETE',
    'FRONT',
    'REAR',
    'TRY',
    'EXCEPT',
    'TRUE',
    'FALSE'
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
    'for': 'FOR',
    'con': 'CON',
    'tuple': 'TUPLE',
    'list': 'LIST',
    'add': 'ADD',
    'size': 'SIZE',
    'delete': 'DELETE',
    'front': 'FRONT',
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
t_SEMI = r';'
t_COMMA = r','
t_LSPAREN = r'\['
t_RSPAREN = r'\]'
t_DOT = r'\.'
#t_QUOTATION = r'\"'
t_STRING = r'\".*?\"'


t_ASSIGN = r'='
t_PLUS = r'\+'
t_PLUSPLUS = r'\+\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_REM = r'%'
t_EQEQ = r'=='
t_NOTEQ = r'!='
t_GT = r'>'
t_LT = r'<'
t_GTEQ = r'>='
t_LTEQ = r'<='
t_AND = r'&&'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.lower() == 'true' or t.value.lower() == 'false':
        t.type = 'BOOL'
    else:
        t.type = keywords.get(t.value.lower(), 'ID')
    return t

def t_COMMENT(t):
    r'@.*|\@*.*\*@'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

precedence = (
	('left','AND','OR'),
	('nonassoc','EQEQ','NOTEQ','GT','LT','GTEQ','LTEQ'),
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV','MOD'),
    #('right','UMINUS'),
    )

#Grammar rules
def p_start(p):
    'start : statement_list'
    # Handle the start symbol here
    pass

def p_statement_list(p):
    '''statement_list : statement SEMICOLON statement_list
                      | empty'''
    # Handle the list of statements here
    pass

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | if_stmnt
                 | while_stmt
                 | function_call
                 | compound_types
                 | compound_type_access
                 | try_except'''

    pass

def p_declaration(p):
    '''declaration : VAR type ID ASSIGN expression '''
    pass

def p_assignment(p):
    '''assignment :  ID ASSIGN expression'''
    pass

def p_type(p):
    '''type : INT
            | BOOL
            | STR'''

    pass

def p_compound_types(p):
    '''compound_types : A ID ASSIGN N'''
    pass

def p_A(p):
    '''A : TUPLE
         | LIST'''
    pass

def p_N(p):
    '''N : LPAREN data RPAREN 
         | LSPAREN data RSPAREN'''
    pass


def p_data(p):
    '''data : factor I'''
    pass

def p_I(p):
    '''I : COMMA data 
        | empty'''
    pass

def p_compounnd_type_access(p):
    '''compound_type_access : Z F 
                            | ID LSPAREN expression RSPAREN'''
    pass

def p_Z(p):
    '''Z : ID DOT '''
    pass

def p_F(p):
    '''F : CON LPAREN factor RPAREN
         | FRONT
         | REAR
         | SIZE
         | DELETE
         | SUBSTR LPAREN ID COMMA int RPAREN'''
    pass

def p_if_stmnt(p):
    '''if_stmnt :   IF LPAREN condition RPAREN  BEGIN  statement_list END T'''
    pass

def p_T(p):
    '''T : ELIF PAREN condition RPAREN BEGIN  statement_list END K
         | empty'''
    pass

def p_K(p):
    '''K : ELSE BEGIN statement_list END 
         | empty'''
    pass

def p_while_stmt(p):
    ''' while_stmt : WHILE LPAREN condition RPAREN BEGIN statement_list END '''
    pass

def p_function_call(p):
    '''function_call : FUNC ID LPAREN parameter_list RPAREN BEGIN statement_list  RETURN ID SEMICOLON END'''
    pass

def p_parameter_list(p):
    '''parameter_list : type ID M '''
    pass

def p_M(p):
    '''M : COMMA parameter_list 
         | empty'''
    pass

def p_condition(p):
    '''condition : expression  comparison_operator  expression'''
    pass

def p_comparison_operator(p):
    '''comparison_operator : EQEQ 
                           | NOTEQ 
                           | LT 
                           | GT 
                           | LTEQ 
                           | GTEQ '''
    pass

def p_expression(p):
    '''expression : term 
                  | expression binary_operator term '''
    pass

def p_binary_operator(p):
    '''binary_operator : PLUS 
                       | MINUS 
                       | MUL 
                       | DIV 
                       | REM '''
    pass

def p_term(p):
    '''term :  factor 
            | term unary_operator factor '''
    pass

def p_unary_operator(p):
    ''' unary_operator : PLUSPLUS 
                       | MINUSMINUS '''
    pass

def p_factor(p):
    ''' factor : ID 
               | NUMBER 
               | STRING
               | TRUE
               | FALSE 
               | LPAREN expression RPAREN '''
    pass

def p_try_except(p):
    '''try_except : TRY x EXCEPT x'''
    pass

def p_x(p):
    '''x : BEGIN statement_list END'''
    pass

def p_print(p):
    '''print : ZOUT LPAREN y RPAREN'''
    pass

def p_y(p):
    '''y : NUMBER 
         | STRING 
         | ID'''
    pass

def p_empty(p):
	'''empty : '''

def find_column(input, p):
	line_start = input.rfind('\n', 0, p.lexpos) + 1
	return (p.lexpos - line_start) + 1

def p_error(p):
	if p is not None:
		column = find_column(code, t)		
		print("Found unexpected character '%s' at line '%s' and column '%s'" % (t.value, t.lineno, column))
	else:
		print("Unexpected end of input!Empty file or syntax error at EOF!")


import ply.yacc as yacc

parser = yacc.yacc()

try:
	if len(sys.argv) < 2:
		print("No file was given as a first argument!")
		print("Use command -> 'bash run.sh 'filename''")
	else:
		file = open(sys.argv[1])
		code = file.read()
		p = parser.parse(code)
except EOFError:
    print("File could not be opened!")
