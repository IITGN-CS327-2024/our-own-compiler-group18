import ply.yacc as yacc

# Get the token map from the lexer
tokens = [
    'EOF'
    'identifier'
    'Number'
    '<parenthesis>'
    '<end_of_stmt>'
    '<comma>'
    '<Dot>'
    '<quotation>'
    '<operator>'
    '<keyword>'
]

# Define the start symbol
start = 'start'

# Grammar rules
def p_start(p):
    'start : statement_list'
    # Handle the start symbol here
    pass

def p_statement_list(p):
    '''statement_list : statement SEMICOLON statement_list
                      | '''
    # Handle the list of statements here
    pass

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | if_stmnt
                 | while
                 | function_call
                 | compound_types'''
    # Handle individual statements here
    pass

def p_declaration(p):
    '''declaration  : var type identifier = expression'''

def p_declaration(p):
    '''assignment  : identifier = expression'''

def p_type(p):
    '''type  -> int|bool|st'''
def p_compound_types(p):
    '''Compound_type  : A identifier = K'''
def p_A(p):
    '''A  : tuple | list'''
def p_K(p):
    '''K  -> (data) | [data]'''
def 

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input:", p)

# Build the parser
parser = yacc.yacc()

# Read content from a text file (example.txt)
with open('example.txt', 'r') as file:
    s = file.read()

result = parser.parse(s)
print(result)
