import ply.yacc as yacc

# Get the token map from the lexer (you'll need to create your own lexer)
tokens = [
    'EOF'
    '<identifier>'
    '<Number>'
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
                 | compound_types
                 | compound_type_access'''
    # Handle individual statements here
    pass

# Add other grammar rules here...
def p_declaration(p):
    '''declaration : 'var' type identifier '=' expression '''
    pass
def p_assignment(p):
    '''assignment : identifier '=' expression'''
    pass
def p_type(p):
    '''type : int
            | bool
            | str'''

    pass
def p_compound_types(p):
    '''compound_types : A identifier P'''
    pass
def p_A(p):
    '''A : tuple
         | list'''
    pass
def p_K(p):
    '''K : (data)
         | [data]'''
    pass
def p_compounnd_type_access(p):
    '''compounnd_type_access : Z F 
                             | identifier expression'''
    pass
def p_Z(p):
    '''Z : identifier '.' '''
    pass
def p_F(p):
    '''F : add()
         | front
         |rear
         |size()
         |delete()'''
    pass
def p_if_stmnt(p):
    '''if_stmnt :  'if' '(' condition ')' 'begin' statement_list 'end' T'''
    pass
def p_T(p):
    '''T : 'elif' '(' condition ')' 'begin' statement_list 'end' K
         | epsilon '''
    pass

    
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input:", p)

# Build the parser
parser = yacc.yacc()

# Input loop
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
