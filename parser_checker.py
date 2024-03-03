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
                 | compound_types'''
    # Handle individual statements here
    pass

# Add other grammar rules here...

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
