
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSPLUSMINUSMINUSnonassocEQEQNOTEQGTLTGTEQLTEQleftPLUSMINUSleftMULDIVREMASSIGN BEGIN BOOL COMMA CON DELETE DIV DOT ELIF ELSE END EQEQ EXCEPT FALSE FRONT FUNC GT GTEQ ID IF INT LIST LPAREN LSPAREN LT LTEQ MINUS MINUSMINUS MUL NOTEQ NUMBER PLUS PLUSPLUS REAR REM RETURN RPAREN RSPAREN SEMICOLON SIZE STR STRING SUBSTR TRUE TRY TUPLE VAR WHILE ZOUTstart : statement_liststatement_list : statement SEMICOLON statement_list\n                      | emptystatement : declaration\n                 | assignment\n                 | if_stmnt\n                 | while_stmt\n                 | function_call\n                 | compound_types\n                 | compound_type_access\n                 | try_except\n                 | printdeclaration : VAR type ID ASSIGN expression assignment :  ID ASSIGN expressiontype : INT\n            | BOOL\n            | STRcompound_types : A ID ASSIGN NA : TUPLE\n         | LISTN : LPAREN data RPAREN\n         | LSPAREN data RSPARENdata : factor PP : COMMA data P\n         | emptycompound_type_access : Z F \n                            | ID LSPAREN expression RSPARENZ : ID DOT F : CON LPAREN factor RPAREN\n         | FRONT\n         | REAR\n         | SIZE\n         | DELETE\n         | SUBSTR LPAREN factor COMMA factor RPAREN\n         | emptyif_stmnt : IF LPAREN condition RPAREN  BEGIN  statement_list END TT :  ELIF LPAREN condition RPAREN BEGIN  statement_list END K\n         |  emptyK : ELSE BEGIN statement_list END \n         | emptywhile_stmt : WHILE LPAREN condition RPAREN BEGIN statement_list ENDfunction_call : FUNC ID LPAREN parameter_list RPAREN BEGIN statement_list  RETURN ID SEMICOLON ENDparameter_list : type ID M M : COMMA parameter_list \n         | emptycondition : expression  comparison_operator  expressioncomparison_operator : EQEQ \n                           | NOTEQ \n                           | LT \n                           | GT \n                           | LTEQ \n                           | GTEQ expression :  D term  D : expression binary_operator \n         | emptybinary_operator : PLUS \n                       | MINUS \n                       | MUL \n                       | DIV \n                       | REM term :  factor \n            | term unary_operator factor  unary_operator : PLUSPLUS \n                       | MINUSMINUS  factor :  ID \n               | NUMBER \n               | STRING\n               | TRUE\n               | FALSE \n               | LPAREN expression RPAREN try_except : TRY x EXCEPT xx : BEGIN statement_list ENDprint : ZOUT LPAREN y RPARENy : NUMBER \n         | STRING \n         | ID\n         | compound_type_accessempty : '
    
