
#tokens
from dataclasses import dataclass
import sys

# punctuators
EOF           = 'EOF'
ID            = '<identifier>'
INTEGER_CONST = '<Number>'
LPAREN        = '<parenthesis>'
RPAREN        = '<parenthesis>'
SEMI          = '<end_of_stmt>'
COMMA         = '<comma>'
LSPAREN       = '<parenthesis>'
RSPAREN       = '<parenthesis>'
DOT           = '<Dot>'
Quotation     = '<quotation>'

# operators
Assign        = '<operator>'
Plus          = '<operator>'
PlusPlus      = '<operator>'
Minus         = '<operator>'
Mul           = '<operator>'
Div           = '<operator>'
Rem           = '<operator>'
Eqeq          = '<operator>'
Noteq         = '<operator>'
Gt            = '<operator>'
Lt            = '<operator>'
Gteq          = '<operator>'
Lteq          = '<operator>'
Modulo        = '<operator>'
And           = '<operator>'
Or            = '<operator>'

# keywords
Var           = 'var'
Integer       = 'int'
Boolean       = 'bool'
Begin         = 'begin'
End           = 'end'
If            = 'if'
Eif           = 'elif'
Else          = 'else'
While         = 'while'
Print         = 'zout'
String        = 'str'
Function      = 'func'
Return        = 'return'
For           = 'for'
Con           = 'con'
Tuple         = 'tuple'
List          = 'list'
Add           = 'add'
size          = 'size'
List          = "list"
Front         = "front"
Rear          = "rear"
Delete        = 'delete'
Size          = 'size'
Try           = 'try'
Except        = 'except'

@dataclass
# class to store the token types and values
class Token:
    type: str
    value: object

    def __str__(self):
        return '({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

KEYWORDS = {
    'PROGRAM': Token('<key_word>', 'PROGRAM'),
    'var': Token('<key_word>', 'var'),
    'int': Token('<key_word>', 'int'),
    'bool': Token('<key_word>', 'bool'),
    'begin': Token('<key_word>', 'begin'),
    'end': Token('<key_word>', 'end'),
    'for': Token('<key_word>', 'for'),
    'true': Token('<key_word>', 'true'),
    'false': Token('<key_word>', 'false'),
    'if': Token('<key_word>', 'if'),
    'elif': Token('<key_word>', 'elif'),
    'else': Token('<key_word>', 'else'),
    'zout': Token('<key_word>', 'zout'),
    'while': Token('<key_word>', 'while'),
    'str': Token('<key_word>', 'str'),
    'func': Token('<key_word>', 'func'),
    'return': Token('<key_word>', 'return'),
    'try': Token('<key_word>', 'try'),
    'except': Token('<key_word>', 'except'),
    'add': Token('<key_word>', 'add'),
    'size': Token('<key_word>', 'size'),
    'list': Token('<key_word>', 'list'),
    'delete': Token('<key_word>', 'delete'),
    'front': Token('<key_word>', 'front'),
    'rear': Token('<key_word>', 'rear'),
    'con': Token('<key_word>', 'con'),
    'tuple': Token('<key_word>', 'tuple')

}

