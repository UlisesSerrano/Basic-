
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COMA CTE_CHAR CTE_F CTE_I CTE_STRING DIFERENT DIV DO ELSE EQ EQUAL FLOAT FOR FUNC GREATERTHAN GREATERTHANEQ ID IF INT LESSTHAN LESSTHANEQ L_B L_P L_SB MAIN MINUS MOD MULT OR PLUS PRINT PROGRAM READ RETURN R_B R_P R_SB SEMICOLON TO VAR VOID WHILEprogram : PROGRAM ID main_quad SEMICOLON g_var funcs mainmain_quad : main : MAIN L_P params R_P var_declaration L_B main_start statements R_Bmain_start : type : INT\n            | FLOAT\n            | CHARg_var : var_declarationfuncs : function funcs\n            | emptyvar_declaration : VAR var1\n                        | emptyvar1 : var_type dec_id var2 SEMICOLON var4var2 : COMA dec_id var3\n            | emptyvar3 : var2var4 : var1\n            | emptydec_id : ID dec_id1dec_id1 : L_SB CTE_I R_SB dec_id2\n            | emptydec_id2 : L_SB CTE_I R_SB\n        | emptyid : ID id1id1 : L_SB expression R_SB id2\n            | emptyid2 : L_SB expression R_SB\n        | emptyvar_type : typefunction : FUNC func_type ID register_func L_P params R_P add_params var_declaration start_func L_B statements R_Bregister_func : add_params : start_func : func_type : VOID\n                | typeparams : var_type param_type dec_id params1\n            | emptyparam_type : params1 : COMA params\n                | emptystatements : statement statements\n                | emptystatement : assignation\n                | call_func\n                | return_func\n                | read\n                | write\n                | decision_statement\n                | repetition_statement\n                | expressionassignation : id id_quad EQUAL expression SEMICOLONargs : args1\n            | emptyargs1 : add_fake expression param_check remove_fake args2param_check : args2 : COMA next_arg args1\n            | emptynext_arg : call_func :  ID call_func_era L_P args R_P SEMICOLONcall_func_exp :  ID call_func_era L_P args R_Pcall_func_era : return_func : RETURN L_P expression R_P SEMICOLONread : READ L_P read_args R_P SEMICOLONread_args : add_fake expression remove_fake read_args1read_args1 : COMA add_fake expression remove_fake read_args1\n                | emptywrite : PRINT L_P write_args R_P SEMICOLONwrite_args : write_args2 write_args1write_args1 : COMA write_args2 write_args1\n                    | emptywrite_args2 : add_fake expression remove_fake\n                | CTE_STRING add_cte_stringdecision_statement : IF L_P expression R_P exp_type L_B statements R_B decision_statement1decision_statement1 : ELSE else_jump L_B statements R_B\n                            | emptyexp_type : else_jump : repetition_statement : while_statement\n                            | for_statementfor_statement : FOR id id_quad EQUAL expression for_id TO breadcrumb expression exp_type do_statementfor_id : breadcrumb : while_statement : WHILE L_P breadcrumb expression R_P exp_type do_statementdo_statement :  DO L_B statements R_Bexpression : texp generate_quad_1 op1texp : gexp generate_quad_2 op2gexp : mexp generate_quad_3 op3auxmexp : term generate_quad_4 op4auxterm : fact generate_quad_5 op5auxgenerate_quad_1 : generate_quad_2 : generate_quad_3 : generate_quad_4 : generate_quad_5 : fact : id id_quad\n            | call_func_exp\n            | L_P add_fake expression R_P remove_fake\n            | cteadd_fake : remove_fake : \n        id_quad :\n    cte : CTE_CHAR add_cte_char\n            | CTE_F add_cte_float\n            | CTE_I add_cte_int add_cte_int : add_cte_float : add_cte_char : add_cte_string : add_operator : op1 : OR add_operator expression\n            | emptyop2 : AND add_operator texp\n            | emptyop3 : LESSTHAN\n            | LESSTHANEQ\xa0\n            | GREATERTHAN\n            | GREATERTHANEQ\n            | EQ\n            | DIFERENTop3aux : op3 mexp\n            | emptyop4 : PLUS\n            | MINUSop4aux : op4 mexp\n            | emptyop5 : MULT\n        | DIV\n        | MODop5aux : op5 term\n            | empty\n        empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,20,102,],[0,-1,-3,]),'ID':([2,15,16,17,18,19,23,24,25,31,37,44,58,64,68,70,72,73,74,75,76,77,78,79,80,81,86,87,88,90,91,92,93,94,95,96,97,98,99,101,104,106,107,108,109,110,111,112,113,114,117,118,119,120,121,122,123,126,127,128,129,133,136,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,182,187,189,190,191,192,193,195,196,197,198,200,201,202,203,204,206,210,213,216,220,223,226,228,229,231,233,235,238,239,240,241,243,245,251,253,254,256,],[3,27,-29,-5,-6,-7,29,-34,-35,27,-38,27,-4,81,-99,81,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,116,-91,-92,-93,-94,-96,-98,-107,-106,-105,127,-95,-24,127,-26,127,-99,-99,127,-131,-82,-131,-131,-131,-131,-102,-103,-104,-101,-131,127,-99,127,127,-85,-109,-111,127,-86,-109,-113,-87,127,-121,-114,-115,-116,-117,-118,-119,-88,127,-125,-122,-123,-89,127,-130,-126,-127,-128,81,-100,-95,127,-131,-99,127,127,127,-120,-124,-129,-97,-99,-51,-60,127,-25,-28,-62,-63,-67,-110,-112,-59,-99,81,-60,-27,127,-83,-82,-58,-131,81,127,-99,-73,-75,-84,81,-80,-74,]),'SEMICOLON':([3,4,26,27,30,32,33,35,41,49,50,51,56,57,67,88,91,92,93,94,95,96,97,98,99,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,168,169,171,176,177,178,180,191,192,193,195,198,201,202,210,213,226,228,],[-2,5,-131,-131,40,-15,-19,-21,-131,-14,-16,-131,-20,-23,-22,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,-100,-95,197,-131,203,204,206,-120,-124,-129,-97,216,-25,-28,-110,-112,-60,-27,]),'VAR':([5,43,62,66,],[8,8,-32,8,]),'FUNC':([5,6,7,9,11,14,40,46,47,48,214,],[-131,13,-8,-12,13,-11,-131,-13,-17,-18,-30,]),'MAIN':([5,6,7,9,10,11,12,14,22,40,46,47,48,214,],[-131,-131,-8,-12,21,-131,-10,-11,-9,-131,-13,-17,-18,-30,]),'INT':([8,13,28,40,45,60,],[17,17,17,17,17,17,]),'FLOAT':([8,13,28,40,45,60,],[18,18,18,18,18,18,]),'CHAR':([8,13,28,40,45,60,],[19,19,19,19,19,19,]),'L_B':([9,14,40,43,46,47,48,52,62,66,100,124,186,209,232,244,250,],[-12,-11,-131,-131,-13,-17,-18,58,-32,-131,-33,167,-76,223,239,-77,253,]),'VOID':([13,],[24,]),'L_P':([21,29,39,58,64,68,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,101,104,105,106,107,108,109,110,111,112,113,114,117,118,119,120,121,122,123,126,127,128,129,133,136,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,175,176,182,187,189,190,191,192,193,195,196,197,198,200,201,202,203,204,206,210,213,216,220,223,226,228,229,231,233,235,238,239,240,241,243,245,251,253,254,256,],[28,-31,45,-4,68,-99,68,-43,-44,-45,-46,-47,-48,-49,-50,-101,-61,109,110,111,112,-78,-79,-90,114,-91,-92,-93,-94,-96,-98,-107,-106,-105,68,-95,129,-24,68,-26,68,-99,-99,68,-131,-82,-131,-131,-131,-131,-102,-103,-104,-101,-61,68,-99,68,68,-85,-109,-111,68,-86,-109,-113,-87,68,-121,-114,-115,-116,-117,-118,-119,-88,68,-125,-122,-123,-89,68,-130,-126,-127,-128,68,-100,-95,196,68,-131,-99,68,68,68,-120,-124,-129,-97,-99,-51,-60,68,-25,-28,-62,-63,-67,-110,-112,-59,-99,68,-60,-27,68,-83,-82,-58,-131,68,68,-99,-73,-75,-84,68,-80,-74,]),'COMA':([26,27,33,35,41,51,53,56,57,67,88,91,92,93,94,95,96,97,98,99,106,108,113,117,118,119,120,121,122,123,126,127,135,137,139,141,144,146,147,149,156,158,161,163,168,169,176,179,184,185,191,192,193,195,199,201,202,205,207,208,210,213,217,226,227,228,237,242,],[31,-131,-19,-21,31,-131,60,-20,-23,-22,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,182,-108,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,-100,-95,-131,-100,-100,-72,-120,-124,-129,-97,-55,-25,-28,220,182,-71,-110,-112,-100,-60,235,-27,-100,220,]),'L_SB':([27,51,81,116,127,176,],[34,55,107,107,107,200,]),'R_P':([27,28,33,35,36,38,45,51,53,54,56,57,59,60,61,65,67,88,91,92,93,94,95,96,97,98,99,106,108,113,117,118,119,120,121,122,123,125,126,127,129,131,132,134,135,137,138,139,141,144,146,147,149,156,158,161,163,168,169,172,173,174,176,179,181,183,184,185,188,191,192,193,195,196,199,201,202,205,207,208,210,213,215,217,219,221,222,226,227,228,234,236,237,242,248,249,],[-131,-131,-19,-21,43,-37,-131,-131,-131,62,-20,-23,-36,-131,-40,-39,-22,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,168,-101,-131,-131,177,178,180,-131,-108,186,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,-100,-95,198,-52,-53,-131,-100,-68,-70,-100,-72,211,-120,-124,-129,-97,-131,-55,-25,-28,-131,-131,-71,-110,-112,226,-100,-64,-66,-69,-60,-131,-27,-54,-57,-100,-131,-56,-65,]),'CTE_I':([34,55,58,64,68,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,101,104,106,107,108,109,110,111,112,113,114,117,118,119,120,121,122,123,126,127,128,129,133,136,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,182,187,189,190,191,192,193,195,196,197,198,200,201,202,203,204,206,210,213,216,220,223,226,228,229,231,233,235,238,239,240,241,243,245,251,253,254,256,],[42,63,-4,99,-99,99,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,99,-95,-24,99,-26,99,-99,-99,99,-131,-82,-131,-131,-131,-131,-102,-103,-104,-101,-131,99,-99,99,99,-85,-109,-111,99,-86,-109,-113,-87,99,-121,-114,-115,-116,-117,-118,-119,-88,99,-125,-122,-123,-89,99,-130,-126,-127,-128,99,-100,-95,99,-131,-99,99,99,99,-120,-124,-129,-97,-99,-51,-60,99,-25,-28,-62,-63,-67,-110,-112,-59,-99,99,-60,-27,99,-83,-82,-58,-131,99,99,-99,-73,-75,-84,99,-80,-74,]),'R_SB':([42,63,88,91,92,93,94,95,96,97,98,99,106,108,113,117,118,119,120,121,122,123,126,127,130,139,141,144,146,147,149,156,158,161,163,168,169,176,191,192,193,195,201,202,210,213,218,226,228,],[51,67,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,176,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,-100,-95,-131,-120,-124,-129,-97,-25,-28,-110,-112,228,-60,-27,]),'RETURN':([58,64,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,104,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,167,168,169,176,191,192,193,195,197,198,201,202,203,204,206,210,213,216,223,226,228,231,238,239,243,245,251,253,254,256,],[-4,82,82,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,82,-100,-95,-131,-120,-124,-129,-97,-51,-60,-25,-28,-62,-63,-67,-110,-112,-59,82,-60,-27,-83,-131,82,-73,-75,-84,82,-80,-74,]),'READ':([58,64,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,104,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,167,168,169,176,191,192,193,195,197,198,201,202,203,204,206,210,213,216,223,226,228,231,238,239,243,245,251,253,254,256,],[-4,83,83,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,83,-100,-95,-131,-120,-124,-129,-97,-51,-60,-25,-28,-62,-63,-67,-110,-112,-59,83,-60,-27,-83,-131,83,-73,-75,-84,83,-80,-74,]),'PRINT':([58,64,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,104,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,167,168,169,176,191,192,193,195,197,198,201,202,203,204,206,210,213,216,223,226,228,231,238,239,243,245,251,253,254,256,],[-4,84,84,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,84,-100,-95,-131,-120,-124,-129,-97,-51,-60,-25,-28,-62,-63,-67,-110,-112,-59,84,-60,-27,-83,-131,84,-73,-75,-84,84,-80,-74,]),'IF':([58,64,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,104,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,167,168,169,176,191,192,193,195,197,198,201,202,203,204,206,210,213,216,223,226,228,231,238,239,243,245,251,253,254,256,],[-4,85,85,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,85,-100,-95,-131,-120,-124,-129,-97,-51,-60,-25,-28,-62,-63,-67,-110,-112,-59,85,-60,-27,-83,-131,85,-73,-75,-84,85,-80,-74,]),'WHILE':([58,64,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,104,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,167,168,169,176,191,192,193,195,197,198,201,202,203,204,206,210,213,216,223,226,228,231,238,239,243,245,251,253,254,256,],[-4,89,89,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,89,-100,-95,-131,-120,-124,-129,-97,-51,-60,-25,-28,-62,-63,-67,-110,-112,-59,89,-60,-27,-83,-131,89,-73,-75,-84,89,-80,-74,]),'FOR':([58,64,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,104,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,167,168,169,176,191,192,193,195,197,198,201,202,203,204,206,210,213,216,223,226,228,231,238,239,243,245,251,253,254,256,],[-4,90,90,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,90,-100,-95,-131,-120,-124,-129,-97,-51,-60,-25,-28,-62,-63,-67,-110,-112,-59,90,-60,-27,-83,-131,90,-73,-75,-84,90,-80,-74,]),'CTE_CHAR':([58,64,68,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,101,104,106,107,108,109,110,111,112,113,114,117,118,119,120,121,122,123,126,127,128,129,133,136,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,182,187,189,190,191,192,193,195,196,197,198,200,201,202,203,204,206,210,213,216,220,223,226,228,229,231,233,235,238,239,240,241,243,245,251,253,254,256,],[-4,97,-99,97,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,97,-95,-24,97,-26,97,-99,-99,97,-131,-82,-131,-131,-131,-131,-102,-103,-104,-101,-131,97,-99,97,97,-85,-109,-111,97,-86,-109,-113,-87,97,-121,-114,-115,-116,-117,-118,-119,-88,97,-125,-122,-123,-89,97,-130,-126,-127,-128,97,-100,-95,97,-131,-99,97,97,97,-120,-124,-129,-97,-99,-51,-60,97,-25,-28,-62,-63,-67,-110,-112,-59,-99,97,-60,-27,97,-83,-82,-58,-131,97,97,-99,-73,-75,-84,97,-80,-74,]),'CTE_F':([58,64,68,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,101,104,106,107,108,109,110,111,112,113,114,117,118,119,120,121,122,123,126,127,128,129,133,136,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,175,176,182,187,189,190,191,192,193,195,196,197,198,200,201,202,203,204,206,210,213,216,220,223,226,228,229,231,233,235,238,239,240,241,243,245,251,253,254,256,],[-4,98,-99,98,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,98,-95,-24,98,-26,98,-99,-99,98,-131,-82,-131,-131,-131,-131,-102,-103,-104,-101,-131,98,-99,98,98,-85,-109,-111,98,-86,-109,-113,-87,98,-121,-114,-115,-116,-117,-118,-119,-88,98,-125,-122,-123,-89,98,-130,-126,-127,-128,98,-100,-95,98,-131,-99,98,98,98,-120,-124,-129,-97,-99,-51,-60,98,-25,-28,-62,-63,-67,-110,-112,-59,-99,98,-60,-27,98,-83,-82,-58,-131,98,98,-99,-73,-75,-84,98,-80,-74,]),'R_B':([58,64,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,103,104,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,167,168,169,176,191,192,193,194,195,197,198,201,202,203,204,206,210,213,216,223,226,228,230,231,238,239,243,245,246,251,253,254,255,256,],[-4,-131,102,-131,-42,-43,-44,-45,-46,-47,-48,-49,-50,-101,-131,-78,-79,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-41,-95,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,-131,-100,-95,-131,-120,-124,-129,214,-97,-51,-60,-25,-28,-62,-63,-67,-110,-112,-59,-131,-60,-27,238,-83,-131,-131,-73,-75,251,-84,-131,-80,256,-74,]),'EQUAL':([80,81,104,106,108,115,116,143,176,201,202,228,],[-101,-131,128,-24,-26,-101,-131,189,-131,-25,-28,-27,]),'MULT':([80,81,94,95,96,97,98,99,104,106,108,120,121,122,123,126,127,168,169,176,195,198,201,202,226,228,],[-101,-131,-94,-96,-98,-107,-106,-105,-95,-24,-26,164,-102,-103,-104,-101,-131,-100,-95,-131,-97,-60,-25,-28,-60,-27,]),'DIV':([80,81,94,95,96,97,98,99,104,106,108,120,121,122,123,126,127,168,169,176,195,198,201,202,226,228,],[-101,-131,-94,-96,-98,-107,-106,-105,-95,-24,-26,165,-102,-103,-104,-101,-131,-100,-95,-131,-97,-60,-25,-28,-60,-27,]),'MOD':([80,81,94,95,96,97,98,99,104,106,108,120,121,122,123,126,127,168,169,176,195,198,201,202,226,228,],[-101,-131,-94,-96,-98,-107,-106,-105,-95,-24,-26,166,-102,-103,-104,-101,-131,-100,-95,-131,-97,-60,-25,-28,-60,-27,]),'PLUS':([80,81,93,94,95,96,97,98,99,104,106,108,119,120,121,122,123,126,127,161,163,168,169,176,193,195,198,201,202,226,228,],[-101,-131,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,159,-131,-102,-103,-104,-101,-131,-89,-130,-100,-95,-131,-129,-97,-60,-25,-28,-60,-27,]),'MINUS':([80,81,93,94,95,96,97,98,99,104,106,108,119,120,121,122,123,126,127,161,163,168,169,176,193,195,198,201,202,226,228,],[-101,-131,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,160,-131,-102,-103,-104,-101,-131,-89,-130,-100,-95,-131,-129,-97,-60,-25,-28,-60,-27,]),'LESSTHAN':([80,81,92,93,94,95,96,97,98,99,104,106,108,118,119,120,121,122,123,126,127,156,158,161,163,168,169,176,192,193,195,198,201,202,226,228,],[-101,-131,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,150,-131,-131,-102,-103,-104,-101,-131,-88,-125,-89,-130,-100,-95,-131,-124,-129,-97,-60,-25,-28,-60,-27,]),'LESSTHANEQ':([80,81,92,93,94,95,96,97,98,99,104,106,108,118,119,120,121,122,123,126,127,156,158,161,163,168,169,176,192,193,195,198,201,202,226,228,],[-101,-131,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,151,-131,-131,-102,-103,-104,-101,-131,-88,-125,-89,-130,-100,-95,-131,-124,-129,-97,-60,-25,-28,-60,-27,]),'GREATERTHAN':([80,81,92,93,94,95,96,97,98,99,104,106,108,118,119,120,121,122,123,126,127,156,158,161,163,168,169,176,192,193,195,198,201,202,226,228,],[-101,-131,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,152,-131,-131,-102,-103,-104,-101,-131,-88,-125,-89,-130,-100,-95,-131,-124,-129,-97,-60,-25,-28,-60,-27,]),'GREATERTHANEQ':([80,81,92,93,94,95,96,97,98,99,104,106,108,118,119,120,121,122,123,126,127,156,158,161,163,168,169,176,192,193,195,198,201,202,226,228,],[-101,-131,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,153,-131,-131,-102,-103,-104,-101,-131,-88,-125,-89,-130,-100,-95,-131,-124,-129,-97,-60,-25,-28,-60,-27,]),'EQ':([80,81,92,93,94,95,96,97,98,99,104,106,108,118,119,120,121,122,123,126,127,156,158,161,163,168,169,176,192,193,195,198,201,202,226,228,],[-101,-131,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,154,-131,-131,-102,-103,-104,-101,-131,-88,-125,-89,-130,-100,-95,-131,-124,-129,-97,-60,-25,-28,-60,-27,]),'DIFERENT':([80,81,92,93,94,95,96,97,98,99,104,106,108,118,119,120,121,122,123,126,127,156,158,161,163,168,169,176,192,193,195,198,201,202,226,228,],[-101,-131,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,155,-131,-131,-102,-103,-104,-101,-131,-88,-125,-89,-130,-100,-95,-131,-124,-129,-97,-60,-25,-28,-60,-27,]),'AND':([80,81,91,92,93,94,95,96,97,98,99,104,106,108,117,118,119,120,121,122,123,126,127,147,149,156,158,161,163,168,169,176,191,192,193,195,198,201,202,226,228,],[-101,-131,-91,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,145,-131,-131,-131,-102,-103,-104,-101,-131,-87,-121,-88,-125,-89,-130,-100,-95,-131,-120,-124,-129,-97,-60,-25,-28,-60,-27,]),'OR':([80,81,88,91,92,93,94,95,96,97,98,99,104,106,108,113,117,118,119,120,121,122,123,126,127,144,146,147,149,156,158,161,163,168,169,176,191,192,193,195,198,201,202,213,226,228,],[-101,-131,-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-95,-24,-26,140,-131,-131,-131,-131,-102,-103,-104,-101,-131,-86,-113,-87,-121,-88,-125,-89,-130,-100,-95,-131,-120,-124,-129,-97,-60,-25,-28,-112,-60,-27,]),'TO':([88,91,92,93,94,95,96,97,98,99,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,168,169,176,191,192,193,195,201,202,210,212,213,225,226,228,],[-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,-100,-95,-131,-120,-124,-129,-97,-25,-28,-110,-81,-112,233,-60,-27,]),'DO':([88,91,92,93,94,95,96,97,98,99,106,108,113,117,118,119,120,121,122,123,126,127,139,141,144,146,147,149,156,158,161,163,168,169,176,191,192,193,195,201,202,210,211,213,224,226,228,247,252,],[-90,-91,-92,-93,-94,-96,-98,-107,-106,-105,-24,-26,-131,-131,-131,-131,-131,-102,-103,-104,-101,-131,-85,-111,-86,-113,-87,-121,-88,-125,-89,-130,-100,-95,-131,-120,-124,-129,-97,-25,-28,-110,-76,-112,232,-60,-27,-76,232,]),'CTE_STRING':([111,182,],[137,137,]),'ELSE':([238,],[244,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'main_quad':([3,],[4,]),'g_var':([5,],[6,]),'var_declaration':([5,43,66,],[7,52,100,]),'empty':([5,6,11,26,27,28,40,41,43,45,51,53,60,64,66,70,81,113,116,117,118,119,120,127,129,135,167,176,196,205,207,223,227,238,239,242,253,],[9,12,12,32,35,38,48,32,9,38,57,61,38,71,9,71,108,141,108,146,149,158,163,108,174,183,71,202,174,221,183,71,236,245,71,221,71,]),'funcs':([6,11,],[10,22,]),'function':([6,11,],[11,11,]),'var1':([8,40,],[14,47,]),'var_type':([8,28,40,45,60,],[15,37,15,37,37,]),'type':([8,13,28,40,45,60,],[16,25,16,16,16,16,]),'main':([10,],[20,]),'func_type':([13,],[23,]),'dec_id':([15,31,44,],[26,41,53,]),'var2':([26,41,],[30,50,]),'dec_id1':([27,],[33,]),'params':([28,45,60,],[36,54,65,]),'register_func':([29,],[39,]),'param_type':([37,],[44,]),'var4':([40,],[46,]),'var3':([41,],[49,]),'dec_id2':([51,],[56,]),'params1':([53,],[59,]),'main_start':([58,],[64,]),'add_params':([62,],[66,]),'statements':([64,70,167,223,239,253,],[69,103,194,230,246,255,]),'statement':([64,70,167,223,239,253,],[70,70,70,70,70,70,]),'assignation':([64,70,167,223,239,253,],[72,72,72,72,72,72,]),'call_func':([64,70,167,223,239,253,],[73,73,73,73,73,73,]),'return_func':([64,70,167,223,239,253,],[74,74,74,74,74,74,]),'read':([64,70,167,223,239,253,],[75,75,75,75,75,75,]),'write':([64,70,167,223,239,253,],[76,76,76,76,76,76,]),'decision_statement':([64,70,167,223,239,253,],[77,77,77,77,77,77,]),'repetition_statement':([64,70,167,223,239,253,],[78,78,78,78,78,78,]),'expression':([64,70,101,107,109,112,128,133,136,142,167,175,187,189,200,223,229,239,240,253,],[79,79,125,130,131,138,171,179,184,188,79,199,210,212,218,79,237,79,247,79,]),'id':([64,70,90,101,107,109,112,128,133,136,142,148,157,162,167,175,187,189,190,200,223,229,239,240,253,],[80,80,115,126,126,126,126,126,126,126,126,126,126,126,80,126,126,126,126,126,80,126,80,126,80,]),'while_statement':([64,70,167,223,239,253,],[86,86,86,86,86,86,]),'for_statement':([64,70,167,223,239,253,],[87,87,87,87,87,87,]),'texp':([64,70,101,107,109,112,128,133,136,142,167,175,187,189,190,200,223,229,239,240,253,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,213,88,88,88,88,88,88,]),'gexp':([64,70,101,107,109,112,128,133,136,142,167,175,187,189,190,200,223,229,239,240,253,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'mexp':([64,70,101,107,109,112,128,133,136,142,148,157,167,175,187,189,190,200,223,229,239,240,253,],[92,92,92,92,92,92,92,92,92,92,191,192,92,92,92,92,92,92,92,92,92,92,92,]),'term':([64,70,101,107,109,112,128,133,136,142,148,157,162,167,175,187,189,190,200,223,229,239,240,253,],[93,93,93,93,93,93,93,93,93,93,93,93,193,93,93,93,93,93,93,93,93,93,93,93,]),'fact':([64,70,101,107,109,112,128,133,136,142,148,157,162,167,175,187,189,190,200,223,229,239,240,253,],[94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'call_func_exp':([64,70,101,107,109,112,128,133,136,142,148,157,162,167,175,187,189,190,200,223,229,239,240,253,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'cte':([64,70,101,107,109,112,128,133,136,142,148,157,162,167,175,187,189,190,200,223,229,239,240,253,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'add_fake':([68,110,111,129,182,196,220,241,],[101,133,136,175,136,175,229,175,]),'id_quad':([80,115,126,],[104,143,169,]),'call_func_era':([81,127,],[105,170,]),'id1':([81,116,127,],[106,106,106,]),'generate_quad_1':([88,],[113,]),'generate_quad_2':([91,],[117,]),'generate_quad_3':([92,],[118,]),'generate_quad_4':([93,],[119,]),'generate_quad_5':([94,],[120,]),'add_cte_char':([97,],[121,]),'add_cte_float':([98,],[122,]),'add_cte_int':([99,],[123,]),'start_func':([100,],[124,]),'read_args':([110,],[132,]),'write_args':([111,],[134,]),'write_args2':([111,182,],[135,207,]),'op1':([113,],[139,]),'breadcrumb':([114,233,],[142,240,]),'op2':([117,],[144,]),'op3aux':([118,],[147,]),'op3':([118,],[148,]),'op4aux':([119,],[156,]),'op4':([119,],[157,]),'op5aux':([120,],[161,]),'op5':([120,],[162,]),'args':([129,196,],[172,215,]),'args1':([129,196,241,],[173,173,248,]),'write_args1':([135,207,],[181,222,]),'add_cte_string':([137,],[185,]),'add_operator':([140,145,],[187,190,]),'remove_fake':([168,179,184,217,237,],[195,205,208,227,242,]),'id2':([176,],[201,]),'exp_type':([186,211,247,],[209,224,252,]),'param_check':([199,],[217,]),'read_args1':([205,242,],[219,249,]),'for_id':([212,],[225,]),'do_statement':([224,252,],[231,254,]),'args2':([227,],[234,]),'next_arg':([235,],[241,]),'decision_statement1':([238,],[243,]),'else_jump':([244,],[250,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID main_quad SEMICOLON g_var funcs main','program',7,'p_program','parser_lexer.py',213),
  ('main_quad -> <empty>','main_quad',0,'p_main_quad','parser_lexer.py',220),
  ('main -> MAIN L_P params R_P var_declaration L_B main_start statements R_B','main',9,'p_main','parser_lexer.py',226),
  ('main_start -> <empty>','main_start',0,'p_main_start','parser_lexer.py',243),
  ('type -> INT','type',1,'p_type','parser_lexer.py',248),
  ('type -> FLOAT','type',1,'p_type','parser_lexer.py',249),
  ('type -> CHAR','type',1,'p_type','parser_lexer.py',250),
  ('g_var -> var_declaration','g_var',1,'p_g_var','parser_lexer.py',256),
  ('funcs -> function funcs','funcs',2,'p_funcs','parser_lexer.py',263),
  ('funcs -> empty','funcs',1,'p_funcs','parser_lexer.py',264),
  ('var_declaration -> VAR var1','var_declaration',2,'p_var_declaration','parser_lexer.py',268),
  ('var_declaration -> empty','var_declaration',1,'p_var_declaration','parser_lexer.py',269),
  ('var1 -> var_type dec_id var2 SEMICOLON var4','var1',5,'p_var1','parser_lexer.py',273),
  ('var2 -> COMA dec_id var3','var2',3,'p_var2','parser_lexer.py',277),
  ('var2 -> empty','var2',1,'p_var2','parser_lexer.py',278),
  ('var3 -> var2','var3',1,'p_var3','parser_lexer.py',282),
  ('var4 -> var1','var4',1,'p_var4','parser_lexer.py',286),
  ('var4 -> empty','var4',1,'p_var4','parser_lexer.py',287),
  ('dec_id -> ID dec_id1','dec_id',2,'p_dec_id','parser_lexer.py',291),
  ('dec_id1 -> L_SB CTE_I R_SB dec_id2','dec_id1',4,'p_dec_id1','parser_lexer.py',311),
  ('dec_id1 -> empty','dec_id1',1,'p_dec_id1','parser_lexer.py',312),
  ('dec_id2 -> L_SB CTE_I R_SB','dec_id2',3,'p_dec_id2','parser_lexer.py',316),
  ('dec_id2 -> empty','dec_id2',1,'p_dec_id2','parser_lexer.py',317),
  ('id -> ID id1','id',2,'p_id','parser_lexer.py',321),
  ('id1 -> L_SB expression R_SB id2','id1',4,'p_id1','parser_lexer.py',327),
  ('id1 -> empty','id1',1,'p_id1','parser_lexer.py',328),
  ('id2 -> L_SB expression R_SB','id2',3,'p_id2','parser_lexer.py',332),
  ('id2 -> empty','id2',1,'p_id2','parser_lexer.py',333),
  ('var_type -> type','var_type',1,'p_var_type','parser_lexer.py',337),
  ('function -> FUNC func_type ID register_func L_P params R_P add_params var_declaration start_func L_B statements R_B','function',13,'p_function','parser_lexer.py',341),
  ('register_func -> <empty>','register_func',0,'p_register_func','parser_lexer.py',355),
  ('add_params -> <empty>','add_params',0,'p_add_params','parser_lexer.py',369),
  ('start_func -> <empty>','start_func',0,'p_start_func','parser_lexer.py',375),
  ('func_type -> VOID','func_type',1,'p_func_type','parser_lexer.py',381),
  ('func_type -> type','func_type',1,'p_func_type','parser_lexer.py',382),
  ('params -> var_type param_type dec_id params1','params',4,'p_params','parser_lexer.py',389),
  ('params -> empty','params',1,'p_params','parser_lexer.py',390),
  ('param_type -> <empty>','param_type',0,'p_param_type','parser_lexer.py',394),
  ('params1 -> COMA params','params1',2,'p_params1','parser_lexer.py',401),
  ('params1 -> empty','params1',1,'p_params1','parser_lexer.py',402),
  ('statements -> statement statements','statements',2,'p_statements','parser_lexer.py',406),
  ('statements -> empty','statements',1,'p_statements','parser_lexer.py',407),
  ('statement -> assignation','statement',1,'p_statement','parser_lexer.py',411),
  ('statement -> call_func','statement',1,'p_statement','parser_lexer.py',412),
  ('statement -> return_func','statement',1,'p_statement','parser_lexer.py',413),
  ('statement -> read','statement',1,'p_statement','parser_lexer.py',414),
  ('statement -> write','statement',1,'p_statement','parser_lexer.py',415),
  ('statement -> decision_statement','statement',1,'p_statement','parser_lexer.py',416),
  ('statement -> repetition_statement','statement',1,'p_statement','parser_lexer.py',417),
  ('statement -> expression','statement',1,'p_statement','parser_lexer.py',418),
  ('assignation -> id id_quad EQUAL expression SEMICOLON','assignation',5,'p_assignation','parser_lexer.py',422),
  ('args -> args1','args',1,'p_args','parser_lexer.py',437),
  ('args -> empty','args',1,'p_args','parser_lexer.py',438),
  ('args1 -> add_fake expression param_check remove_fake args2','args1',5,'p_args1','parser_lexer.py',442),
  ('param_check -> <empty>','param_check',0,'p_param_check','parser_lexer.py',446),
  ('args2 -> COMA next_arg args1','args2',3,'p_args2','parser_lexer.py',461),
  ('args2 -> empty','args2',1,'p_args2','parser_lexer.py',462),
  ('next_arg -> <empty>','next_arg',0,'p_next_arg','parser_lexer.py',466),
  ('call_func -> ID call_func_era L_P args R_P SEMICOLON','call_func',6,'p_call_func','parser_lexer.py',472),
  ('call_func_exp -> ID call_func_era L_P args R_P','call_func_exp',5,'p_call_func_exp','parser_lexer.py',483),
  ('call_func_era -> <empty>','call_func_era',0,'p_call_func_era','parser_lexer.py',506),
  ('return_func -> RETURN L_P expression R_P SEMICOLON','return_func',5,'p_return_func','parser_lexer.py',517),
  ('read -> READ L_P read_args R_P SEMICOLON','read',5,'p_read','parser_lexer.py',527),
  ('read_args -> add_fake expression remove_fake read_args1','read_args',4,'p_read_args','parser_lexer.py',536),
  ('read_args1 -> COMA add_fake expression remove_fake read_args1','read_args1',5,'p_read_args1','parser_lexer.py',540),
  ('read_args1 -> empty','read_args1',1,'p_read_args1','parser_lexer.py',541),
  ('write -> PRINT L_P write_args R_P SEMICOLON','write',5,'p_write','parser_lexer.py',545),
  ('write_args -> write_args2 write_args1','write_args',2,'p_write_args','parser_lexer.py',553),
  ('write_args1 -> COMA write_args2 write_args1','write_args1',3,'p_write_args1','parser_lexer.py',557),
  ('write_args1 -> empty','write_args1',1,'p_write_args1','parser_lexer.py',558),
  ('write_args2 -> add_fake expression remove_fake','write_args2',3,'p_write_args2','parser_lexer.py',562),
  ('write_args2 -> CTE_STRING add_cte_string','write_args2',2,'p_write_args2','parser_lexer.py',563),
  ('decision_statement -> IF L_P expression R_P exp_type L_B statements R_B decision_statement1','decision_statement',9,'p_decision_statement','parser_lexer.py',567),
  ('decision_statement1 -> ELSE else_jump L_B statements R_B','decision_statement1',5,'p_decision_statement1','parser_lexer.py',574),
  ('decision_statement1 -> empty','decision_statement1',1,'p_decision_statement1','parser_lexer.py',575),
  ('exp_type -> <empty>','exp_type',0,'p_exp_type','parser_lexer.py',579),
  ('else_jump -> <empty>','else_jump',0,'p_else_jump','parser_lexer.py',591),
  ('repetition_statement -> while_statement','repetition_statement',1,'p_repetition_statement','parser_lexer.py',600),
  ('repetition_statement -> for_statement','repetition_statement',1,'p_repetition_statement','parser_lexer.py',601),
  ('for_statement -> FOR id id_quad EQUAL expression for_id TO breadcrumb expression exp_type do_statement','for_statement',11,'p_for_statement','parser_lexer.py',605),
  ('for_id -> <empty>','for_id',0,'p_for_id','parser_lexer.py',631),
  ('breadcrumb -> <empty>','breadcrumb',0,'p_breadcrumb','parser_lexer.py',647),
  ('while_statement -> WHILE L_P breadcrumb expression R_P exp_type do_statement','while_statement',7,'p_while_statement','parser_lexer.py',653),
  ('do_statement -> DO L_B statements R_B','do_statement',4,'p_do_statement','parser_lexer.py',662),
  ('expression -> texp generate_quad_1 op1','expression',3,'p_expression','parser_lexer.py',666),
  ('texp -> gexp generate_quad_2 op2','texp',3,'p_texp','parser_lexer.py',670),
  ('gexp -> mexp generate_quad_3 op3aux','gexp',3,'p_gexp','parser_lexer.py',674),
  ('mexp -> term generate_quad_4 op4aux','mexp',3,'p_mexp','parser_lexer.py',678),
  ('term -> fact generate_quad_5 op5aux','term',3,'p_term','parser_lexer.py',682),
  ('generate_quad_1 -> <empty>','generate_quad_1',0,'p_generate_quad_1','parser_lexer.py',686),
  ('generate_quad_2 -> <empty>','generate_quad_2',0,'p_generate_quad_2','parser_lexer.py',693),
  ('generate_quad_3 -> <empty>','generate_quad_3',0,'p_generate_quad_3','parser_lexer.py',700),
  ('generate_quad_4 -> <empty>','generate_quad_4',0,'p_generate_quad_4','parser_lexer.py',707),
  ('generate_quad_5 -> <empty>','generate_quad_5',0,'p_generate_quad_5','parser_lexer.py',714),
  ('fact -> id id_quad','fact',2,'p_fact','parser_lexer.py',721),
  ('fact -> call_func_exp','fact',1,'p_fact','parser_lexer.py',722),
  ('fact -> L_P add_fake expression R_P remove_fake','fact',5,'p_fact','parser_lexer.py',723),
  ('fact -> cte','fact',1,'p_fact','parser_lexer.py',724),
  ('add_fake -> <empty>','add_fake',0,'p_add_fake','parser_lexer.py',728),
  ('remove_fake -> <empty>','remove_fake',0,'p_remove_fake','parser_lexer.py',734),
  ('id_quad -> <empty>','id_quad',0,'p_id_quad','parser_lexer.py',741),
  ('cte -> CTE_CHAR add_cte_char','cte',2,'p_cte','parser_lexer.py',761),
  ('cte -> CTE_F add_cte_float','cte',2,'p_cte','parser_lexer.py',762),
  ('cte -> CTE_I add_cte_int','cte',2,'p_cte','parser_lexer.py',763),
  ('add_cte_int -> <empty>','add_cte_int',0,'p_add_cte_int','parser_lexer.py',767),
  ('add_cte_float -> <empty>','add_cte_float',0,'p_add_cte_float','parser_lexer.py',782),
  ('add_cte_char -> <empty>','add_cte_char',0,'p_add_cte_char','parser_lexer.py',797),
  ('add_cte_string -> <empty>','add_cte_string',0,'p_add_cte_string','parser_lexer.py',811),
  ('add_operator -> <empty>','add_operator',0,'p_add_operator','parser_lexer.py',825),
  ('op1 -> OR add_operator expression','op1',3,'p_op1','parser_lexer.py',830),
  ('op1 -> empty','op1',1,'p_op1','parser_lexer.py',831),
  ('op2 -> AND add_operator texp','op2',3,'p_op2','parser_lexer.py',834),
  ('op2 -> empty','op2',1,'p_op2','parser_lexer.py',835),
  ('op3 -> LESSTHAN','op3',1,'p_op3','parser_lexer.py',839),
  ('op3 -> LESSTHANEQ','op3',1,'p_op3','parser_lexer.py',840),
  ('op3 -> GREATERTHAN','op3',1,'p_op3','parser_lexer.py',841),
  ('op3 -> GREATERTHANEQ','op3',1,'p_op3','parser_lexer.py',842),
  ('op3 -> EQ','op3',1,'p_op3','parser_lexer.py',843),
  ('op3 -> DIFERENT','op3',1,'p_op3','parser_lexer.py',844),
  ('op3aux -> op3 mexp','op3aux',2,'p_op3aux','parser_lexer.py',850),
  ('op3aux -> empty','op3aux',1,'p_op3aux','parser_lexer.py',851),
  ('op4 -> PLUS','op4',1,'p_op4','parser_lexer.py',855),
  ('op4 -> MINUS','op4',1,'p_op4','parser_lexer.py',856),
  ('op4aux -> op4 mexp','op4aux',2,'p_op4aux','parser_lexer.py',862),
  ('op4aux -> empty','op4aux',1,'p_op4aux','parser_lexer.py',863),
  ('op5 -> MULT','op5',1,'p_op5','parser_lexer.py',867),
  ('op5 -> DIV','op5',1,'p_op5','parser_lexer.py',868),
  ('op5 -> MOD','op5',1,'p_op5','parser_lexer.py',869),
  ('op5aux -> op5 term','op5aux',2,'p_op5aux','parser_lexer.py',875),
  ('op5aux -> empty','op5aux',1,'p_op5aux','parser_lexer.py',876),
  ('empty -> <empty>','empty',0,'p_empty','parser_lexer.py',881),
]
