import re

class Lexer(object):
    def __init__(self, src_code) -> None:
        self.src_code = src_code
    
    def tokenize(self):
        tokens = []

        source = self.src_code.split()

        for word in source:
            if word == 'var':
                tokens.append(['VAR_DECLARATION', word])
            
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[-1] == ';':
                    tokens.append(['IDENTIFIER', word[0:len(word)-1]])
                else:
                    tokens.append(['IDENTIFIER', word])

            elif re.match('[0-9]', word):
                if word[-1] == ';':
                    tokens.append(['INTEGER', word[0:len(word)-1]])
                else:
                    tokens.append(['INTEGER', word])
            
            elif word in '=+-/*':
                tokens.append(['OPERATOR', word])
            

            if word[-1] == ';':
                tokens.append(['STATEMENT_END', ';'])

        print(tokens)
        
        return tokens