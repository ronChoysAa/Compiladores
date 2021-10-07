# ------------------------------------------------------------
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
Reservadas = {'y': 'and', 'logico': 'bool', 'romper': 'break', 'caso': 'case', 'capturar': 'catch', 
'caracter': 'type_char', 'clase': 'class', 'constante': 'const', 'continuar': 'continue', 
'borrar': 'delete', 'hacer': 'do', 'predet': 'default', 'sino': 'else', 'Falso': 'false', 
'flotante': 'type_float', 'para': 'for', 'si': 'if', 'entero': 'type_int', 'no': 'not', 'o': 'or', 
'retornar': 'func_return', 'Verdadero': 'true', 'mientras': 'while'}

# List of token names. This is always required
tokens = ['identificador','numeral','oper_igua', 'oper_sum','oper_sus', 'oper_mult', 'oper_div', 'oper_res',
            'parI','parD','corI', 'corD', 'llaI', 'llaD', 'oper_may','oper_men', 'oper_no','puntocoma'] + list(Reservadas.values())
# Regular expression rules for simple tokens
t_oper_igua = r'='
t_oper_sum = r'\+'
t_oper_sus = r'-'
t_oper_mult= r'\*'
t_oper_div = r'/'
t_oper_res = r'%'
t_parI = r'\('
t_parD = r'\)'
t_corI = r'\['
t_corD = r'\]'
t_llaI = r'\{'
t_llaD = r'\}'
t_oper_may= r'>'
t_oper_men = r'<'
t_oper_no = r'!'
t_puntocoma = r';'
# A regular expression rule with some action code
def t_identificador(t):
    r'[a-zA-Z]+ ( [a-zA-Z0-9]* )'    
    t.type = Reservadas.get(t.value,'identificador')    # Check for reserved words
    return t

def t_numeral(t):
    r'\d+'
    t.value = int(t.value) # guardamos el valor del lexema
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character ’ %s’" % t.value[0])
    t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()
# Test it out
f = open("Ejemplo 3.txt", "r")
data = f.read()
f.close()
# Give the lexer some input
lexer.input(data)   


if __name__ == "__main__":
    while True:
        tok = lexer.token()
        if tok is None:
            break
        print ('Tipo:',tok.type,'    Valor: ', tok.value, '    ', tok.lineno, tok.lexpos)
