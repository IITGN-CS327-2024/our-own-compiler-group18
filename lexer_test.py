from lexer import *

def main():

    text = open("test_cases_lexer/test1.zeva","r").read()
    # text = "2 + 3 "
    
    lexer = Lexer(text)
    Token = lexer.get_token()
    while Token.type != EOF:
       
        print(Token.__str__())
        Token = lexer.get_token()
    print(Token.value, Token.type)         # to check EOF

main()