_lr_action_items = {'$end':([0,1,2,4,25,48,],[-78,0,-1,-3,-78,-2,]),'VAR':([0,25,46,108,110,122,149,155,],[14,14,14,14,14,14,14,14,]),'ID':([0,18,19,23,24,25,26,27,28,29,30,31,33,34,46,47,51,52,59,60,68,69,70,71,72,73,74,82,85,86,87,88,89,90,91,94,96,97,104,105,106,108,110,117,122,128,141,143,149,155,],[15,35,36,-19,-20,15,49,-15,-16,-17,-78,-78,-78,-78,15,66,77,-55,77,77,-78,-54,-56,-57,-58,-59,-60,-78,-78,-47,-48,-49,-50,-51,-52,112,77,77,77,-63,-64,15,15,77,15,77,144,-78,15,15,]),'IF':([0,25,46,108,110,122,149,155,],[16,16,16,16,16,16,16,16,]),'WHILE':([0,25,46,108,110,122,149,155,],[17,17,17,17,17,17,17,17,]),'FUNC':([0,25,46,108,110,122,149,155,],[18,18,18,18,18,18,18,18,]),'TRY':([0,25,46,108,110,122,149,155,],[21,21,21,21,21,21,21,21,]),'ZOUT':([0,25,46,108,110,122,149,155,],[22,22,22,22,22,22,22,22,]),'TUPLE':([0,25,46,108,110,122,149,155,],[23,23,23,23,23,23,23,23,]),'LIST':([0,25,46,108,110,122,149,155,],[24,24,24,24,24,24,24,24,]),'SEMICOLON':([3,5,6,7,8,9,10,11,12,13,20,32,37,39,40,41,42,44,50,75,76,77,78,79,80,81,83,95,100,101,102,103,116,118,119,126,130,132,133,137,138,140,144,148,151,152,154,157,],[25,-4,-5,-6,-7,-8,-9,-10,-11,-12,-78,-28,-26,-30,-31,-32,-33,-35,-14,-53,-61,-65,-66,-67,-68,-69,-27,-18,-71,-72,-73,-13,-29,-62,-70,-21,-22,-78,-41,-34,-36,-38,146,-42,-78,-37,-40,-39,]),'END':([4,25,46,48,62,108,110,120,121,146,149,150,155,156,],[-3,-78,-78,-2,101,-78,-78,132,133,148,-78,151,-78,157,]),'RETURN':([4,25,48,122,134,],[-3,-78,-2,-78,141,]),'INT':([14,57,124,],[27,27,27,]),'BOOL':([14,57,124,],[28,28,28,]),'STR':([14,57,124,],[29,29,29,]),'ASSIGN':([15,36,49,],[30,58,68,]),'LSPAREN':([15,58,66,],[31,97,31,]),'DOT':([15,66,],[32,32,]),'LPAREN':([16,17,22,30,31,33,34,35,38,43,51,52,58,59,60,68,69,70,71,72,73,74,82,85,86,87,88,89,90,91,96,97,104,105,106,117,128,139,143,],[33,34,47,-78,-78,-78,-78,57,59,60,82,-55,96,82,82,-78,-54,-56,-57,-58,-59,-60,-78,-78,-47,-48,-49,-50,-51,-52,82,82,82,-63,-64,82,82,143,-78,]),'CON':([20,32,],[38,-28,]),'FRONT':([20,32,],[39,-28,]),'REAR':([20,32,],[40,-28,]),'SIZE':([20,32,],[41,-28,]),'DELETE':([20,32,],[42,-28,]),'SUBSTR':([20,32,],[43,-28,]),'RPAREN':([20,32,37,39,40,41,42,44,54,56,63,64,65,66,67,75,76,77,78,79,80,81,83,93,98,107,109,112,113,114,116,118,119,123,125,127,129,131,135,136,137,142,145,],[-78,-28,-26,-30,-31,-32,-33,-35,84,92,102,-74,-75,-76,-77,-53,-61,-65,-66,-67,-68,-69,-27,111,116,119,-46,-78,126,-78,-29,-62,-70,-43,-45,-23,-25,137,-44,-78,-34,-24,147,]),'BEGIN':([21,61,84,92,111,147,153,],[46,46,108,110,122,149,155,]),'NUMBER':([30,31,33,34,47,51,52,59,60,68,69,70,71,72,73,74,82,85,86,87,88,89,90,91,96,97,104,105,106,117,128,143,],[-78,-78,-78,-78,64,78,-55,78,78,-78,-54,-56,-57,-58,-59,-60,-78,-78,-47,-48,-49,-50,-51,-52,78,78,78,-63,-64,78,78,-78,]),'STRING':([30,31,33,34,47,51,52,59,60,68,69,70,71,72,73,74,82,85,86,87,88,89,90,91,96,97,104,105,106,117,128,143,],[-78,-78,-78,-78,65,79,-55,79,79,-78,-54,-56,-57,-58,-59,-60,-78,-78,-47,-48,-49,-50,-51,-52,79,79,79,-63,-64,79,79,-78,]),'TRUE':([30,31,33,34,51,52,59,60,68,69,70,71,72,73,74,82,85,86,87,88,89,90,91,96,97,104,105,106,117,128,143,],[-78,-78,-78,-78,80,-55,80,80,-78,-54,-56,-57,-58,-59,-60,-78,-78,-47,-48,-49,-50,-51,-52,80,80,80,-63,-64,80,80,-78,]),'FALSE':([30,31,33,34,51,52,59,60,68,69,70,71,72,73,74,82,85,86,87,88,89,90,91,96,97,104,105,106,117,128,143,],[-78,-78,-78,-78,81,-55,81,81,-78,-54,-56,-57,-58,-59,-60,-78,-78,-47,-48,-49,-50,-51,-52,81,81,81,-63,-64,81,81,-78,]),'EXCEPT':([45,101,],[61,-72,]),'PLUS':([50,53,55,75,76,77,78,79,80,81,103,107,109,118,119,],[70,70,70,-53,-61,-65,-66,-67,-68,-69,70,70,70,-62,-70,]),'MINUS':([50,53,55,75,76,77,78,79,80,81,103,107,109,118,119,],[71,71,71,-53,-61,-65,-66,-67,-68,-69,71,71,71,-62,-70,]),'MUL':([50,53,55,75,76,77,78,79,80,81,103,107,109,118,119,],[72,72,72,-53,-61,-65,-66,-67,-68,-69,72,72,72,-62,-70,]),'DIV':([50,53,55,75,76,77,78,79,80,81,103,107,109,118,119,],[73,73,73,-53,-61,-65,-66,-67,-68,-69,73,73,73,-62,-70,]),'REM':([50,53,55,75,76,77,78,79,80,81,103,107,109,118,119,],[74,74,74,-53,-61,-65,-66,-67,-68,-69,74,74,74,-62,-70,]),'RSPAREN':([53,75,76,77,78,79,80,81,114,115,118,119,127,129,136,142,],[83,-53,-61,-65,-66,-67,-68,-69,-78,130,-62,-70,-23,-25,-78,-24,]),'EQEQ':([55,75,76,77,78,79,80,81,118,119,],[86,-53,-61,-65,-66,-67,-68,-69,-62,-70,]),'NOTEQ':([55,75,76,77,78,79,80,81,118,119,],[87,-53,-61,-65,-66,-67,-68,-69,-62,-70,]),'LT':([55,75,76,77,78,79,80,81,118,119,],[88,-53,-61,-65,-66,-67,-68,-69,-62,-70,]),'GT':([55,75,76,77,78,79,80,81,118,119,],[89,-53,-61,-65,-66,-67,-68,-69,-62,-70,]),'LTEQ':([55,75,76,77,78,79,80,81,118,119,],[90,-53,-61,-65,-66,-67,-68,-69,-62,-70,]),'GTEQ':([55,75,76,77,78,79,80,81,118,119,],[91,-53,-61,-65,-66,-67,-68,-69,-62,-70,]),'PLUSPLUS':([75,76,77,78,79,80,81,118,119,],[105,-61,-65,-66,-67,-68,-69,-62,-70,]),'MINUSMINUS':([75,76,77,78,79,80,81,118,119,],[106,-61,-65,-66,-67,-68,-69,-62,-70,]),'COMMA':([77,78,79,80,81,99,112,114,119,127,129,136,142,],[-65,-66,-67,-68,-69,117,124,128,-70,-23,-25,128,-24,]),'ELIF':([132,],[139,]),'ELSE':([151,],[153,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statement_list':([0,25,46,108,110,122,149,155,],[2,48,62,120,121,134,150,156,]),'statement':([0,25,46,108,110,122,149,155,],[3,3,3,3,3,3,3,3,]),'empty':([0,20,25,30,31,33,34,46,68,82,85,108,110,112,114,122,132,136,143,149,151,155,],[4,44,4,52,52,52,52,4,52,52,52,4,4,125,129,4,140,129,52,4,154,4,]),'declaration':([0,25,46,108,110,122,149,155,],[5,5,5,5,5,5,5,5,]),'assignment':([0,25,46,108,110,122,149,155,],[6,6,6,6,6,6,6,6,]),'if_stmnt':([0,25,46,108,110,122,149,155,],[7,7,7,7,7,7,7,7,]),'while_stmt':([0,25,46,108,110,122,149,155,],[8,8,8,8,8,8,8,8,]),'function_call':([0,25,46,108,110,122,149,155,],[9,9,9,9,9,9,9,9,]),'compound_types':([0,25,46,108,110,122,149,155,],[10,10,10,10,10,10,10,10,]),'compound_type_access':([0,25,46,47,108,110,122,149,155,],[11,11,11,67,11,11,11,11,11,]),'try_except':([0,25,46,108,110,122,149,155,],[12,12,12,12,12,12,12,12,]),'print':([0,25,46,108,110,122,149,155,],[13,13,13,13,13,13,13,13,]),'A':([0,25,46,108,110,122,149,155,],[19,19,19,19,19,19,19,19,]),'Z':([0,25,46,47,108,110,122,149,155,],[20,20,20,20,20,20,20,20,20,]),'type':([14,57,124,],[26,94,94,]),'F':([20,],[37,]),'x':([21,61,],[45,100,]),'expression':([30,31,33,34,68,82,85,143,],[50,53,55,55,103,107,109,55,]),'D':([30,31,33,34,68,82,85,143,],[51,51,51,51,51,51,51,51,]),'condition':([33,34,143,],[54,56,145,]),'y':([47,],[63,]),'binary_operator':([50,53,55,103,107,109,],[69,69,69,69,69,69,]),'term':([51,],[75,]),'factor':([51,59,60,96,97,104,117,128,],[76,98,99,114,114,118,131,114,]),'comparison_operator':([55,],[85,]),'parameter_list':([57,124,],[93,135,]),'N':([58,],[95,]),'unary_operator':([75,],[104,]),'data':([96,97,128,],[113,115,136,]),'M':([112,],[123,]),'P':([114,136,],[127,142,]),'T':([132,],[138,]),'K':([151,],[152,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statement_list','start',1,'p_start','my_lex.py',148),
  ('statement_list -> statement SEMICOLON statement_list','statement_list',3,'p_statement_list','my_lex.py',153),
  ('statement_list -> empty','statement_list',1,'p_statement_list','my_lex.py',154),
  ('statement -> declaration','statement',1,'p_statement','my_lex.py',159),
  ('statement -> assignment','statement',1,'p_statement','my_lex.py',160),
  ('statement -> if_stmnt','statement',1,'p_statement','my_lex.py',161),
  ('statement -> while_stmt','statement',1,'p_statement','my_lex.py',162),
  ('statement -> function_call','statement',1,'p_statement','my_lex.py',163),
  ('statement -> compound_types','statement',1,'p_statement','my_lex.py',164),
  ('statement -> compound_type_access','statement',1,'p_statement','my_lex.py',165),
  ('statement -> try_except','statement',1,'p_statement','my_lex.py',166),
  ('statement -> print','statement',1,'p_statement','my_lex.py',167),
  ('declaration -> VAR type ID ASSIGN expression','declaration',5,'p_declaration','my_lex.py',172),
  ('assignment -> ID ASSIGN expression','assignment',3,'p_assignment','my_lex.py',176),
  ('type -> INT','type',1,'p_type','my_lex.py',180),
  ('type -> BOOL','type',1,'p_type','my_lex.py',181),
  ('type -> STR','type',1,'p_type','my_lex.py',182),
  ('compound_types -> A ID ASSIGN N','compound_types',4,'p_compound_types','my_lex.py',187),
  ('A -> TUPLE','A',1,'p_A','my_lex.py',192),
  ('A -> LIST','A',1,'p_A','my_lex.py',193),
  ('N -> LPAREN data RPAREN','N',3,'p_N','my_lex.py',197),
  ('N -> LSPAREN data RSPAREN','N',3,'p_N','my_lex.py',198),
  ('data -> factor P','data',2,'p_data','my_lex.py',202),
  ('P -> COMMA data P','P',3,'p_P','my_lex.py',206),
  ('P -> empty','P',1,'p_P','my_lex.py',207),
  ('compound_type_access -> Z F','compound_type_access',2,'p_compound_type_access','my_lex.py',211),
  ('compound_type_access -> ID LSPAREN expression RSPAREN','compound_type_access',4,'p_compound_type_access','my_lex.py',212),
  ('Z -> ID DOT','Z',2,'p_Z','my_lex.py',216),
  ('F -> CON LPAREN factor RPAREN','F',4,'p_F','my_lex.py',220),
  ('F -> FRONT','F',1,'p_F','my_lex.py',221),
  ('F -> REAR','F',1,'p_F','my_lex.py',222),
  ('F -> SIZE','F',1,'p_F','my_lex.py',223),
  ('F -> DELETE','F',1,'p_F','my_lex.py',224),
  ('F -> SUBSTR LPAREN factor COMMA factor RPAREN','F',6,'p_F','my_lex.py',225),
  ('F -> empty','F',1,'p_F','my_lex.py',226),
  ('if_stmnt -> IF LPAREN condition RPAREN BEGIN statement_list END T','if_stmnt',8,'p_if_stmnt','my_lex.py',230),
  ('T -> ELIF LPAREN condition RPAREN BEGIN statement_list END K','T',8,'p_T','my_lex.py',234),
  ('T -> empty','T',1,'p_T','my_lex.py',235),
  ('K -> ELSE BEGIN statement_list END','K',4,'p_K','my_lex.py',239),
  ('K -> empty','K',1,'p_K','my_lex.py',240),
  ('while_stmt -> WHILE LPAREN condition RPAREN BEGIN statement_list END','while_stmt',7,'p_while_stmt','my_lex.py',244),
  ('function_call -> FUNC ID LPAREN parameter_list RPAREN BEGIN statement_list RETURN ID SEMICOLON END','function_call',11,'p_function_call','my_lex.py',248),
  ('parameter_list -> type ID M','parameter_list',3,'p_parameter_list','my_lex.py',252),
  ('M -> COMMA parameter_list','M',2,'p_M','my_lex.py',256),
  ('M -> empty','M',1,'p_M','my_lex.py',257),
  ('condition -> expression comparison_operator expression','condition',3,'p_condition','my_lex.py',261),
  ('comparison_operator -> EQEQ','comparison_operator',1,'p_comparison_operator','my_lex.py',265),
  ('comparison_operator -> NOTEQ','comparison_operator',1,'p_comparison_operator','my_lex.py',266),
  ('comparison_operator -> LT','comparison_operator',1,'p_comparison_operator','my_lex.py',267),
  ('comparison_operator -> GT','comparison_operator',1,'p_comparison_operator','my_lex.py',268),
  ('comparison_operator -> LTEQ','comparison_operator',1,'p_comparison_operator','my_lex.py',269),
  ('comparison_operator -> GTEQ','comparison_operator',1,'p_comparison_operator','my_lex.py',270),
  ('expression -> D term','expression',2,'p_expression','my_lex.py',274),
  ('D -> expression binary_operator','D',2,'p_D','my_lex.py',278),
  ('D -> empty','D',1,'p_D','my_lex.py',279),
  ('binary_operator -> PLUS','binary_operator',1,'p_binary_operator','my_lex.py',283),
  ('binary_operator -> MINUS','binary_operator',1,'p_binary_operator','my_lex.py',284),
  ('binary_operator -> MUL','binary_operator',1,'p_binary_operator','my_lex.py',285),
  ('binary_operator -> DIV','binary_operator',1,'p_binary_operator','my_lex.py',286),
  ('binary_operator -> REM','binary_operator',1,'p_binary_operator','my_lex.py',287),
  ('term -> factor','term',1,'p_term','my_lex.py',291),
  ('term -> term unary_operator factor','term',3,'p_term','my_lex.py',292),
  ('unary_operator -> PLUSPLUS','unary_operator',1,'p_unary_operator','my_lex.py',296),
  ('unary_operator -> MINUSMINUS','unary_operator',1,'p_unary_operator','my_lex.py',297),
  ('factor -> ID','factor',1,'p_factor','my_lex.py',301),
  ('factor -> NUMBER','factor',1,'p_factor','my_lex.py',302),
  ('factor -> STRING','factor',1,'p_factor','my_lex.py',303),
  ('factor -> TRUE','factor',1,'p_factor','my_lex.py',304),
  ('factor -> FALSE','factor',1,'p_factor','my_lex.py',305),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','my_lex.py',306),
  ('try_except -> TRY x EXCEPT x','try_except',4,'p_try_except','my_lex.py',310),
  ('x -> BEGIN statement_list END','x',3,'p_x','my_lex.py',314),
  ('print -> ZOUT LPAREN y RPAREN','print',4,'p_print','my_lex.py',318),
  ('y -> NUMBER','y',1,'p_y','my_lex.py',322),
  ('y -> STRING','y',1,'p_y','my_lex.py',323),
  ('y -> ID','y',1,'p_y','my_lex.py',324),
  ('y -> compound_type_access','y',1,'p_y','my_lex.py',325),
  ('empty -> <empty>','empty',0,'p_empty','my_lex.py',329),
]
