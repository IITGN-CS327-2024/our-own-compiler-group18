
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVREMnonassocEQEQNOTEQGTLTGTEQLTEQrightPLUSPLUSMINUSMINUSADD ASSIGN BEGIN BOOL COMMA CON DELETE DIV DOT ELIF ELSE END EQEQ EXCEPT FALSE FRONT FUNC GT GTEQ ID IF INT LIST LPAREN LSPAREN LT LTEQ MINUS MINUSMINUS MUL NOTEQ NUMBER PLUS PLUSPLUS REAR REM RETURN RPAREN RSPAREN SEMICOLON SIZE STR STRING SUBSTR TRUE TRY TUPLE VAR WHILE ZOUTstart : statement_liststatement_list : statement_list statement SEMICOLON\n                      | emptystatement : declaration\n                 | assignment\n                 | if_stmnt\n                 | while_stmt\n                 | function_call\n                 | expression\n                 | compound_types\n                 | compound_type_access\n                 | try_except\n                 | printdeclaration : VAR type assignmentassignment :  ID ASSIGN LL : statement\n       | ID LPAREN data RPARENtype : INT\n            | BOOL\n            | STRcompound_types : A ID ASSIGN LPAREN data RPARENA : TUPLE\n         | LISTdata : expression data\n            | COMMA data\n            | emptycompound_type_access : ID DOT F \n                            | ID LSPAREN expression RSPARENF : CON LPAREN factor RPAREN\n         | FRONT\n         | ADD LPAREN factor RPAREN\n         | REAR\n         | SIZE\n         | DELETE\n         | SUBSTR LPAREN factor COMMA factor RPAREN\n         | emptyif_stmnt : IF LPAREN condition RPAREN  BEGIN  statement_list END TT :  ELIF LPAREN condition RPAREN BEGIN  statement_list END K\n         |  emptyK : ELSE BEGIN statement_list END \n         | emptywhile_stmt : WHILE LPAREN condition RPAREN BEGIN statement_list ENDfunction_call : FUNC ID LPAREN parameter_list RPAREN BEGIN statement_list  RETURN data SEMICOLON ENDparameter_list : type ID optional_parameter_list\n                    | emptyoptional_parameter_list : COMMA type ID optional_parameter_list\n                              | emptycondition : expression  comparison_operator  expressioncomparison_operator : EQEQ \n                           | NOTEQ \n                           | LT \n                           | GT \n                           | LTEQ \n                           | GTEQ expression : expression binary_operator expression\n                  | expression unary_operator\n                  | factorbinary_operator  : MINUS \n                      | MUL \n                      | PLUS\n                      | DIV \n                      | REM  unary_operator : PLUSPLUS \n                       | MINUSMINUS  factor :  ID \n               | NUMBER \n               | STRING\n               | TRUE\n               | FALSE \n               | LPAREN expression RPARENtry_except : BEGIN TRY statement_list EXCEPT statement_list ENDprint : ZOUT LPAREN y RPARENy : expression\n         | compound_type_accessempty : '
    
