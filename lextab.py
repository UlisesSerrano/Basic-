# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('AMP', 'AND', 'CHAR', 'COMA', 'CTE_CHAR', 'CTE_F', 'CTE_I', 'CTE_NEG_I', 'CTE_STRING', 'DIFERENT', 'DIV', 'DO', 'ELSE', 'EQ', 'EQUAL', 'FLOAT', 'FOR', 'FUNC', 'GREATERTHAN', 'GREATERTHANEQ', 'ID', 'IF', 'INT', 'LESSTHAN', 'LESSTHANEQ', 'L_B', 'L_P', 'L_SB', 'MAIN', 'MINUS', 'MOD', 'MULT', 'OR', 'PLUS', 'PRINT', 'PROGRAM', 'READ', 'RETURN', 'R_B', 'R_P', 'R_SB', 'SEMICOLON', 'TO', 'VAR', 'VOID', 'WHILE'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_newline>\\n+)|(?P<t_ID>[a-zA-Z][a-zA-Z_\\d]*)|(?P<t_CTE_F>\\d*\\.\\d+)|(?P<t_CTE_I>\\d+)|(?P<t_CTE_NEG_I>-\\d+)|(?P<t_CTE_STRING>\\"([^\\\\\\n]|(\\\\.))*?\\")|(?P<t_CTE_CHAR>(\\\'[^\\\']*\\\'))|(?P<t_AND>\\&\\&)|(?P<t_OR>\\|\\|)|(?P<t_EQ>\\=\\=)|(?P<t_GREATERTHANEQ>\\>\\=)|(?P<t_LESSTHANEQ>\\<\\=)|(?P<t_DIFERENT>\\!\\=)|(?P<t_MINUS>\\-)|(?P<t_PLUS>\\+)|(?P<t_MULT>\\*)|(?P<t_DIV>\\/)|(?P<t_MOD>\\%)|(?P<t_SEMICOLON>\\;)|(?P<t_L_P>\\()|(?P<t_R_P>\\))|(?P<t_COMA>\\,)|(?P<t_L_B>\\{)|(?P<t_R_B>\\})|(?P<t_L_SB>\\[)|(?P<t_R_SB>\\])|(?P<t_GREATERTHAN>\\>)|(?P<t_LESSTHAN>\\<)|(?P<t_EQUAL>\\=)|(?P<t_AMP>\\&)', [None, ('t_newline', 'newline'), ('t_ID', 'ID'), ('t_CTE_F', 'CTE_F'), ('t_CTE_I', 'CTE_I'), ('t_CTE_NEG_I', 'CTE_NEG_I'), ('t_CTE_STRING', 'CTE_STRING'), None, None, ('t_CTE_CHAR', 'CTE_CHAR'), None, (None, 'AND'), (None, 'OR'), (None, 'EQ'), (None, 'GREATERTHANEQ'), (None, 'LESSTHANEQ'), (None, 'DIFERENT'), (None, 'MINUS'), (None, 'PLUS'), (None, 'MULT'), (None, 'DIV'), (None, 'MOD'), (None, 'SEMICOLON'), (None, 'L_P'), (None, 'R_P'), (None, 'COMA'), (None, 'L_B'), (None, 'R_B'), (None, 'L_SB'), (None, 'R_SB'), (None, 'GREATERTHAN'), (None, 'LESSTHAN'), (None, 'EQUAL'), (None, 'AMP')])]}
_lexstateignore = {'INITIAL': ' \t\r\n'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
