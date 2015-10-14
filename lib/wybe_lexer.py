from UtopiaLexer import lexer

STRING = 'str'
INDEX = 'ind'
NAME = 'name'
CALL = 'call'
BRACK = 'bracket'
SEP = 'separator'
TO = 'to'


def lex(script):
    lexr = lexer()

    lexr.add_token_expr(r'^"[^"\\]*(?:\\.[^"\\]*)*"', STRING, (1, -1, 1))
    lexr.add_token_expr(r'^[\s]', None)
    lexr.add_token_expr(r'^\[[^\]]*\]', INDEX, (1, -1, 1))
    lexr.add_token_expr(r'[[{\]}]', BRACK)
    lexr.add_token_expr(r',', SEP)
    lexr.add_token_expr(r':', TO)
    lexr.add_token_expr(r'^`', CALL, (1, None, 1))
    lexr.add_token_expr(r'^[^\s]*', NAME)

    return lexr.lex(script)


if __name__ == '__main__':
    print(lex(input()))