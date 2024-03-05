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
    '''declaration : var type identifier ASSIGN expression'''
    pass
def p_assignment(p):
    '''assignment :  identifier ASSIGN expression'''
    pass
def p_type(p):
    '''type : INT
            | BOOL
            | STR'''

    pass
def p_compound_types(p):
    '''compound_types :  A identifier ASSIGN K'''
    pass
def p_A(p):
    '''A : tuple
         | list'''
    pass

def p_K(p):
    '''K : LPAREN data RPAREN | LSPAREN data RSPAREN'''
    pass

def p_compounnd_type_access(p):
    '''compound_type_access : Z F 
                            | identifier LSPAREN expression RSPAREN'''
    pass

def p_Z(p):
    '''Z : identifier DOT '''
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
def p_K(p):
    '''K : 'else' 'begin' statement_list 'end' 
         | epsilon'''
    pass
def p_while(p):
    '''while :  'while' '(' condition ')' 'begin' statement_list 'end' '''
    pass
def p_function_call(p):
    '''function_call : 'func' identifier '(' parameter_list ')' 'begin' statement_list  'return' L';' 'end' '''
    pass
def p_L(p):
    '''L :  identifier
         | function_call'''
    pass
def p_parameter_list(p):
    '''parameter_list :  type identifier M '''
    pass
def p_M(p):
    '''M : ',' parameter_list 
         | epsilon '''
    pass
def p_condition(p):
    '''condition : expression comparison_operator expression '''
    pass
def p_comparison_operator(p):
    '''comparison_operator : == 
                           | != 
                           | < 
                           | > 
                           | <= 
                           | >= '''
    pass
def p_expression(p):
    '''expression : term 
                  | expression binary_operator term '''
    pass
def p_binary_operator(p):
    '''binary_operator : + 
                       | - 
                       | * 
                       | / 
                       | % 
                       | ^ '''
    pass
def p_term(p):
    '''term :  factor 
            | term unary_operator factor '''
    pass
def p_unary_operator(p):
    ''' unary_operator : ++ 
                       | -- '''
    pass
def p_factor(p):
    ''' factor :  identifier 
               |  literal 
               |  ( expression ) '''
    pass
def p_literal(p):
    ''' literal :  integer_literal 
                | string_literal 
                | boolean_literal '''
    pass
def p_integer_literal(p):
    '''integer_literal : digit_sequence '''
    pass
def p_digit_sequence(p):
    '''digit_sequence : digit 
                      | digit_sequence digit'''
    pass
def p_digit(p):
    '''digit : 0 
             | 1 
             | 2 
             | 3 
             | 4 
             | 5 
             | 6 
             | 7 
             | 8 
             | 9 '''
    pass
def p_string_literal(p):
    '''string_literal : character_sequence '''
    pass
def p_character_sequence(p):
    '''character_sequence : character 
                          | character_sequence character '''
    pass
def p_boolean_literal(p):
    '''boolean_literal :  true 
                       | false '''
    pass
def p_identifier(p):
    '''identifier : letter_sequence P 
                  | identifier letter_or_digit '''
    pass
def p_P(p):
    '''P :  _ 
         | epsilon '''
    pass
def p_letter(p):
    '''letter : a 
              | b 
              | c 
              |d 
              |d
              |e
              |f
              |g
              |h
              |i
              |j
              |k
              |l
              |m
              |n
              |o
              |p
              |q
              |r
              |s
              |t
              |u
              |v
              |w
              |x
              |y
              |z 
              | A 
              | B 
              | C 
              |D 
              |E
              |F
              |G
              |H
              |I
              |J
              |K
              |L
              |M
              |N
              |O
              |P
              |Q
              |R
              |S
              |T
              |U
              |V
              |W
              |X
              |Y
              | Z  '''
    pass
def p_letter_sequence(p):
    '''letter_sequence : letter 
                       | letter_sequence letter '''
    pass
def p_character(p):
    '''character :a 
              | b 
              | c 
              |d 
              |d
              |e
              |f
              |g
              |h
              |i
              |j
              |k
              |l
              |m
              |n
              |o
              |p
              |q
              |r
              |s
              |t
              |u
              |v
              |w
              |x
              |y
              |z 
              | A 
              | B 
              | C 
              |D 
              |E
              |F
              |G
              |H
              |I
              |J
              |K
              |L
              |M
              |N
              |O
              |P
              |Q
              |R
              |S
              |T
              |U
              |V
              |W
              |X
              |Y
              | Z
              |@
              |#
              |$
              |%
              |^
              |&
              |*
              |(
              |)
              |-
              |+
              |\
              |/*
              |/
              |<
              |>
              |.
              |, '''
    pass
def p_letter_or_digit(p):
    '''letter_or_digit : charecter_sequence | digit_sequence '''
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