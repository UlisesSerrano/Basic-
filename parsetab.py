
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COMA CTE_BOOLEAN CTE_CHAR CTE_F CTE_I CTE_STRING DIFERENT DIV DO ELSE EQ EQUAL FLOAT FOR FUNC GREATERTHAN GREATERTHANEQ ID IF INT LESSTHAN LESSTHANEQ L_B L_P L_SB MAIN MINUS MOD MULT NOT OR PLUS PRINT PROGRAM READ RETURN R_B R_P R_SB SEMICOLON TO VAR VOID WHILEprogram : PROGRAM ID SEMICOLON g_var funcs mainmain : MAIN L_P params R_P var_declaration L_B statements R_Bg_var : var_declaration \n            | emptyfuncs : function funcs\n            | emptyvar_declaration : VAR var1\n                        | emptyvar1 : var_type id var2 SEMICOLON var4var2 : COMA id var3\n            | emptyvar3 : var2\n            | emptyvar4 : var1\n        | emptyid : ID id1id1 : L_SB expression R_SB id2\n        | emptyid2 : L_SB expression R_SB\n        | emptytype : INT \n            | FLOAT \n            | CHARvar_type : typefunction : func_type FUNC ID L_P params R_P var_declaration L_B statements R_Bfunc_type : VOID\n                | typeparams : var_type id params1\n            | emptyparams1 : COMA params\n                | emptystatements : statement statements\n                | emptystatement : assignation\n                | call_func\n                | return_func\n                | read\n                | write\n                | decision_statement\n                | repetition_statement\n                | expressionassignation : id EQUAL expression SEMICOLONargs : args1\n            | emptyargs1 : expression args2args2 : COMA args1\n            | emptycall_func :  ID L_P args R_P SEMICOLONreturn_func : RETURN L_P expression R_P SEMICOLONread : READ L_P read_args R_P SEMICOLONread_args : expression read_args1read_args1 : COMA expression read_args1\n                | emptywrite : PRINT L_P write_args R_P SEMICOLONwrite_args : write_args2 write_args1write_args1 : COMA write_args2 write_args1\n                    | emptywrite_args2 : expression\n                | CTE_STRINGdecision_statement : IF L_P expression R_P L_B statements R_B decision_statement1decision_statement1 : ELSE L_B statements R_B\n                            | emptyrepetition_statement : while_statement\n                            | for_statementfor_statement : FOR id EQUAL expression TO expression do_statementwhile_statement : WHILE L_P expression R_P do_statementdo_statement :  DO L_B statements R_Bexpression : texp op1texp : gexp op2gexp : nexp op3auxnexp : term op4auxterm : fact op5auxfact : ID fact1\n            | L_P expression R_P\n            | ctefact1 : L_P args R_P\n            | id1\n            | emptycte : CTE_I\n            | CTE_F\n            | CTE_CHARop1 : OR expression\n            | emptyop2 : AND texp\n            | emptyop3 : LESSTHAN\n            | LESSTHANEQ\xa0\n            | GREATERTHAN\n            | GREATERTHANEQ\n            | EQ\n            | DIFERENTop3aux : op3 gexp\n            | emptyop4 : PLUS\n            | MINUSop4aux : op4 nexp\n            | emptyop5 : MULT\n        | DIV\n        | MODop5aux : op5 term\n            | empty\n        empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,21,145,],[0,-1,-2,]),'ID':([2,15,16,17,19,20,24,30,33,36,42,43,44,45,46,47,48,49,50,51,52,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,100,101,102,103,104,105,106,107,112,113,117,119,122,124,125,126,127,128,129,130,131,133,138,139,141,142,143,147,148,149,150,151,152,153,154,155,169,171,172,176,180,185,186,187,189,191,192,194,198,200,202,203,205,206,207,209,],[3,-21,-22,-23,26,-24,28,26,47,26,-103,-103,-103,-103,-103,-103,47,-75,-79,-80,-81,-103,-68,47,-83,-69,47,-85,-70,47,-93,-86,-87,-88,-89,-90,-91,-71,47,-97,-94,-95,-72,47,-102,-98,-99,-100,-73,47,-77,-18,47,-17,-20,-82,-84,-92,-96,-101,-74,133,-76,47,133,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,26,133,-19,47,47,-77,-18,47,47,47,47,47,47,-42,-76,47,47,-48,-49,-50,-54,133,-66,47,133,-103,-65,-60,-62,-67,133,-61,]),'SEMICOLON':([3,25,26,29,31,32,34,40,42,43,44,45,46,47,49,50,51,52,59,60,61,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,117,143,158,172,173,174,178,],[4,-103,-103,39,-11,-16,-18,-103,-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-10,-12,-11,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,-76,-19,171,185,186,187,189,]),'VAR':([4,53,99,],[8,8,8,]),'VOID':([4,5,6,7,10,18,39,56,57,58,170,],[-103,13,-3,-4,13,-7,-103,-9,-14,-15,-25,]),'INT':([4,5,6,7,8,10,18,27,38,39,56,57,58,97,170,],[-103,15,-3,-4,15,15,-7,15,15,15,-9,-14,-15,15,-25,]),'FLOAT':([4,5,6,7,8,10,18,27,38,39,56,57,58,97,170,],[-103,16,-3,-4,16,16,-7,16,16,16,-9,-14,-15,16,-25,]),'CHAR':([4,5,6,7,8,10,18,27,38,39,56,57,58,97,170,],[-103,17,-3,-4,17,17,-7,17,17,17,-9,-14,-15,17,-25,]),'MAIN':([4,5,6,7,9,10,11,18,23,39,56,57,58,170,],[-103,-103,-3,-4,22,-103,-6,-7,-5,-103,-9,-14,-15,-25,]),'FUNC':([12,13,14,15,16,17,],[24,-26,-27,-21,-22,-23,]),'L_B':([18,39,53,56,57,58,94,95,99,115,182,193,204,],[-7,-103,-103,-9,-14,-15,113,-8,-103,142,191,198,207,]),'L_P':([22,28,33,42,43,44,45,46,47,48,49,50,51,52,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,100,101,102,103,104,105,106,107,112,113,117,119,122,124,125,126,127,128,129,130,131,133,134,135,136,137,138,139,140,142,143,147,148,149,150,151,152,153,154,155,169,171,172,176,180,185,186,187,189,191,192,194,198,200,202,203,205,206,207,209,],[27,38,48,-103,-103,-103,-103,-103,90,48,-75,-79,-80,-81,-103,-68,48,-83,-69,48,-85,-70,48,-93,-86,-87,-88,-89,-90,-91,-71,48,-97,-94,-95,-72,48,-102,-98,-99,-100,-73,48,-77,-18,48,-17,-20,-82,-84,-92,-96,-101,-74,48,-76,48,48,-34,-35,-36,-37,-38,-39,-40,-41,148,151,152,153,154,-63,-64,155,48,-19,48,48,-77,-18,48,48,48,48,48,48,-42,-76,48,48,-48,-49,-50,-54,48,-66,48,48,-103,-65,-60,-62,-67,48,-61,]),'COMA':([25,26,32,34,40,42,43,44,45,46,47,49,50,51,52,54,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,111,112,117,143,162,164,165,166,188,190,],[30,-103,-16,-18,30,-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,97,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,119,-74,-76,-19,176,180,-58,-59,176,180,]),'L_SB':([26,47,62,133,],[33,33,100,33,]),'R_P':([26,27,32,34,35,37,38,42,43,44,45,46,47,49,50,51,52,54,55,62,63,65,66,68,69,71,78,80,83,85,89,90,91,92,93,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,114,117,118,120,143,144,148,159,160,161,162,163,164,165,166,167,168,175,177,179,181,188,190,195,196,],[-103,-103,-16,-18,53,-29,-103,-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,99,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-103,-77,-18,112,-28,-103,-31,-17,-20,-82,-84,-92,-96,-101,117,-43,-44,-103,-74,-30,-76,-45,-47,-19,-46,-103,172,173,174,-103,178,-103,-58,-59,182,183,-51,-53,-55,-57,-103,-103,-52,-56,]),'EQUAL':([26,32,34,62,101,102,132,133,143,149,150,156,],[-103,-16,-18,-103,-17,-20,147,-103,-19,-16,-18,169,]),'CTE_I':([33,42,43,44,45,46,47,48,49,50,51,52,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,100,101,102,103,104,105,106,107,112,113,117,119,122,124,125,126,127,128,129,130,131,133,138,139,142,143,147,148,149,150,151,152,153,154,155,169,171,172,176,180,185,186,187,189,191,192,194,198,200,202,203,205,206,207,209,],[50,-103,-103,-103,-103,-103,-103,50,-75,-79,-80,-81,-103,-68,50,-83,-69,50,-85,-70,50,-93,-86,-87,-88,-89,-90,-91,-71,50,-97,-94,-95,-72,50,-102,-98,-99,-100,-73,50,-77,-18,50,-17,-20,-82,-84,-92,-96,-101,-74,50,-76,50,50,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,50,-19,50,50,-77,-18,50,50,50,50,50,50,-42,-76,50,50,-48,-49,-50,-54,50,-66,50,50,-103,-65,-60,-62,-67,50,-61,]),'CTE_F':([33,42,43,44,45,46,47,48,49,50,51,52,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,100,101,102,103,104,105,106,107,112,113,117,119,122,124,125,126,127,128,129,130,131,133,138,139,142,143,147,148,149,150,151,152,153,154,155,169,171,172,176,180,185,186,187,189,191,192,194,198,200,202,203,205,206,207,209,],[51,-103,-103,-103,-103,-103,-103,51,-75,-79,-80,-81,-103,-68,51,-83,-69,51,-85,-70,51,-93,-86,-87,-88,-89,-90,-91,-71,51,-97,-94,-95,-72,51,-102,-98,-99,-100,-73,51,-77,-18,51,-17,-20,-82,-84,-92,-96,-101,-74,51,-76,51,51,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,51,-19,51,51,-77,-18,51,51,51,51,51,51,-42,-76,51,51,-48,-49,-50,-54,51,-66,51,51,-103,-65,-60,-62,-67,51,-61,]),'CTE_CHAR':([33,42,43,44,45,46,47,48,49,50,51,52,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,100,101,102,103,104,105,106,107,112,113,117,119,122,124,125,126,127,128,129,130,131,133,138,139,142,143,147,148,149,150,151,152,153,154,155,169,171,172,176,180,185,186,187,189,191,192,194,198,200,202,203,205,206,207,209,],[52,-103,-103,-103,-103,-103,-103,52,-75,-79,-80,-81,-103,-68,52,-83,-69,52,-85,-70,52,-93,-86,-87,-88,-89,-90,-91,-71,52,-97,-94,-95,-72,52,-102,-98,-99,-100,-73,52,-77,-18,52,-17,-20,-82,-84,-92,-96,-101,-74,52,-76,52,52,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,52,-19,52,52,-77,-18,52,52,52,52,52,52,-42,-76,52,52,-48,-49,-50,-54,52,-66,52,52,-103,-65,-60,-62,-67,52,-61,]),'R_SB':([41,42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,116,117,143,],[62,-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,143,-76,-19,]),'OR':([42,43,44,45,46,47,49,50,51,52,62,66,68,69,71,78,80,83,85,89,91,92,101,102,104,105,106,107,112,117,133,143,149,150,172,],[64,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-84,-92,-96,-101,-74,-76,-103,-19,-77,-18,-76,]),'RETURN':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,113,117,122,124,125,126,127,128,129,130,131,133,138,139,142,143,149,150,171,172,185,186,187,189,191,192,198,200,202,203,205,206,207,209,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,134,-76,134,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,134,-19,-77,-18,-42,-76,-48,-49,-50,-54,134,-66,134,-103,-65,-60,-62,-67,134,-61,]),'READ':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,113,117,122,124,125,126,127,128,129,130,131,133,138,139,142,143,149,150,171,172,185,186,187,189,191,192,198,200,202,203,205,206,207,209,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,135,-76,135,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,135,-19,-77,-18,-42,-76,-48,-49,-50,-54,135,-66,135,-103,-65,-60,-62,-67,135,-61,]),'PRINT':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,113,117,122,124,125,126,127,128,129,130,131,133,138,139,142,143,149,150,171,172,185,186,187,189,191,192,198,200,202,203,205,206,207,209,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,136,-76,136,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,136,-19,-77,-18,-42,-76,-48,-49,-50,-54,136,-66,136,-103,-65,-60,-62,-67,136,-61,]),'IF':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,113,117,122,124,125,126,127,128,129,130,131,133,138,139,142,143,149,150,171,172,185,186,187,189,191,192,198,200,202,203,205,206,207,209,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,137,-76,137,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,137,-19,-77,-18,-42,-76,-48,-49,-50,-54,137,-66,137,-103,-65,-60,-62,-67,137,-61,]),'WHILE':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,113,117,122,124,125,126,127,128,129,130,131,133,138,139,142,143,149,150,171,172,185,186,187,189,191,192,198,200,202,203,205,206,207,209,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,140,-76,140,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,140,-19,-77,-18,-42,-76,-48,-49,-50,-54,140,-66,140,-103,-65,-60,-62,-67,140,-61,]),'FOR':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,113,117,122,124,125,126,127,128,129,130,131,133,138,139,142,143,149,150,171,172,185,186,187,189,191,192,198,200,202,203,205,206,207,209,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,141,-76,141,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,141,-19,-77,-18,-42,-76,-48,-49,-50,-54,141,-66,141,-103,-65,-60,-62,-67,141,-61,]),'R_B':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,113,117,121,122,123,124,125,126,127,128,129,130,131,133,138,139,142,143,146,149,150,157,171,172,185,186,187,189,191,192,197,198,200,201,202,203,205,206,207,208,209,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,-103,-76,145,-103,-33,-34,-35,-36,-37,-38,-39,-40,-41,-103,-63,-64,-103,-19,-32,-77,-18,170,-42,-76,-48,-49,-50,-54,-103,-66,200,-103,-103,206,-65,-60,-62,-67,-103,209,-61,]),'TO':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,117,143,184,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,-76,-19,194,]),'DO':([42,43,44,45,46,47,49,50,51,52,62,63,65,66,68,69,71,78,80,83,85,89,91,92,101,102,103,104,105,106,107,112,117,143,183,199,],[-103,-103,-103,-103,-103,-103,-75,-79,-80,-81,-103,-68,-83,-69,-85,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-82,-84,-92,-96,-101,-74,-76,-19,193,193,]),'AND':([43,44,45,46,47,49,50,51,52,62,69,71,78,80,83,85,89,91,92,101,102,105,106,107,112,117,133,143,149,150,172,],[67,-103,-103,-103,-103,-75,-79,-80,-81,-103,-70,-93,-71,-97,-72,-102,-73,-77,-18,-17,-20,-92,-96,-101,-74,-76,-103,-19,-77,-18,-76,]),'LESSTHAN':([44,45,46,47,49,50,51,52,62,78,80,83,85,89,91,92,101,102,106,107,112,117,133,143,149,150,172,],[72,-103,-103,-103,-75,-79,-80,-81,-103,-71,-97,-72,-102,-73,-77,-18,-17,-20,-96,-101,-74,-76,-103,-19,-77,-18,-76,]),'LESSTHANEQ':([44,45,46,47,49,50,51,52,62,78,80,83,85,89,91,92,101,102,106,107,112,117,133,143,149,150,172,],[73,-103,-103,-103,-75,-79,-80,-81,-103,-71,-97,-72,-102,-73,-77,-18,-17,-20,-96,-101,-74,-76,-103,-19,-77,-18,-76,]),'GREATERTHAN':([44,45,46,47,49,50,51,52,62,78,80,83,85,89,91,92,101,102,106,107,112,117,133,143,149,150,172,],[74,-103,-103,-103,-75,-79,-80,-81,-103,-71,-97,-72,-102,-73,-77,-18,-17,-20,-96,-101,-74,-76,-103,-19,-77,-18,-76,]),'GREATERTHANEQ':([44,45,46,47,49,50,51,52,62,78,80,83,85,89,91,92,101,102,106,107,112,117,133,143,149,150,172,],[75,-103,-103,-103,-75,-79,-80,-81,-103,-71,-97,-72,-102,-73,-77,-18,-17,-20,-96,-101,-74,-76,-103,-19,-77,-18,-76,]),'EQ':([44,45,46,47,49,50,51,52,62,78,80,83,85,89,91,92,101,102,106,107,112,117,133,143,149,150,172,],[76,-103,-103,-103,-75,-79,-80,-81,-103,-71,-97,-72,-102,-73,-77,-18,-17,-20,-96,-101,-74,-76,-103,-19,-77,-18,-76,]),'DIFERENT':([44,45,46,47,49,50,51,52,62,78,80,83,85,89,91,92,101,102,106,107,112,117,133,143,149,150,172,],[77,-103,-103,-103,-75,-79,-80,-81,-103,-71,-97,-72,-102,-73,-77,-18,-17,-20,-96,-101,-74,-76,-103,-19,-77,-18,-76,]),'PLUS':([45,46,47,49,50,51,52,62,83,85,89,91,92,101,102,107,112,117,133,143,149,150,172,],[81,-103,-103,-75,-79,-80,-81,-103,-72,-102,-73,-77,-18,-17,-20,-101,-74,-76,-103,-19,-77,-18,-76,]),'MINUS':([45,46,47,49,50,51,52,62,83,85,89,91,92,101,102,107,112,117,133,143,149,150,172,],[82,-103,-103,-75,-79,-80,-81,-103,-72,-102,-73,-77,-18,-17,-20,-101,-74,-76,-103,-19,-77,-18,-76,]),'MULT':([46,47,49,50,51,52,62,89,91,92,101,102,112,117,133,143,149,150,172,],[86,-103,-75,-79,-80,-81,-103,-73,-77,-18,-17,-20,-74,-76,-103,-19,-77,-18,-76,]),'DIV':([46,47,49,50,51,52,62,89,91,92,101,102,112,117,133,143,149,150,172,],[87,-103,-75,-79,-80,-81,-103,-73,-77,-18,-17,-20,-74,-76,-103,-19,-77,-18,-76,]),'MOD':([46,47,49,50,51,52,62,89,91,92,101,102,112,117,133,143,149,150,172,],[88,-103,-75,-79,-80,-81,-103,-73,-77,-18,-17,-20,-74,-76,-103,-19,-77,-18,-76,]),'CTE_STRING':([153,180,],[166,166,]),'ELSE':([200,],[204,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'g_var':([4,],[5,]),'var_declaration':([4,53,99,],[6,94,115,]),'empty':([4,5,10,25,26,27,38,39,40,42,43,44,45,46,47,53,54,62,90,97,99,111,113,122,133,142,148,162,164,188,190,191,198,200,207,],[7,11,11,31,34,37,37,58,61,65,68,71,80,85,92,95,98,102,110,37,95,120,123,123,150,123,110,177,181,177,181,123,123,205,123,]),'funcs':([5,10,],[9,23,]),'function':([5,10,],[10,10,]),'func_type':([5,10,],[12,12,]),'type':([5,8,10,27,38,39,97,],[14,20,14,20,20,20,20,]),'var1':([8,39,],[18,57,]),'var_type':([8,27,38,39,97,],[19,36,36,19,36,]),'main':([9,],[21,]),'id':([19,30,36,113,122,141,142,191,198,207,],[25,40,54,132,132,156,132,132,132,132,]),'var2':([25,40,],[29,60,]),'id1':([26,47,133,],[32,91,149,]),'params':([27,38,97,],[35,55,114,]),'expression':([33,48,64,90,100,113,119,122,142,147,148,151,152,153,154,155,169,176,180,191,194,198,207,],[41,93,103,111,116,131,111,131,131,158,111,160,162,165,167,168,184,188,165,131,199,131,131,]),'texp':([33,48,64,67,90,100,113,119,122,142,147,148,151,152,153,154,155,169,176,180,191,194,198,207,],[42,42,42,104,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'gexp':([33,48,64,67,70,90,100,113,119,122,142,147,148,151,152,153,154,155,169,176,180,191,194,198,207,],[43,43,43,43,105,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'nexp':([33,48,64,67,70,79,90,100,113,119,122,142,147,148,151,152,153,154,155,169,176,180,191,194,198,207,],[44,44,44,44,44,106,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'term':([33,48,64,67,70,79,84,90,100,113,119,122,142,147,148,151,152,153,154,155,169,176,180,191,194,198,207,],[45,45,45,45,45,45,107,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'fact':([33,48,64,67,70,79,84,90,100,113,119,122,142,147,148,151,152,153,154,155,169,176,180,191,194,198,207,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'cte':([33,48,64,67,70,79,84,90,100,113,119,122,142,147,148,151,152,153,154,155,169,176,180,191,194,198,207,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'var4':([39,],[56,]),'var3':([40,],[59,]),'op1':([42,],[63,]),'op2':([43,],[66,]),'op3aux':([44,],[69,]),'op3':([44,],[70,]),'op4aux':([45,],[78,]),'op4':([45,],[79,]),'op5aux':([46,],[83,]),'op5':([46,],[84,]),'fact1':([47,133,],[89,89,]),'params1':([54,],[96,]),'id2':([62,],[101,]),'args':([90,148,],[108,159,]),'args1':([90,119,148,],[109,144,109,]),'args2':([111,],[118,]),'statements':([113,122,142,191,198,207,],[121,146,157,197,201,208,]),'statement':([113,122,142,191,198,207,],[122,122,122,122,122,122,]),'assignation':([113,122,142,191,198,207,],[124,124,124,124,124,124,]),'call_func':([113,122,142,191,198,207,],[125,125,125,125,125,125,]),'return_func':([113,122,142,191,198,207,],[126,126,126,126,126,126,]),'read':([113,122,142,191,198,207,],[127,127,127,127,127,127,]),'write':([113,122,142,191,198,207,],[128,128,128,128,128,128,]),'decision_statement':([113,122,142,191,198,207,],[129,129,129,129,129,129,]),'repetition_statement':([113,122,142,191,198,207,],[130,130,130,130,130,130,]),'while_statement':([113,122,142,191,198,207,],[138,138,138,138,138,138,]),'for_statement':([113,122,142,191,198,207,],[139,139,139,139,139,139,]),'read_args':([152,],[161,]),'write_args':([153,],[163,]),'write_args2':([153,180,],[164,190,]),'read_args1':([162,188,],[175,195,]),'write_args1':([164,190,],[179,196,]),'do_statement':([183,199,],[192,202,]),'decision_statement1':([200,],[203,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON g_var funcs main','program',6,'p_program','parser-lexer.py',122),
  ('main -> MAIN L_P params R_P var_declaration L_B statements R_B','main',8,'p_main','parser-lexer.py',127),
  ('g_var -> var_declaration','g_var',1,'p_g_var','parser-lexer.py',132),
  ('g_var -> empty','g_var',1,'p_g_var','parser-lexer.py',133),
  ('funcs -> function funcs','funcs',2,'p_funcs','parser-lexer.py',138),
  ('funcs -> empty','funcs',1,'p_funcs','parser-lexer.py',139),
  ('var_declaration -> VAR var1','var_declaration',2,'p_var_declaration','parser-lexer.py',144),
  ('var_declaration -> empty','var_declaration',1,'p_var_declaration','parser-lexer.py',145),
  ('var1 -> var_type id var2 SEMICOLON var4','var1',5,'p_var1','parser-lexer.py',150),
  ('var2 -> COMA id var3','var2',3,'p_var2','parser-lexer.py',155),
  ('var2 -> empty','var2',1,'p_var2','parser-lexer.py',156),
  ('var3 -> var2','var3',1,'p_var3','parser-lexer.py',161),
  ('var3 -> empty','var3',1,'p_var3','parser-lexer.py',162),
  ('var4 -> var1','var4',1,'p_var4','parser-lexer.py',167),
  ('var4 -> empty','var4',1,'p_var4','parser-lexer.py',168),
  ('id -> ID id1','id',2,'p_id','parser-lexer.py',173),
  ('id1 -> L_SB expression R_SB id2','id1',4,'p_id1','parser-lexer.py',178),
  ('id1 -> empty','id1',1,'p_id1','parser-lexer.py',179),
  ('id2 -> L_SB expression R_SB','id2',3,'p_id2','parser-lexer.py',184),
  ('id2 -> empty','id2',1,'p_id2','parser-lexer.py',185),
  ('type -> INT','type',1,'p_type','parser-lexer.py',190),
  ('type -> FLOAT','type',1,'p_type','parser-lexer.py',191),
  ('type -> CHAR','type',1,'p_type','parser-lexer.py',192),
  ('var_type -> type','var_type',1,'p_var_type','parser-lexer.py',197),
  ('function -> func_type FUNC ID L_P params R_P var_declaration L_B statements R_B','function',10,'p_function','parser-lexer.py',202),
  ('func_type -> VOID','func_type',1,'p_func_type','parser-lexer.py',207),
  ('func_type -> type','func_type',1,'p_func_type','parser-lexer.py',208),
  ('params -> var_type id params1','params',3,'p_params','parser-lexer.py',213),
  ('params -> empty','params',1,'p_params','parser-lexer.py',214),
  ('params1 -> COMA params','params1',2,'p_params1','parser-lexer.py',219),
  ('params1 -> empty','params1',1,'p_params1','parser-lexer.py',220),
  ('statements -> statement statements','statements',2,'p_statements','parser-lexer.py',225),
  ('statements -> empty','statements',1,'p_statements','parser-lexer.py',226),
  ('statement -> assignation','statement',1,'p_statement','parser-lexer.py',231),
  ('statement -> call_func','statement',1,'p_statement','parser-lexer.py',232),
  ('statement -> return_func','statement',1,'p_statement','parser-lexer.py',233),
  ('statement -> read','statement',1,'p_statement','parser-lexer.py',234),
  ('statement -> write','statement',1,'p_statement','parser-lexer.py',235),
  ('statement -> decision_statement','statement',1,'p_statement','parser-lexer.py',236),
  ('statement -> repetition_statement','statement',1,'p_statement','parser-lexer.py',237),
  ('statement -> expression','statement',1,'p_statement','parser-lexer.py',238),
  ('assignation -> id EQUAL expression SEMICOLON','assignation',4,'p_assignation','parser-lexer.py',243),
  ('args -> args1','args',1,'p_args','parser-lexer.py',248),
  ('args -> empty','args',1,'p_args','parser-lexer.py',249),
  ('args1 -> expression args2','args1',2,'p_args1','parser-lexer.py',254),
  ('args2 -> COMA args1','args2',2,'p_args2','parser-lexer.py',259),
  ('args2 -> empty','args2',1,'p_args2','parser-lexer.py',260),
  ('call_func -> ID L_P args R_P SEMICOLON','call_func',5,'p_call_func','parser-lexer.py',265),
  ('return_func -> RETURN L_P expression R_P SEMICOLON','return_func',5,'p_return_func','parser-lexer.py',270),
  ('read -> READ L_P read_args R_P SEMICOLON','read',5,'p_read','parser-lexer.py',275),
  ('read_args -> expression read_args1','read_args',2,'p_read_args','parser-lexer.py',280),
  ('read_args1 -> COMA expression read_args1','read_args1',3,'p_read_args1','parser-lexer.py',285),
  ('read_args1 -> empty','read_args1',1,'p_read_args1','parser-lexer.py',286),
  ('write -> PRINT L_P write_args R_P SEMICOLON','write',5,'p_write','parser-lexer.py',291),
  ('write_args -> write_args2 write_args1','write_args',2,'p_write_args','parser-lexer.py',296),
  ('write_args1 -> COMA write_args2 write_args1','write_args1',3,'p_write_args1','parser-lexer.py',301),
  ('write_args1 -> empty','write_args1',1,'p_write_args1','parser-lexer.py',302),
  ('write_args2 -> expression','write_args2',1,'p_write_args2','parser-lexer.py',307),
  ('write_args2 -> CTE_STRING','write_args2',1,'p_write_args2','parser-lexer.py',308),
  ('decision_statement -> IF L_P expression R_P L_B statements R_B decision_statement1','decision_statement',8,'p_decision_statement','parser-lexer.py',313),
  ('decision_statement1 -> ELSE L_B statements R_B','decision_statement1',4,'p_decision_statement1','parser-lexer.py',318),
  ('decision_statement1 -> empty','decision_statement1',1,'p_decision_statement1','parser-lexer.py',319),
  ('repetition_statement -> while_statement','repetition_statement',1,'p_repetition_statement','parser-lexer.py',324),
  ('repetition_statement -> for_statement','repetition_statement',1,'p_repetition_statement','parser-lexer.py',325),
  ('for_statement -> FOR id EQUAL expression TO expression do_statement','for_statement',7,'p_for_statement','parser-lexer.py',330),
  ('while_statement -> WHILE L_P expression R_P do_statement','while_statement',5,'p_while_statement','parser-lexer.py',335),
  ('do_statement -> DO L_B statements R_B','do_statement',4,'p_do_statement','parser-lexer.py',340),
  ('expression -> texp op1','expression',2,'p_expression','parser-lexer.py',345),
  ('texp -> gexp op2','texp',2,'p_texp','parser-lexer.py',350),
  ('gexp -> nexp op3aux','gexp',2,'p_gexp','parser-lexer.py',355),
  ('nexp -> term op4aux','nexp',2,'p_nexp','parser-lexer.py',360),
  ('term -> fact op5aux','term',2,'p_term','parser-lexer.py',365),
  ('fact -> ID fact1','fact',2,'p_fact','parser-lexer.py',370),
  ('fact -> L_P expression R_P','fact',3,'p_fact','parser-lexer.py',371),
  ('fact -> cte','fact',1,'p_fact','parser-lexer.py',372),
  ('fact1 -> L_P args R_P','fact1',3,'p_fact1','parser-lexer.py',377),
  ('fact1 -> id1','fact1',1,'p_fact1','parser-lexer.py',378),
  ('fact1 -> empty','fact1',1,'p_fact1','parser-lexer.py',379),
  ('cte -> CTE_I','cte',1,'p_cte','parser-lexer.py',382),
  ('cte -> CTE_F','cte',1,'p_cte','parser-lexer.py',383),
  ('cte -> CTE_CHAR','cte',1,'p_cte','parser-lexer.py',384),
  ('op1 -> OR expression','op1',2,'p_op1','parser-lexer.py',388),
  ('op1 -> empty','op1',1,'p_op1','parser-lexer.py',389),
  ('op2 -> AND texp','op2',2,'p_op2','parser-lexer.py',394),
  ('op2 -> empty','op2',1,'p_op2','parser-lexer.py',395),
  ('op3 -> LESSTHAN','op3',1,'p_op3','parser-lexer.py',400),
  ('op3 -> LESSTHANEQ','op3',1,'p_op3','parser-lexer.py',401),
  ('op3 -> GREATERTHAN','op3',1,'p_op3','parser-lexer.py',402),
  ('op3 -> GREATERTHANEQ','op3',1,'p_op3','parser-lexer.py',403),
  ('op3 -> EQ','op3',1,'p_op3','parser-lexer.py',404),
  ('op3 -> DIFERENT','op3',1,'p_op3','parser-lexer.py',405),
  ('op3aux -> op3 gexp','op3aux',2,'p_op3aux','parser-lexer.py',409),
  ('op3aux -> empty','op3aux',1,'p_op3aux','parser-lexer.py',410),
  ('op4 -> PLUS','op4',1,'p_op4','parser-lexer.py',415),
  ('op4 -> MINUS','op4',1,'p_op4','parser-lexer.py',416),
  ('op4aux -> op4 nexp','op4aux',2,'p_op4aux','parser-lexer.py',421),
  ('op4aux -> empty','op4aux',1,'p_op4aux','parser-lexer.py',422),
  ('op5 -> MULT','op5',1,'p_op5','parser-lexer.py',427),
  ('op5 -> DIV','op5',1,'p_op5','parser-lexer.py',428),
  ('op5 -> MOD','op5',1,'p_op5','parser-lexer.py',429),
  ('op5aux -> op5 term','op5aux',2,'p_op5aux','parser-lexer.py',434),
  ('op5aux -> empty','op5aux',1,'p_op5aux','parser-lexer.py',435),
  ('empty -> <empty>','empty',0,'p_empty','parser-lexer.py',441),
]
