
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COMA CTE_CHAR CTE_F CTE_I CTE_STRING DIFERENT DIV DO ELSE EQ EQUAL FLOAT FOR FUNC GREATERTHAN GREATERTHANEQ ID IF INT LESSTHAN LESSTHANEQ L_B L_P L_SB MAIN MINUS MOD MULT OR PLUS PRINT PROGRAM READ RETURN R_B R_P R_SB SEMICOLON TO VAR VOID WHILEprogram : PROGRAM ID main_quad SEMICOLON g_var funcs mainmain_quad : main : MAIN L_P params R_P var_declaration L_B main_start statements R_Bmain_start : type : INT\n            | FLOAT\n            | CHARg_var : var_declarationfuncs : function funcs\n            | emptyvar_declaration : VAR var1\n                        | emptyvar1 : var_type dec_id var2 SEMICOLON var4var2 : COMA dec_id var3\n            | emptyvar3 : var2var4 : var1\n            | emptydec_id : ID add_id dec_id1dec_id1 : L_SB CTE_I set_array R_SB dec_id2\n            | emptydec_id2 : L_SB CTE_I set_array R_SB\n        | emptyadd_id : set_array : id : ID id1id1 : L_SB expression R_SB id2\n            | emptyid2 : L_SB expression R_SB\n        | emptyvar_type : typefunction : FUNC func_type ID register_func L_P params R_P add_params var_declaration start_func L_B statements R_Bregister_func : add_params : start_func : func_type : VOID\n                | typeparams : var_type param_type dec_id params1\n            | emptyparam_type : params1 : COMA params\n                | emptystatements : statement statements\n                | emptystatement : assignation\n                | call_func\n                | return_func\n                | read\n                | write\n                | decision_statement\n                | repetition_statement\n                | expressionassignation : id id_quad EQUAL expression SEMICOLONargs : args1\n            | emptyargs1 : add_fake expression param_check remove_fake args2param_check : args2 : COMA next_arg args1\n            | emptynext_arg : call_func :  ID call_func_era L_P args R_P SEMICOLONcall_func_exp :  ID call_func_era L_P args R_Pcall_func_era : return_func : RETURN L_P expression R_P SEMICOLONread : READ L_P read_args R_P SEMICOLONread_args : add_fake expression remove_fake read_args1read_args1 : COMA add_fake expression remove_fake read_args1\n                | emptywrite : PRINT L_P write_args R_P SEMICOLONwrite_args : write_args2 write_args1write_args1 : COMA write_args2 write_args1\n                    | emptywrite_args2 : add_fake expression remove_fake\n                | CTE_STRING add_cte_stringdecision_statement : IF L_P expression R_P exp_type L_B statements R_B decision_statement1decision_statement1 : ELSE else_jump L_B statements R_B\n                            | emptyexp_type : else_jump : repetition_statement : while_statement\n                            | for_statementfor_statement : FOR id id_quad EQUAL expression for_id TO breadcrumb expression exp_type do_statementfor_id : breadcrumb : while_statement : WHILE L_P breadcrumb expression R_P exp_type do_statementdo_statement :  DO L_B statements R_Bexpression : texp generate_quad_1 op1texp : gexp generate_quad_2 op2gexp : mexp generate_quad_3 op3auxmexp : term generate_quad_4 op4auxterm : fact generate_quad_5 op5auxgenerate_quad_1 : generate_quad_2 : generate_quad_3 : generate_quad_4 : generate_quad_5 : fact : id id_quad\n            | call_func_exp\n            | L_P add_fake expression R_P remove_fake\n            | cteadd_fake : remove_fake : \n        id_quad :\n    cte : CTE_CHAR add_cte_char\n            | CTE_F add_cte_float\n            | CTE_I add_cte_int add_cte_int : add_cte_float : add_cte_char : add_cte_string : add_operator : op1 : OR add_operator expression\n            | emptyop2 : AND add_operator texp\n            | emptyop3 : LESSTHAN\n            | LESSTHANEQ\xa0\n            | GREATERTHAN\n            | GREATERTHANEQ\n            | EQ\n            | DIFERENTop3aux : op3 mexp\n            | emptyop4 : PLUS\n            | MINUSop4aux : op4 mexp\n            | emptyop5 : MULT\n        | DIV\n        | MODop5aux : op5 term\n            | empty\n        empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,20,103,],[0,-1,-3,]),'ID':([2,15,16,17,18,19,23,24,25,31,35,44,56,62,68,70,72,73,74,75,76,77,78,79,80,81,86,87,88,90,91,92,93,94,95,96,97,98,99,102,105,107,108,109,110,111,112,113,114,115,118,119,120,121,122,123,124,128,129,130,131,135,138,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,171,172,178,179,185,190,192,193,194,195,196,198,199,200,201,203,204,205,206,207,209,213,216,219,223,226,229,231,232,234,236,238,241,242,243,244,246,248,254,256,257,259,],[3,27,-31,-5,-6,-7,29,-36,-37,27,-40,27,-4,81,-101,81,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,117,-93,-94,-95,-96,-98,-100,-109,-108,-107,129,-97,-26,129,-28,129,-101,-101,129,-133,-84,-133,-133,-133,-133,-104,-105,-106,-103,-133,129,-101,129,129,-87,-111,-113,129,-88,-111,-115,-89,129,-123,-116,-117,-118,-119,-120,-121,-90,129,-127,-124,-125,-91,129,-132,-128,-129,-130,81,-102,-97,129,-133,-101,129,129,129,-122,-126,-131,-99,-101,-53,-62,129,-27,-30,-64,-65,-69,-112,-114,-61,-101,81,-62,-29,129,-85,-84,-60,-133,81,129,-101,-75,-77,-86,81,-82,-76,]),'SEMICOLON':([3,4,26,27,30,32,33,39,40,42,49,50,61,66,67,88,91,92,93,94,95,96,97,98,99,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,170,171,172,174,179,180,181,183,194,195,196,198,201,204,205,213,216,229,231,],[-2,5,-133,-24,38,-15,-133,-133,-19,-21,-14,-16,-133,-20,-23,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,-22,-102,-97,200,-133,206,207,209,-122,-126,-131,-99,219,-27,-30,-112,-114,-62,-29,]),'VAR':([5,43,60,64,],[8,8,-34,8,]),'FUNC':([5,6,7,9,11,14,38,46,47,48,217,],[-133,13,-8,-12,13,-11,-133,-13,-17,-18,-32,]),'MAIN':([5,6,7,9,10,11,12,14,22,38,46,47,48,217,],[-133,-133,-8,-12,21,-133,-10,-11,-9,-133,-13,-17,-18,-32,]),'INT':([8,13,28,38,45,58,],[17,17,17,17,17,17,]),'FLOAT':([8,13,28,38,45,58,],[18,18,18,18,18,18,]),'CHAR':([8,13,28,38,45,58,],[19,19,19,19,19,19,]),'L_B':([9,14,38,43,46,47,48,52,60,64,100,125,189,212,235,247,253,],[-12,-11,-133,-133,-13,-17,-18,56,-34,-133,-35,169,-78,226,242,-79,256,]),'VOID':([13,],[24,]),'L_P':([21,29,37,56,62,68,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,113,114,115,118,119,120,121,122,123,124,128,129,130,131,135,138,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,171,172,173,178,179,185,190,192,193,194,195,196,198,199,200,201,203,204,205,206,207,209,213,216,219,223,226,229,231,232,234,236,238,241,242,243,244,246,248,254,256,257,259,],[28,-33,45,-4,68,-101,68,-45,-46,-47,-48,-49,-50,-51,-52,-103,-63,110,111,112,113,-80,-81,-92,115,-93,-94,-95,-96,-98,-100,-109,-108,-107,68,-97,131,-26,68,-28,68,-101,-101,68,-133,-84,-133,-133,-133,-133,-104,-105,-106,-103,-63,68,-101,68,68,-87,-111,-113,68,-88,-111,-115,-89,68,-123,-116,-117,-118,-119,-120,-121,-90,68,-127,-124,-125,-91,68,-132,-128,-129,-130,68,-102,-97,199,68,-133,-101,68,68,68,-122,-126,-131,-99,-101,-53,-62,68,-27,-30,-64,-65,-69,-112,-114,-61,-101,68,-62,-29,68,-85,-84,-60,-133,68,68,-101,-75,-77,-86,68,-82,-76,]),'COMA':([26,27,33,39,40,42,53,61,66,67,88,91,92,93,94,95,96,97,98,99,107,109,114,118,119,120,121,122,123,124,128,129,137,139,141,143,146,148,149,151,158,160,163,165,170,171,172,179,182,187,188,194,195,196,198,202,204,205,208,210,211,213,216,220,229,230,231,240,245,],[31,-24,-133,31,-19,-21,58,-133,-20,-23,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,185,-110,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,-22,-102,-97,-133,-102,-102,-74,-122,-126,-131,-99,-57,-27,-30,223,185,-73,-112,-114,-102,-62,238,-29,-102,223,]),'L_SB':([27,33,61,81,117,129,179,],[-24,41,65,108,108,108,203,]),'R_P':([27,28,33,34,36,40,42,45,53,54,57,58,59,61,63,66,67,88,91,92,93,94,95,96,97,98,99,107,109,114,118,119,120,121,122,123,124,127,128,129,131,133,134,136,137,139,140,141,143,146,148,149,151,158,160,163,165,170,171,172,175,176,177,179,182,184,186,187,188,191,194,195,196,198,199,202,204,205,208,210,211,213,216,218,220,222,224,225,229,230,231,237,239,240,245,251,252,],[-24,-133,-133,43,-39,-19,-21,-133,-133,60,-38,-133,-42,-133,-41,-20,-23,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,171,-103,-133,-133,180,181,183,-133,-110,189,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,-22,-102,-97,201,-54,-55,-133,-102,-70,-72,-102,-74,214,-122,-126,-131,-99,-133,-57,-27,-30,-133,-133,-73,-112,-114,229,-102,-66,-68,-71,-62,-133,-29,-56,-59,-102,-133,-58,-67,]),'CTE_I':([41,56,62,65,68,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,102,105,107,108,109,110,111,112,113,114,115,118,119,120,121,122,123,124,128,129,130,131,135,138,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,171,172,178,179,185,190,192,193,194,195,196,198,199,200,201,203,204,205,206,207,209,213,216,219,223,226,229,231,232,234,236,238,241,242,243,244,246,248,254,256,257,259,],[51,-4,99,101,-101,99,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,99,-97,-26,99,-28,99,-101,-101,99,-133,-84,-133,-133,-133,-133,-104,-105,-106,-103,-133,99,-101,99,99,-87,-111,-113,99,-88,-111,-115,-89,99,-123,-116,-117,-118,-119,-120,-121,-90,99,-127,-124,-125,-91,99,-132,-128,-129,-130,99,-102,-97,99,-133,-101,99,99,99,-122,-126,-131,-99,-101,-53,-62,99,-27,-30,-64,-65,-69,-112,-114,-61,-101,99,-62,-29,99,-85,-84,-60,-133,99,99,-101,-75,-77,-86,99,-82,-76,]),'R_SB':([51,55,88,91,92,93,94,95,96,97,98,99,101,107,109,114,118,119,120,121,122,123,124,126,128,129,132,141,143,146,148,149,151,158,160,163,165,171,172,179,194,195,196,198,204,205,213,216,221,229,231,],[-25,61,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-25,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,170,-103,-133,179,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,-102,-97,-133,-122,-126,-131,-99,-27,-30,-112,-114,231,-62,-29,]),'RETURN':([56,62,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,105,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,169,171,172,179,194,195,196,198,200,201,204,205,206,207,209,213,216,219,226,229,231,234,241,242,246,248,254,256,257,259,],[-4,82,82,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,82,-102,-97,-133,-122,-126,-131,-99,-53,-62,-27,-30,-64,-65,-69,-112,-114,-61,82,-62,-29,-85,-133,82,-75,-77,-86,82,-82,-76,]),'READ':([56,62,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,105,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,169,171,172,179,194,195,196,198,200,201,204,205,206,207,209,213,216,219,226,229,231,234,241,242,246,248,254,256,257,259,],[-4,83,83,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,83,-102,-97,-133,-122,-126,-131,-99,-53,-62,-27,-30,-64,-65,-69,-112,-114,-61,83,-62,-29,-85,-133,83,-75,-77,-86,83,-82,-76,]),'PRINT':([56,62,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,105,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,169,171,172,179,194,195,196,198,200,201,204,205,206,207,209,213,216,219,226,229,231,234,241,242,246,248,254,256,257,259,],[-4,84,84,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,84,-102,-97,-133,-122,-126,-131,-99,-53,-62,-27,-30,-64,-65,-69,-112,-114,-61,84,-62,-29,-85,-133,84,-75,-77,-86,84,-82,-76,]),'IF':([56,62,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,105,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,169,171,172,179,194,195,196,198,200,201,204,205,206,207,209,213,216,219,226,229,231,234,241,242,246,248,254,256,257,259,],[-4,85,85,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,85,-102,-97,-133,-122,-126,-131,-99,-53,-62,-27,-30,-64,-65,-69,-112,-114,-61,85,-62,-29,-85,-133,85,-75,-77,-86,85,-82,-76,]),'WHILE':([56,62,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,105,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,169,171,172,179,194,195,196,198,200,201,204,205,206,207,209,213,216,219,226,229,231,234,241,242,246,248,254,256,257,259,],[-4,89,89,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,89,-102,-97,-133,-122,-126,-131,-99,-53,-62,-27,-30,-64,-65,-69,-112,-114,-61,89,-62,-29,-85,-133,89,-75,-77,-86,89,-82,-76,]),'FOR':([56,62,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,105,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,169,171,172,179,194,195,196,198,200,201,204,205,206,207,209,213,216,219,226,229,231,234,241,242,246,248,254,256,257,259,],[-4,90,90,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,90,-102,-97,-133,-122,-126,-131,-99,-53,-62,-27,-30,-64,-65,-69,-112,-114,-61,90,-62,-29,-85,-133,90,-75,-77,-86,90,-82,-76,]),'CTE_CHAR':([56,62,68,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,102,105,107,108,109,110,111,112,113,114,115,118,119,120,121,122,123,124,128,129,130,131,135,138,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,171,172,178,179,185,190,192,193,194,195,196,198,199,200,201,203,204,205,206,207,209,213,216,219,223,226,229,231,232,234,236,238,241,242,243,244,246,248,254,256,257,259,],[-4,97,-101,97,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,97,-97,-26,97,-28,97,-101,-101,97,-133,-84,-133,-133,-133,-133,-104,-105,-106,-103,-133,97,-101,97,97,-87,-111,-113,97,-88,-111,-115,-89,97,-123,-116,-117,-118,-119,-120,-121,-90,97,-127,-124,-125,-91,97,-132,-128,-129,-130,97,-102,-97,97,-133,-101,97,97,97,-122,-126,-131,-99,-101,-53,-62,97,-27,-30,-64,-65,-69,-112,-114,-61,-101,97,-62,-29,97,-85,-84,-60,-133,97,97,-101,-75,-77,-86,97,-82,-76,]),'CTE_F':([56,62,68,70,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,102,105,107,108,109,110,111,112,113,114,115,118,119,120,121,122,123,124,128,129,130,131,135,138,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,171,172,178,179,185,190,192,193,194,195,196,198,199,200,201,203,204,205,206,207,209,213,216,219,223,226,229,231,232,234,236,238,241,242,243,244,246,248,254,256,257,259,],[-4,98,-101,98,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,98,-97,-26,98,-28,98,-101,-101,98,-133,-84,-133,-133,-133,-133,-104,-105,-106,-103,-133,98,-101,98,98,-87,-111,-113,98,-88,-111,-115,-89,98,-123,-116,-117,-118,-119,-120,-121,-90,98,-127,-124,-125,-91,98,-132,-128,-129,-130,98,-102,-97,98,-133,-101,98,98,98,-122,-126,-131,-99,-101,-53,-62,98,-27,-30,-64,-65,-69,-112,-114,-61,-101,98,-62,-29,98,-85,-84,-60,-133,98,98,-101,-75,-77,-86,98,-82,-76,]),'R_B':([56,62,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,91,92,93,94,95,96,97,98,99,104,105,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,169,171,172,179,194,195,196,197,198,200,201,204,205,206,207,209,213,216,219,226,229,231,233,234,241,242,246,248,249,254,256,257,258,259,],[-4,-133,103,-133,-44,-45,-46,-47,-48,-49,-50,-51,-52,-103,-133,-80,-81,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-43,-97,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,-133,-102,-97,-133,-122,-126,-131,217,-99,-53,-62,-27,-30,-64,-65,-69,-112,-114,-61,-133,-62,-29,241,-85,-133,-133,-75,-77,254,-86,-133,-82,259,-76,]),'EQUAL':([80,81,105,107,109,116,117,145,179,204,205,231,],[-103,-133,130,-26,-28,-103,-133,192,-133,-27,-30,-29,]),'MULT':([80,81,94,95,96,97,98,99,105,107,109,121,122,123,124,128,129,171,172,179,198,201,204,205,229,231,],[-103,-133,-96,-98,-100,-109,-108,-107,-97,-26,-28,166,-104,-105,-106,-103,-133,-102,-97,-133,-99,-62,-27,-30,-62,-29,]),'DIV':([80,81,94,95,96,97,98,99,105,107,109,121,122,123,124,128,129,171,172,179,198,201,204,205,229,231,],[-103,-133,-96,-98,-100,-109,-108,-107,-97,-26,-28,167,-104,-105,-106,-103,-133,-102,-97,-133,-99,-62,-27,-30,-62,-29,]),'MOD':([80,81,94,95,96,97,98,99,105,107,109,121,122,123,124,128,129,171,172,179,198,201,204,205,229,231,],[-103,-133,-96,-98,-100,-109,-108,-107,-97,-26,-28,168,-104,-105,-106,-103,-133,-102,-97,-133,-99,-62,-27,-30,-62,-29,]),'PLUS':([80,81,93,94,95,96,97,98,99,105,107,109,120,121,122,123,124,128,129,163,165,171,172,179,196,198,201,204,205,229,231,],[-103,-133,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,161,-133,-104,-105,-106,-103,-133,-91,-132,-102,-97,-133,-131,-99,-62,-27,-30,-62,-29,]),'MINUS':([80,81,93,94,95,96,97,98,99,105,107,109,120,121,122,123,124,128,129,163,165,171,172,179,196,198,201,204,205,229,231,],[-103,-133,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,162,-133,-104,-105,-106,-103,-133,-91,-132,-102,-97,-133,-131,-99,-62,-27,-30,-62,-29,]),'LESSTHAN':([80,81,92,93,94,95,96,97,98,99,105,107,109,119,120,121,122,123,124,128,129,158,160,163,165,171,172,179,195,196,198,201,204,205,229,231,],[-103,-133,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,152,-133,-133,-104,-105,-106,-103,-133,-90,-127,-91,-132,-102,-97,-133,-126,-131,-99,-62,-27,-30,-62,-29,]),'LESSTHANEQ':([80,81,92,93,94,95,96,97,98,99,105,107,109,119,120,121,122,123,124,128,129,158,160,163,165,171,172,179,195,196,198,201,204,205,229,231,],[-103,-133,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,153,-133,-133,-104,-105,-106,-103,-133,-90,-127,-91,-132,-102,-97,-133,-126,-131,-99,-62,-27,-30,-62,-29,]),'GREATERTHAN':([80,81,92,93,94,95,96,97,98,99,105,107,109,119,120,121,122,123,124,128,129,158,160,163,165,171,172,179,195,196,198,201,204,205,229,231,],[-103,-133,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,154,-133,-133,-104,-105,-106,-103,-133,-90,-127,-91,-132,-102,-97,-133,-126,-131,-99,-62,-27,-30,-62,-29,]),'GREATERTHANEQ':([80,81,92,93,94,95,96,97,98,99,105,107,109,119,120,121,122,123,124,128,129,158,160,163,165,171,172,179,195,196,198,201,204,205,229,231,],[-103,-133,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,155,-133,-133,-104,-105,-106,-103,-133,-90,-127,-91,-132,-102,-97,-133,-126,-131,-99,-62,-27,-30,-62,-29,]),'EQ':([80,81,92,93,94,95,96,97,98,99,105,107,109,119,120,121,122,123,124,128,129,158,160,163,165,171,172,179,195,196,198,201,204,205,229,231,],[-103,-133,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,156,-133,-133,-104,-105,-106,-103,-133,-90,-127,-91,-132,-102,-97,-133,-126,-131,-99,-62,-27,-30,-62,-29,]),'DIFERENT':([80,81,92,93,94,95,96,97,98,99,105,107,109,119,120,121,122,123,124,128,129,158,160,163,165,171,172,179,195,196,198,201,204,205,229,231,],[-103,-133,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,157,-133,-133,-104,-105,-106,-103,-133,-90,-127,-91,-132,-102,-97,-133,-126,-131,-99,-62,-27,-30,-62,-29,]),'AND':([80,81,91,92,93,94,95,96,97,98,99,105,107,109,118,119,120,121,122,123,124,128,129,149,151,158,160,163,165,171,172,179,194,195,196,198,201,204,205,229,231,],[-103,-133,-93,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,147,-133,-133,-133,-104,-105,-106,-103,-133,-89,-123,-90,-127,-91,-132,-102,-97,-133,-122,-126,-131,-99,-62,-27,-30,-62,-29,]),'OR':([80,81,88,91,92,93,94,95,96,97,98,99,105,107,109,114,118,119,120,121,122,123,124,128,129,146,148,149,151,158,160,163,165,171,172,179,194,195,196,198,201,204,205,216,229,231,],[-103,-133,-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-97,-26,-28,142,-133,-133,-133,-133,-104,-105,-106,-103,-133,-88,-115,-89,-123,-90,-127,-91,-132,-102,-97,-133,-122,-126,-131,-99,-62,-27,-30,-114,-62,-29,]),'TO':([88,91,92,93,94,95,96,97,98,99,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,171,172,179,194,195,196,198,204,205,213,215,216,228,229,231,],[-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,-102,-97,-133,-122,-126,-131,-99,-27,-30,-112,-83,-114,236,-62,-29,]),'DO':([88,91,92,93,94,95,96,97,98,99,107,109,114,118,119,120,121,122,123,124,128,129,141,143,146,148,149,151,158,160,163,165,171,172,179,194,195,196,198,204,205,213,214,216,227,229,231,250,255,],[-92,-93,-94,-95,-96,-98,-100,-109,-108,-107,-26,-28,-133,-133,-133,-133,-133,-104,-105,-106,-103,-133,-87,-113,-88,-115,-89,-123,-90,-127,-91,-132,-102,-97,-133,-122,-126,-131,-99,-27,-30,-112,-78,-114,235,-62,-29,-78,235,]),'CTE_STRING':([112,185,],[139,139,]),'ELSE':([241,],[247,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'main_quad':([3,],[4,]),'g_var':([5,],[6,]),'var_declaration':([5,43,64,],[7,52,100,]),'empty':([5,6,11,26,28,33,38,39,43,45,53,58,61,62,64,70,81,114,117,118,119,120,121,129,131,137,169,179,199,208,210,226,230,241,242,245,256,],[9,12,12,32,36,42,48,32,9,36,59,36,67,71,9,71,109,143,109,148,151,160,165,109,177,186,71,205,177,224,186,71,239,248,71,224,71,]),'funcs':([6,11,],[10,22,]),'function':([6,11,],[11,11,]),'var1':([8,38,],[14,47,]),'var_type':([8,28,38,45,58,],[15,35,15,35,35,]),'type':([8,13,28,38,45,58,],[16,25,16,16,16,16,]),'main':([10,],[20,]),'func_type':([13,],[23,]),'dec_id':([15,31,44,],[26,39,53,]),'var2':([26,39,],[30,50,]),'add_id':([27,],[33,]),'params':([28,45,58,],[34,54,63,]),'register_func':([29,],[37,]),'dec_id1':([33,],[40,]),'param_type':([35,],[44,]),'var4':([38,],[46,]),'var3':([39,],[49,]),'set_array':([51,101,],[55,126,]),'params1':([53,],[57,]),'main_start':([56,],[62,]),'add_params':([60,],[64,]),'dec_id2':([61,],[66,]),'statements':([62,70,169,226,242,256,],[69,104,197,233,249,258,]),'statement':([62,70,169,226,242,256,],[70,70,70,70,70,70,]),'assignation':([62,70,169,226,242,256,],[72,72,72,72,72,72,]),'call_func':([62,70,169,226,242,256,],[73,73,73,73,73,73,]),'return_func':([62,70,169,226,242,256,],[74,74,74,74,74,74,]),'read':([62,70,169,226,242,256,],[75,75,75,75,75,75,]),'write':([62,70,169,226,242,256,],[76,76,76,76,76,76,]),'decision_statement':([62,70,169,226,242,256,],[77,77,77,77,77,77,]),'repetition_statement':([62,70,169,226,242,256,],[78,78,78,78,78,78,]),'expression':([62,70,102,108,110,113,130,135,138,144,169,178,190,192,203,226,232,242,243,256,],[79,79,127,132,133,140,174,182,187,191,79,202,213,215,221,79,240,79,250,79,]),'id':([62,70,90,102,108,110,113,130,135,138,144,150,159,164,169,178,190,192,193,203,226,232,242,243,256,],[80,80,116,128,128,128,128,128,128,128,128,128,128,128,80,128,128,128,128,128,80,128,80,128,80,]),'while_statement':([62,70,169,226,242,256,],[86,86,86,86,86,86,]),'for_statement':([62,70,169,226,242,256,],[87,87,87,87,87,87,]),'texp':([62,70,102,108,110,113,130,135,138,144,169,178,190,192,193,203,226,232,242,243,256,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,216,88,88,88,88,88,88,]),'gexp':([62,70,102,108,110,113,130,135,138,144,169,178,190,192,193,203,226,232,242,243,256,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'mexp':([62,70,102,108,110,113,130,135,138,144,150,159,169,178,190,192,193,203,226,232,242,243,256,],[92,92,92,92,92,92,92,92,92,92,194,195,92,92,92,92,92,92,92,92,92,92,92,]),'term':([62,70,102,108,110,113,130,135,138,144,150,159,164,169,178,190,192,193,203,226,232,242,243,256,],[93,93,93,93,93,93,93,93,93,93,93,93,196,93,93,93,93,93,93,93,93,93,93,93,]),'fact':([62,70,102,108,110,113,130,135,138,144,150,159,164,169,178,190,192,193,203,226,232,242,243,256,],[94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'call_func_exp':([62,70,102,108,110,113,130,135,138,144,150,159,164,169,178,190,192,193,203,226,232,242,243,256,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'cte':([62,70,102,108,110,113,130,135,138,144,150,159,164,169,178,190,192,193,203,226,232,242,243,256,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'add_fake':([68,111,112,131,185,199,223,244,],[102,135,138,178,138,178,232,178,]),'id_quad':([80,116,128,],[105,145,172,]),'call_func_era':([81,129,],[106,173,]),'id1':([81,117,129,],[107,107,107,]),'generate_quad_1':([88,],[114,]),'generate_quad_2':([91,],[118,]),'generate_quad_3':([92,],[119,]),'generate_quad_4':([93,],[120,]),'generate_quad_5':([94,],[121,]),'add_cte_char':([97,],[122,]),'add_cte_float':([98,],[123,]),'add_cte_int':([99,],[124,]),'start_func':([100,],[125,]),'read_args':([111,],[134,]),'write_args':([112,],[136,]),'write_args2':([112,185,],[137,210,]),'op1':([114,],[141,]),'breadcrumb':([115,236,],[144,243,]),'op2':([118,],[146,]),'op3aux':([119,],[149,]),'op3':([119,],[150,]),'op4aux':([120,],[158,]),'op4':([120,],[159,]),'op5aux':([121,],[163,]),'op5':([121,],[164,]),'args':([131,199,],[175,218,]),'args1':([131,199,244,],[176,176,251,]),'write_args1':([137,210,],[184,225,]),'add_cte_string':([139,],[188,]),'add_operator':([142,147,],[190,193,]),'remove_fake':([171,182,187,220,240,],[198,208,211,230,245,]),'id2':([179,],[204,]),'exp_type':([189,214,250,],[212,227,255,]),'param_check':([202,],[220,]),'read_args1':([208,245,],[222,252,]),'for_id':([215,],[228,]),'do_statement':([227,255,],[234,257,]),'args2':([230,],[237,]),'next_arg':([238,],[244,]),'decision_statement1':([241,],[246,]),'else_jump':([247,],[253,]),}

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
  ('dec_id -> ID add_id dec_id1','dec_id',3,'p_dec_id','parser_lexer.py',291),
  ('dec_id1 -> L_SB CTE_I set_array R_SB dec_id2','dec_id1',5,'p_dec_id1','parser_lexer.py',295),
  ('dec_id1 -> empty','dec_id1',1,'p_dec_id1','parser_lexer.py',296),
  ('dec_id2 -> L_SB CTE_I set_array R_SB','dec_id2',4,'p_dec_id2','parser_lexer.py',300),
  ('dec_id2 -> empty','dec_id2',1,'p_dec_id2','parser_lexer.py',301),
  ('add_id -> <empty>','add_id',0,'p_add_id','parser_lexer.py',304),
  ('set_array -> <empty>','set_array',0,'p_set_array','parser_lexer.py',324),
  ('id -> ID id1','id',2,'p_id','parser_lexer.py',333),
  ('id1 -> L_SB expression R_SB id2','id1',4,'p_id1','parser_lexer.py',339),
  ('id1 -> empty','id1',1,'p_id1','parser_lexer.py',340),
  ('id2 -> L_SB expression R_SB','id2',3,'p_id2','parser_lexer.py',344),
  ('id2 -> empty','id2',1,'p_id2','parser_lexer.py',345),
  ('var_type -> type','var_type',1,'p_var_type','parser_lexer.py',349),
  ('function -> FUNC func_type ID register_func L_P params R_P add_params var_declaration start_func L_B statements R_B','function',13,'p_function','parser_lexer.py',353),
  ('register_func -> <empty>','register_func',0,'p_register_func','parser_lexer.py',367),
  ('add_params -> <empty>','add_params',0,'p_add_params','parser_lexer.py',381),
  ('start_func -> <empty>','start_func',0,'p_start_func','parser_lexer.py',387),
  ('func_type -> VOID','func_type',1,'p_func_type','parser_lexer.py',393),
  ('func_type -> type','func_type',1,'p_func_type','parser_lexer.py',394),
  ('params -> var_type param_type dec_id params1','params',4,'p_params','parser_lexer.py',401),
  ('params -> empty','params',1,'p_params','parser_lexer.py',402),
  ('param_type -> <empty>','param_type',0,'p_param_type','parser_lexer.py',406),
  ('params1 -> COMA params','params1',2,'p_params1','parser_lexer.py',413),
  ('params1 -> empty','params1',1,'p_params1','parser_lexer.py',414),
  ('statements -> statement statements','statements',2,'p_statements','parser_lexer.py',418),
  ('statements -> empty','statements',1,'p_statements','parser_lexer.py',419),
  ('statement -> assignation','statement',1,'p_statement','parser_lexer.py',423),
  ('statement -> call_func','statement',1,'p_statement','parser_lexer.py',424),
  ('statement -> return_func','statement',1,'p_statement','parser_lexer.py',425),
  ('statement -> read','statement',1,'p_statement','parser_lexer.py',426),
  ('statement -> write','statement',1,'p_statement','parser_lexer.py',427),
  ('statement -> decision_statement','statement',1,'p_statement','parser_lexer.py',428),
  ('statement -> repetition_statement','statement',1,'p_statement','parser_lexer.py',429),
  ('statement -> expression','statement',1,'p_statement','parser_lexer.py',430),
  ('assignation -> id id_quad EQUAL expression SEMICOLON','assignation',5,'p_assignation','parser_lexer.py',434),
  ('args -> args1','args',1,'p_args','parser_lexer.py',449),
  ('args -> empty','args',1,'p_args','parser_lexer.py',450),
  ('args1 -> add_fake expression param_check remove_fake args2','args1',5,'p_args1','parser_lexer.py',454),
  ('param_check -> <empty>','param_check',0,'p_param_check','parser_lexer.py',458),
  ('args2 -> COMA next_arg args1','args2',3,'p_args2','parser_lexer.py',473),
  ('args2 -> empty','args2',1,'p_args2','parser_lexer.py',474),
  ('next_arg -> <empty>','next_arg',0,'p_next_arg','parser_lexer.py',478),
  ('call_func -> ID call_func_era L_P args R_P SEMICOLON','call_func',6,'p_call_func','parser_lexer.py',484),
  ('call_func_exp -> ID call_func_era L_P args R_P','call_func_exp',5,'p_call_func_exp','parser_lexer.py',495),
  ('call_func_era -> <empty>','call_func_era',0,'p_call_func_era','parser_lexer.py',518),
  ('return_func -> RETURN L_P expression R_P SEMICOLON','return_func',5,'p_return_func','parser_lexer.py',529),
  ('read -> READ L_P read_args R_P SEMICOLON','read',5,'p_read','parser_lexer.py',539),
  ('read_args -> add_fake expression remove_fake read_args1','read_args',4,'p_read_args','parser_lexer.py',548),
  ('read_args1 -> COMA add_fake expression remove_fake read_args1','read_args1',5,'p_read_args1','parser_lexer.py',552),
  ('read_args1 -> empty','read_args1',1,'p_read_args1','parser_lexer.py',553),
  ('write -> PRINT L_P write_args R_P SEMICOLON','write',5,'p_write','parser_lexer.py',557),
  ('write_args -> write_args2 write_args1','write_args',2,'p_write_args','parser_lexer.py',561),
  ('write_args1 -> COMA write_args2 write_args1','write_args1',3,'p_write_args1','parser_lexer.py',565),
  ('write_args1 -> empty','write_args1',1,'p_write_args1','parser_lexer.py',566),
  ('write_args2 -> add_fake expression remove_fake','write_args2',3,'p_write_args2','parser_lexer.py',570),
  ('write_args2 -> CTE_STRING add_cte_string','write_args2',2,'p_write_args2','parser_lexer.py',571),
  ('decision_statement -> IF L_P expression R_P exp_type L_B statements R_B decision_statement1','decision_statement',9,'p_decision_statement','parser_lexer.py',579),
  ('decision_statement1 -> ELSE else_jump L_B statements R_B','decision_statement1',5,'p_decision_statement1','parser_lexer.py',586),
  ('decision_statement1 -> empty','decision_statement1',1,'p_decision_statement1','parser_lexer.py',587),
  ('exp_type -> <empty>','exp_type',0,'p_exp_type','parser_lexer.py',591),
  ('else_jump -> <empty>','else_jump',0,'p_else_jump','parser_lexer.py',603),
  ('repetition_statement -> while_statement','repetition_statement',1,'p_repetition_statement','parser_lexer.py',612),
  ('repetition_statement -> for_statement','repetition_statement',1,'p_repetition_statement','parser_lexer.py',613),
  ('for_statement -> FOR id id_quad EQUAL expression for_id TO breadcrumb expression exp_type do_statement','for_statement',11,'p_for_statement','parser_lexer.py',617),
  ('for_id -> <empty>','for_id',0,'p_for_id','parser_lexer.py',643),
  ('breadcrumb -> <empty>','breadcrumb',0,'p_breadcrumb','parser_lexer.py',659),
  ('while_statement -> WHILE L_P breadcrumb expression R_P exp_type do_statement','while_statement',7,'p_while_statement','parser_lexer.py',665),
  ('do_statement -> DO L_B statements R_B','do_statement',4,'p_do_statement','parser_lexer.py',674),
  ('expression -> texp generate_quad_1 op1','expression',3,'p_expression','parser_lexer.py',678),
  ('texp -> gexp generate_quad_2 op2','texp',3,'p_texp','parser_lexer.py',682),
  ('gexp -> mexp generate_quad_3 op3aux','gexp',3,'p_gexp','parser_lexer.py',686),
  ('mexp -> term generate_quad_4 op4aux','mexp',3,'p_mexp','parser_lexer.py',690),
  ('term -> fact generate_quad_5 op5aux','term',3,'p_term','parser_lexer.py',694),
  ('generate_quad_1 -> <empty>','generate_quad_1',0,'p_generate_quad_1','parser_lexer.py',698),
  ('generate_quad_2 -> <empty>','generate_quad_2',0,'p_generate_quad_2','parser_lexer.py',705),
  ('generate_quad_3 -> <empty>','generate_quad_3',0,'p_generate_quad_3','parser_lexer.py',712),
  ('generate_quad_4 -> <empty>','generate_quad_4',0,'p_generate_quad_4','parser_lexer.py',719),
  ('generate_quad_5 -> <empty>','generate_quad_5',0,'p_generate_quad_5','parser_lexer.py',726),
  ('fact -> id id_quad','fact',2,'p_fact','parser_lexer.py',733),
  ('fact -> call_func_exp','fact',1,'p_fact','parser_lexer.py',734),
  ('fact -> L_P add_fake expression R_P remove_fake','fact',5,'p_fact','parser_lexer.py',735),
  ('fact -> cte','fact',1,'p_fact','parser_lexer.py',736),
  ('add_fake -> <empty>','add_fake',0,'p_add_fake','parser_lexer.py',740),
  ('remove_fake -> <empty>','remove_fake',0,'p_remove_fake','parser_lexer.py',746),
  ('id_quad -> <empty>','id_quad',0,'p_id_quad','parser_lexer.py',753),
  ('cte -> CTE_CHAR add_cte_char','cte',2,'p_cte','parser_lexer.py',773),
  ('cte -> CTE_F add_cte_float','cte',2,'p_cte','parser_lexer.py',774),
  ('cte -> CTE_I add_cte_int','cte',2,'p_cte','parser_lexer.py',775),
  ('add_cte_int -> <empty>','add_cte_int',0,'p_add_cte_int','parser_lexer.py',779),
  ('add_cte_float -> <empty>','add_cte_float',0,'p_add_cte_float','parser_lexer.py',794),
  ('add_cte_char -> <empty>','add_cte_char',0,'p_add_cte_char','parser_lexer.py',809),
  ('add_cte_string -> <empty>','add_cte_string',0,'p_add_cte_string','parser_lexer.py',824),
  ('add_operator -> <empty>','add_operator',0,'p_add_operator','parser_lexer.py',839),
  ('op1 -> OR add_operator expression','op1',3,'p_op1','parser_lexer.py',845),
  ('op1 -> empty','op1',1,'p_op1','parser_lexer.py',846),
  ('op2 -> AND add_operator texp','op2',3,'p_op2','parser_lexer.py',850),
  ('op2 -> empty','op2',1,'p_op2','parser_lexer.py',851),
  ('op3 -> LESSTHAN','op3',1,'p_op3','parser_lexer.py',855),
  ('op3 -> LESSTHANEQ','op3',1,'p_op3','parser_lexer.py',856),
  ('op3 -> GREATERTHAN','op3',1,'p_op3','parser_lexer.py',857),
  ('op3 -> GREATERTHANEQ','op3',1,'p_op3','parser_lexer.py',858),
  ('op3 -> EQ','op3',1,'p_op3','parser_lexer.py',859),
  ('op3 -> DIFERENT','op3',1,'p_op3','parser_lexer.py',860),
  ('op3aux -> op3 mexp','op3aux',2,'p_op3aux','parser_lexer.py',866),
  ('op3aux -> empty','op3aux',1,'p_op3aux','parser_lexer.py',867),
  ('op4 -> PLUS','op4',1,'p_op4','parser_lexer.py',871),
  ('op4 -> MINUS','op4',1,'p_op4','parser_lexer.py',872),
  ('op4aux -> op4 mexp','op4aux',2,'p_op4aux','parser_lexer.py',878),
  ('op4aux -> empty','op4aux',1,'p_op4aux','parser_lexer.py',879),
  ('op5 -> MULT','op5',1,'p_op5','parser_lexer.py',883),
  ('op5 -> DIV','op5',1,'p_op5','parser_lexer.py',884),
  ('op5 -> MOD','op5',1,'p_op5','parser_lexer.py',885),
  ('op5aux -> op5 term','op5aux',2,'p_op5aux','parser_lexer.py',891),
  ('op5aux -> empty','op5aux',1,'p_op5aux','parser_lexer.py',892),
  ('empty -> <empty>','empty',0,'p_empty','parser_lexer.py',897),
]
