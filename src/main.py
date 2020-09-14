import lexer
import code_parser


def main():
    content = ""

    with open('test.nord', 'r') as f:
        content = f.read()
    
    _lexer = lexer.Lexer(content)

    tokens = _lexer.tokenize()

    _parser = code_parser.Parser(tokens)

    _parser.parse()



if __name__ == "__main__":
    main()