class Lexer(object):
    def __init__(self, text):

        self.text = text                        # stream of input
        self.pos = 0                            # current position in the stream
        self.lineNum = 1                        # line number in code
        self.curLinePos = 0                     # current position in current line of program
        self.indicator = 0

        if text == "":
            print("Empty Program")
            self.curChar = None

        else:
            self.curChar = self.text[self.pos]      # current character in the stream
        self.curLine = self.curChar             # current line of program read till now


    def error(self):
        print("Current Character", self.curChar)
        sys.exit('Invalid character')

    def nextChar(self):                         # advances the pos pointer
        self.pos += 1
        self.curLinePos += 1

        if self.pos > len(self.text) - 1:       # end of input stream
            self.curChar = None                 
        else:
            self.curChar = self.text[self.pos]
            self.curLine += self.curChar
            if self.curChar == '\n':
                self.lineNum+=1
                self.curLine=""
                self.curLinePos=0


    def peek(self):                             # returns the lookahead character
        if self.pos + 1 > len(self.text) - 1:
            return None
        else:
            return self.text[self.pos + 1]

    def skipSpaces(self):                       # to skip white spacses
        while self.curChar is not None and self.curChar.isspace():
            # if self.curChar == '\n':
            #     self.lineNum+=1
            #     self.curLine=""
            #     self.curLinePos=0
            self.nextChar()

    def skipComments(self):
        
        if self.curChar == '@':
            self.nextChar()
            if self.curChar == '*':
                # Multi-line comment
                self.nextChar()  # Skip '*'
                while self.curChar is not None and not (self.curChar == '*' and self.text[self.pos + 1] == '@'):
                    self.nextChar()
                self.nextChar()  # Skip '*'
                self.nextChar()  # Skip '@'
            else:
                # Single-line comment
                while self.curChar is not None and self.curChar != '\n':
                    self.nextChar()

    def number(self):                           
        # Consume all the consecutive digits and decimal if present.
        result = ''
        while self.curChar is not None and self.curChar.isdigit():
            result += self.curChar
            self.nextChar()

        if self.curChar == '.':
            result += self.curChar
            self.nextChar()

            while (
                self.curChar is not None and
                self.curChar.isdigit()
            ):
                result += self.curChar
                self.nextChar()

            token = Token('REAL_CONST', float(result))
        else:
            token = Token(INTEGER_CONST, int(result))

        return token

    def _id(self):
        # Handles identifiers and reserved keywords
        result = ''
        while self.curChar is not None and self.curChar.isalnum():
            result += self.curChar
            self.nextChar()
            
        token = KEYWORDS.get(result, Token(ID, result))
        return token
    
                     
    def Stringlex(self):
        # Handles strings
        result = ''
        while self.curChar != '"':
            result += self.curChar
            self.nextChar()

        token = Token(String, result)
        return token

    def get_token(self):
        # returns the token and token type
        while self.curChar is not None:

            if self.curChar.isspace():
                self.skipSpaces()
                continue

            if self.curChar == '@':
                self.skipComments()
                continue

            if self.curChar.isalpha():
                return self._id()

            if self.curChar.isdigit():
                return self.number()

            
            if self.curChar == '=':
                if self.peek() == '=':
                    self.nextChar()
                    self.nextChar()
                    return Token(Eqeq, '==')
                else:
                    self.nextChar()
                    return Token(Assign, '=') 

            if self.curChar == "|":
                if self.peek() == "|":
                    self.nextChar()
                    self.nextChar()
                    return Token(Or, "||")


            if self.curChar == "&":
                if self.peek() == "&":
                    self.nextChar()
                    self.nextChar()
                    return Token(And, "&&")

            if self.curChar == '>':
                if self.peek() == '=':
                    self.nextChar()
                    self.nextChar()
                    return Token(Gteq, '>=')
                else:
                    self.nextChar()
                    return Token(Gt, '>')

            if self.curChar == '<':
                if self.peek() == '=':
                    self.nextChar()
                    self.nextChar()
                    return Token(Lteq, '<=')
                elif self.peek() == '>':
                    self.nextChar()
                    self.nextChar()
                    return Token(Noteq, '!=') # <>
                else:
                    self.nextChar()
                    return Token(Lt, '<')

            if self.curChar == '*':                 
                self.nextChar()
                return Token(Mul, '*')

            if self.curChar == "%":
                self.nextChar()
                return Token(Rem, '%')

            if self.curChar == '+':
                if self.peek() == '+':
                    self.nextChar()
                    self.nextChar()
                    return Token(PlusPlus, '++')
                else:
                    return Token(Plus, '+')

            if self.curChar == '-':
                self.nextChar()
                return Token(Minus, '-')

            if self.curChar == '/':  
              self.nextChar()
              return Token(Div, '/')

            if self.curChar == '(':
                self.nextChar()
                return Token(LPAREN, '(')

            if self.curChar == ')':
                self.nextChar()
                return Token(RPAREN, ')')

            if self.curChar == ';':
                self.nextChar()
                return Token(SEMI, ';')

            if self.curChar == ',':
                self.nextChar()
                return Token(COMMA, ',')
            
            
            if ((self.curChar == '"') and (self.indicator == 0 or self.indicator == 2)):
                self.indicator += 1
                if(self.indicator == 3): 
                    self.nextChar()
                    self.indicator = 0
                return Token(Quotation, ' /" ')
            
            if self.curChar == '"':
                self.nextChar()
                self.indicator += 1
                return self.Stringlex()  

            if self.curChar == '[':
                self.nextChar()
                return Token(LSPAREN, '[')   

            if self.curChar == ']':
                self.nextChar()
                return Token(RSPAREN, ']')
            
            if self.curChar == '.':
                self.nextChar()
                return Token(DOT, '.')
            
            self.error()

        return Token(EOF, None)