_lr_action_items = {'VAR':([0,2,3,31,45,51,75,96,110,112,113,123,125,126,134,149,150,155,156,],[-75,15,-3,-2,15,-75,15,-75,-75,15,-75,15,15,-75,15,-75,15,-75,15,]),'ID':([0,2,3,18,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,50,51,52,55,56,74,75,83,84,85,86,89,90,91,92,93,94,95,96,99,101,104,105,110,112,113,122,123,125,126,134,135,140,142,149,150,155,156,],[-75,16,-3,50,53,-57,54,-66,-67,-68,-69,-22,-23,-2,50,-56,-58,-59,-60,-61,-62,-63,-64,58,-18,-19,-20,59,50,50,-65,-75,50,82,-55,-70,16,50,50,50,50,50,-49,-50,-51,-52,-53,-54,-75,115,50,50,50,-75,16,-75,50,16,16,-75,16,141,50,50,-75,16,-75,16,]),'IF':([0,2,3,31,45,51,75,96,110,112,113,123,125,126,134,149,150,155,156,],[-75,17,-3,-2,17,-75,17,-75,-75,17,-75,17,17,-75,17,-75,17,-75,17,]),'WHILE':([0,2,3,31,45,51,75,96,110,112,113,123,125,126,134,149,150,155,156,],[-75,20,-3,-2,20,-75,20,-75,-75,20,-75,20,20,-75,20,-75,20,-75,20,]),'FUNC':([0,2,3,31,45,51,75,96,110,112,113,123,125,126,134,149,150,155,156,],[-75,21,-3,-2,21,-75,21,-75,-75,21,-75,21,21,-75,21,-75,21,-75,21,]),'BEGIN':([0,2,3,31,45,51,75,88,96,97,110,112,113,114,123,125,126,134,147,149,150,153,155,156,],[-75,19,-3,-2,19,-75,19,110,-75,113,-75,19,-75,126,19,19,-75,19,149,-75,19,155,-75,19,]),'ZOUT':([0,2,3,31,45,51,75,96,110,112,113,123,125,126,134,149,150,155,156,],[-75,24,-3,-2,24,-75,24,-75,-75,24,-75,24,24,-75,24,-75,24,-75,24,]),'NUMBER':([0,2,3,18,22,25,26,27,28,31,32,33,34,35,36,37,38,39,40,45,47,48,50,51,52,55,56,74,75,83,84,85,86,89,90,91,92,93,94,95,96,101,104,105,110,112,113,122,123,125,126,134,140,142,149,150,155,156,],[-75,25,-3,25,-57,-66,-67,-68,-69,-2,25,-56,-58,-59,-60,-61,-62,-63,-64,25,25,25,-65,-75,25,25,-55,-70,25,25,25,25,25,25,-49,-50,-51,-52,-53,-54,-75,25,25,25,-75,25,-75,25,25,25,-75,25,25,25,-75,25,-75,25,]),'STRING':([0,2,3,18,22,25,26,27,28,31,32,33,34,35,36,37,38,39,40,45,47,48,50,51,52,55,56,74,75,83,84,85,86,89,90,91,92,93,94,95,96,101,104,105,110,112,113,122,123,125,126,134,140,142,149,150,155,156,],[-75,26,-3,26,-57,-66,-67,-68,-69,-2,26,-56,-58,-59,-60,-61,-62,-63,-64,26,26,26,-65,-75,26,26,-55,-70,26,26,26,26,26,26,-49,-50,-51,-52,-53,-54,-75,26,26,26,-75,26,-75,26,26,26,-75,26,26,26,-75,26,-75,26,]),'TRUE':([0,2,3,18,22,25,26,27,28,31,32,33,34,35,36,37,38,39,40,45,47,48,50,51,52,55,56,74,75,83,84,85,86,89,90,91,92,93,94,95,96,101,104,105,110,112,113,122,123,125,126,134,140,142,149,150,155,156,],[-75,27,-3,27,-57,-66,-67,-68,-69,-2,27,-56,-58,-59,-60,-61,-62,-63,-64,27,27,27,-65,-75,27,27,-55,-70,27,27,27,27,27,27,-49,-50,-51,-52,-53,-54,-75,27,27,27,-75,27,-75,27,27,27,-75,27,27,27,-75,27,-75,27,]),'FALSE':([0,2,3,18,22,25,26,27,28,31,32,33,34,35,36,37,38,39,40,45,47,48,50,51,52,55,56,74,75,83,84,85,86,89,90,91,92,93,94,95,96,101,104,105,110,112,113,122,123,125,126,134,140,142,149,150,155,156,],[-75,28,-3,28,-57,-66,-67,-68,-69,-2,28,-56,-58,-59,-60,-61,-62,-63,-64,28,28,28,-65,-75,28,28,-55,-70,28,28,28,28,28,28,-49,-50,-51,-52,-53,-54,-75,28,28,28,-75,28,-75,28,28,28,-75,28,28,28,-75,28,-75,28,]),'LPAREN':([0,2,3,17,18,20,22,24,25,26,27,28,31,32,33,34,35,36,37,38,39,40,45,47,48,50,51,52,53,55,56,59,63,65,69,74,75,78,83,84,85,86,89,90,91,92,93,94,95,96,101,104,105,110,112,113,122,123,125,126,134,138,140,142,149,150,155,156,],[-75,18,-3,48,18,52,-57,55,-66,-67,-68,-69,-2,18,-56,-58,-59,-60,-61,-62,-63,-64,18,18,18,-65,-75,18,77,18,-55,83,84,85,86,-70,18,101,18,18,18,18,18,-49,-50,-51,-52,-53,-54,-75,18,18,18,-75,18,-75,18,18,18,-75,18,142,18,18,-75,18,-75,18,]),'TUPLE':([0,2,3,31,45,51,75,96,110,112,113,123,125,126,134,149,150,155,156,],[-75,29,-3,-2,29,-75,29,-75,-75,29,-75,29,29,-75,29,-75,29,-75,29,]),'LIST':([0,2,3,31,45,51,75,96,110,112,113,123,125,126,134,149,150,155,156,],[-75,30,-3,-2,30,-75,30,-75,-75,30,-75,30,30,-75,30,-75,30,-75,30,]),'$end':([0,1,2,3,31,],[-75,0,-1,-3,-2,]),'EXCEPT':([3,31,51,75,],[-3,-2,-75,96,]),'END':([3,31,96,110,112,113,123,125,146,149,150,155,156,],[-3,-2,-75,-75,124,-75,132,133,148,-75,151,-75,157,]),'RETURN':([3,31,126,134,],[-3,-2,-75,140,]),'SEMICOLON':([4,5,6,7,8,9,10,11,12,13,14,16,22,25,26,27,28,33,39,40,46,50,56,57,59,60,61,62,64,66,67,68,70,74,87,102,104,105,106,117,118,119,120,121,124,130,132,133,136,137,139,140,143,148,151,152,154,157,],[31,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-65,-57,-66,-67,-68,-69,-56,-63,-64,-75,-65,-55,-14,-65,-15,-16,-27,-30,-32,-33,-34,-36,-70,-28,-72,-75,-75,-26,-17,-24,-25,-29,-31,-71,-21,-75,-42,-35,-37,-39,-75,146,-43,-75,-38,-41,-40,]),'MINUS':([10,16,22,25,26,27,28,33,39,40,49,50,56,59,71,73,74,80,82,104,111,],[34,-65,-57,-66,-67,-68,-69,-56,-63,-64,34,-65,34,-65,34,34,-70,34,-65,34,34,]),'MUL':([10,16,22,25,26,27,28,33,39,40,49,50,56,59,71,73,74,80,82,104,111,],[35,-65,-57,-66,-67,-68,-69,-56,-63,-64,35,-65,35,-65,35,35,-70,35,-65,35,35,]),'PLUS':([10,16,22,25,26,27,28,33,39,40,49,50,56,59,71,73,74,80,82,104,111,],[36,-65,-57,-66,-67,-68,-69,-56,-63,-64,36,-65,36,-65,36,36,-70,36,-65,36,36,]),'DIV':([10,16,22,25,26,27,28,33,39,40,49,50,56,59,71,73,74,80,82,104,111,],[37,-65,-57,-66,-67,-68,-69,-56,-63,-64,37,-65,37,-65,37,37,-70,37,-65,37,37,]),'REM':([10,16,22,25,26,27,28,33,39,40,49,50,56,59,71,73,74,80,82,104,111,],[38,-65,-57,-66,-67,-68,-69,-56,-63,-64,38,-65,38,-65,38,38,-70,38,-65,38,38,]),'PLUSPLUS':([10,16,22,25,26,27,28,33,39,40,49,50,56,59,71,73,74,80,82,104,111,],[39,-65,-57,-66,-67,-68,-69,-56,-63,-64,39,-65,39,-65,39,39,-70,39,-65,39,39,]),'MINUSMINUS':([10,16,22,25,26,27,28,33,39,40,49,50,56,59,71,73,74,80,82,104,111,],[40,-65,-57,-66,-67,-68,-69,-56,-63,-64,40,-65,40,-65,40,40,-70,40,-65,40,40,]),'INT':([15,77,128,],[42,42,42,]),'BOOL':([15,77,128,],[43,43,43,]),'STR':([15,77,128,],[44,44,44,]),'ASSIGN':([16,54,58,59,],[45,78,45,45,]),'DOT':([16,59,82,],[46,46,46,]),'LSPAREN':([16,59,82,],[47,47,47,]),'TRY':([19,],[51,]),'RPAREN':([22,25,26,27,28,33,39,40,46,49,50,56,62,64,66,67,68,70,72,74,76,77,79,80,81,82,83,87,98,100,101,103,104,105,106,107,108,111,115,116,118,119,120,121,127,129,131,136,141,144,145,],[-57,-66,-67,-68,-69,-56,-63,-64,-75,74,-65,-55,-27,-30,-32,-33,-34,-36,88,-70,97,-75,102,-73,-74,-65,-75,-28,114,-45,-75,117,-75,-75,-26,120,121,-48,-75,130,-24,-25,-29,-31,-44,-47,136,-35,-75,-46,147,]),'RSPAREN':([22,25,26,27,28,33,39,40,50,56,71,74,],[-57,-66,-67,-68,-69,-56,-63,-64,-65,-55,87,-70,]),'EQEQ':([22,25,26,27,28,33,39,40,50,56,73,74,],[-57,-66,-67,-68,-69,-56,-63,-64,-65,-55,90,-70,]),'NOTEQ':([22,25,26,27,28,33,39,40,50,56,73,74,],[-57,-66,-67,-68,-69,-56,-63,-64,-65,-55,91,-70,]),'LT':([22,25,26,27,28,33,39,40,50,56,73,74,],[-57,-66,-67,-68,-69,-56,-63,-64,-65,-55,92,-70,]),'GT':([22,25,26,27,28,33,39,40,50,56,73,74,],[-57,-66,-67,-68,-69,-56,-63,-64,-65,-55,93,-70,]),'LTEQ':([22,25,26,27,28,33,39,40,50,56,73,74,],[-57,-66,-67,-68,-69,-56,-63,-64,-65,-55,94,-70,]),'GTEQ':([22,25,26,27,28,33,39,40,50,56,73,74,],[-57,-66,-67,-68,-69,-56,-63,-64,-65,-55,95,-70,]),'COMMA':([22,25,26,27,28,33,39,40,50,56,74,83,101,104,105,109,115,140,141,],[-57,-66,-67,-68,-69,-56,-63,-64,-65,-55,-70,105,105,105,105,122,128,105,128,]),'CON':([46,],[63,]),'FRONT':([46,],[64,]),'ADD':([46,],[65,]),'REAR':([46,],[66,]),'SIZE':([46,],[67,]),'DELETE':([46,],[68,]),'SUBSTR':([46,],[69,]),'ELIF':([132,],[138,]),'ELSE':([151,],[153,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statement_list':([0,51,96,110,113,126,149,155,],[2,75,112,123,125,134,150,156,]),'empty':([0,46,51,77,83,96,101,104,105,110,113,115,126,132,140,141,149,151,155,],[3,70,3,100,106,3,106,106,106,3,3,129,3,139,106,129,3,154,3,]),'statement':([2,45,75,112,123,125,134,150,156,],[4,61,4,4,4,4,4,4,4,]),'declaration':([2,45,75,112,123,125,134,150,156,],[5,5,5,5,5,5,5,5,5,]),'assignment':([2,41,45,75,112,123,125,134,150,156,],[6,57,6,6,6,6,6,6,6,6,]),'if_stmnt':([2,45,75,112,123,125,134,150,156,],[7,7,7,7,7,7,7,7,7,]),'while_stmt':([2,45,75,112,123,125,134,150,156,],[8,8,8,8,8,8,8,8,8,]),'function_call':([2,45,75,112,123,125,134,150,156,],[9,9,9,9,9,9,9,9,9,]),'expression':([2,18,32,45,47,48,52,55,75,83,89,101,104,105,112,123,125,134,140,142,150,156,],[10,49,56,10,71,73,73,80,10,104,111,104,104,104,10,10,10,10,104,73,10,10,]),'compound_types':([2,45,75,112,123,125,134,150,156,],[11,11,11,11,11,11,11,11,11,]),'compound_type_access':([2,45,55,75,112,123,125,134,150,156,],[12,12,81,12,12,12,12,12,12,12,]),'try_except':([2,45,75,112,123,125,134,150,156,],[13,13,13,13,13,13,13,13,13,]),'print':([2,45,75,112,123,125,134,150,156,],[14,14,14,14,14,14,14,14,14,]),'factor':([2,18,32,45,47,48,52,55,75,83,84,85,86,89,101,104,105,112,122,123,125,134,140,142,150,156,],[22,22,22,22,22,22,22,22,22,22,107,108,109,22,22,22,22,22,131,22,22,22,22,22,22,22,]),'A':([2,45,75,112,123,125,134,150,156,],[23,23,23,23,23,23,23,23,23,]),'binary_operator':([10,49,56,71,73,80,104,111,],[32,32,32,32,32,32,32,32,]),'unary_operator':([10,49,56,71,73,80,104,111,],[33,33,33,33,33,33,33,33,]),'type':([15,77,128,],[41,99,135,]),'L':([45,],[60,]),'F':([46,],[62,]),'condition':([48,52,142,],[72,76,145,]),'y':([55,],[79,]),'comparison_operator':([73,],[89,]),'parameter_list':([77,],[98,]),'data':([83,101,104,105,140,],[103,116,118,119,143,]),'optional_parameter_list':([115,141,],[127,144,]),'T':([132,],[137,]),'K':([151,],[152,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statement_list','start',1,'p_start','my_parser.py',159),
  ('statement_list -> statement_list statement SEMICOLON','statement_list',3,'p_statement_list','my_parser.py',164),
  ('statement_list -> empty','statement_list',1,'p_statement_list','my_parser.py',165),
  ('statement -> declaration','statement',1,'p_statement','my_parser.py',173),
  ('statement -> assignment','statement',1,'p_statement','my_parser.py',174),
  ('statement -> if_stmnt','statement',1,'p_statement','my_parser.py',175),
  ('statement -> while_stmt','statement',1,'p_statement','my_parser.py',176),
  ('statement -> function_call','statement',1,'p_statement','my_parser.py',177),
  ('statement -> expression','statement',1,'p_statement','my_parser.py',178),
  ('statement -> compound_types','statement',1,'p_statement','my_parser.py',179),
  ('statement -> compound_type_access','statement',1,'p_statement','my_parser.py',180),
  ('statement -> try_except','statement',1,'p_statement','my_parser.py',181),
  ('statement -> print','statement',1,'p_statement','my_parser.py',182),
  ('declaration -> VAR type assignment','declaration',3,'p_declaration','my_parser.py',187),
  ('assignment -> ID ASSIGN L','assignment',3,'p_assignment','my_parser.py',192),
  ('L -> statement','L',1,'p_L','my_parser.py',196),
  ('L -> ID LPAREN data RPAREN','L',4,'p_L','my_parser.py',197),
  ('type -> INT','type',1,'p_type','my_parser.py',204),
  ('type -> BOOL','type',1,'p_type','my_parser.py',205),
  ('type -> STR','type',1,'p_type','my_parser.py',206),
  ('compound_types -> A ID ASSIGN LPAREN data RPAREN','compound_types',6,'p_compound_types','my_parser.py',211),
  ('A -> TUPLE','A',1,'p_A','my_parser.py',216),
  ('A -> LIST','A',1,'p_A','my_parser.py',217),
  ('data -> expression data','data',2,'p_data','my_parser.py',221),
  ('data -> COMMA data','data',2,'p_data','my_parser.py',222),
  ('data -> empty','data',1,'p_data','my_parser.py',223),
  ('compound_type_access -> ID DOT F','compound_type_access',3,'p_compound_type_access','my_parser.py',229),
  ('compound_type_access -> ID LSPAREN expression RSPAREN','compound_type_access',4,'p_compound_type_access','my_parser.py',230),
  ('F -> CON LPAREN factor RPAREN','F',4,'p_F','my_parser.py',239),
  ('F -> FRONT','F',1,'p_F','my_parser.py',240),
  ('F -> ADD LPAREN factor RPAREN','F',4,'p_F','my_parser.py',241),
  ('F -> REAR','F',1,'p_F','my_parser.py',242),
  ('F -> SIZE','F',1,'p_F','my_parser.py',243),
  ('F -> DELETE','F',1,'p_F','my_parser.py',244),
  ('F -> SUBSTR LPAREN factor COMMA factor RPAREN','F',6,'p_F','my_parser.py',245),
  ('F -> empty','F',1,'p_F','my_parser.py',246),
  ('if_stmnt -> IF LPAREN condition RPAREN BEGIN statement_list END T','if_stmnt',8,'p_if_stmnt','my_parser.py',257),
  ('T -> ELIF LPAREN condition RPAREN BEGIN statement_list END K','T',8,'p_T','my_parser.py',261),
  ('T -> empty','T',1,'p_T','my_parser.py',262),
  ('K -> ELSE BEGIN statement_list END','K',4,'p_K','my_parser.py',269),
  ('K -> empty','K',1,'p_K','my_parser.py',270),
  ('while_stmt -> WHILE LPAREN condition RPAREN BEGIN statement_list END','while_stmt',7,'p_while_stmt','my_parser.py',277),
  ('function_call -> FUNC ID LPAREN parameter_list RPAREN BEGIN statement_list RETURN data SEMICOLON END','function_call',11,'p_function_call','my_parser.py',281),
  ('parameter_list -> type ID optional_parameter_list','parameter_list',3,'p_parameter_list','my_parser.py',285),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','my_parser.py',286),
  ('optional_parameter_list -> COMMA type ID optional_parameter_list','optional_parameter_list',4,'p_optional_parameter_list','my_parser.py',293),
  ('optional_parameter_list -> empty','optional_parameter_list',1,'p_optional_parameter_list','my_parser.py',294),
  ('condition -> expression comparison_operator expression','condition',3,'p_condition','my_parser.py',301),
  ('comparison_operator -> EQEQ','comparison_operator',1,'p_comparison_operator','my_parser.py',305),
  ('comparison_operator -> NOTEQ','comparison_operator',1,'p_comparison_operator','my_parser.py',306),
  ('comparison_operator -> LT','comparison_operator',1,'p_comparison_operator','my_parser.py',307),
  ('comparison_operator -> GT','comparison_operator',1,'p_comparison_operator','my_parser.py',308),
  ('comparison_operator -> LTEQ','comparison_operator',1,'p_comparison_operator','my_parser.py',309),
  ('comparison_operator -> GTEQ','comparison_operator',1,'p_comparison_operator','my_parser.py',310),
  ('expression -> expression binary_operator expression','expression',3,'p_expression','my_parser.py',314),
  ('expression -> expression unary_operator','expression',2,'p_expression','my_parser.py',315),
  ('expression -> factor','expression',1,'p_expression','my_parser.py',316),
  ('binary_operator -> MINUS','binary_operator',1,'p_binary_operator','my_parser.py',326),
  ('binary_operator -> MUL','binary_operator',1,'p_binary_operator','my_parser.py',327),
  ('binary_operator -> PLUS','binary_operator',1,'p_binary_operator','my_parser.py',328),
  ('binary_operator -> DIV','binary_operator',1,'p_binary_operator','my_parser.py',329),
  ('binary_operator -> REM','binary_operator',1,'p_binary_operator','my_parser.py',330),
  ('unary_operator -> PLUSPLUS','unary_operator',1,'p_unary_operator','my_parser.py',334),
  ('unary_operator -> MINUSMINUS','unary_operator',1,'p_unary_operator','my_parser.py',335),
  ('factor -> ID','factor',1,'p_factor','my_parser.py',339),
  ('factor -> NUMBER','factor',1,'p_factor','my_parser.py',340),
  ('factor -> STRING','factor',1,'p_factor','my_parser.py',341),
  ('factor -> TRUE','factor',1,'p_factor','my_parser.py',342),
  ('factor -> FALSE','factor',1,'p_factor','my_parser.py',343),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','my_parser.py',344),
  ('try_except -> BEGIN TRY statement_list EXCEPT statement_list END','try_except',6,'p_try_except','my_parser.py',351),
  ('print -> ZOUT LPAREN y RPAREN','print',4,'p_print','my_parser.py',355),
  ('y -> expression','y',1,'p_y','my_parser.py',359),
  ('y -> compound_type_access','y',1,'p_y','my_parser.py',360),
  ('empty -> <empty>','empty',0,'p_empty','my_parser.py',364),
]
