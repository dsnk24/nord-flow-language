class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        
    def parse(self):
        for token in self.tokens:
            token_type = token[0]
            token_value = token[1]

            if token_type == "VAR_DECLARATION" and token_value == "var":
                self.parse_var_declaration(self.tokens[self.tokens.index(token):len(self.tokens)])
    
    def parse_var_declaration(self, token_stream):
        for token in token_stream:
            token_type = token[0]
            token_value = token[1]

            if token_stream.index(token) == 0:
                print(f'Variable Type: {token_value}')

            