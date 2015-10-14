from UtopiaLexer import lexer

STRING = 'str'
INDEX = 'ind'
NAME = 'name'
RAWNAME = 'rn'
CALL = 'call'
SHORTCALL = 'scall'
BRACK = 'bracket'
SEP = 'separator'
TO = 'to'


def lex(script):
    lexr = lexer()

    lexr.add_token_expr(r'^"[^"\\]*(?:\\.[^"\\]*)*"', STRING, (1, -1, 1))
    lexr.add_token_expr(r'^[\s]', None)
    lexr.add_token_expr(r'^\[[^\]]*\]', INDEX, (1, -1, 1))
    lexr.add_token_expr(r'[[{\]}]', BRACK)
    # lexr.add_token_expr(r',', SEP)
    # lexr.add_token_expr(r':', TO)
    lexr.add_token_expr(r'^[a-zA-Z_][a-zA-Z0-9_]*', NAME)
    lexr.add_token_expr(r'^\\[a-zA-Z_][a-zA-Z0-9_]*', RAWNAME, (1, None, 1))
    lexr.add_token_expr(r'^`[a-zA-Z_][a-zA-Z0-9_]*', SHORTCALL, (1, None, 1))
    lexr.add_token_expr(r'^[\s]*', CALL)

    return lexr.lex(script)


if __name__ == '__main__':
    print(lex(input()))