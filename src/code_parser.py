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


            if token_type == 'STATEMENT_END': break


            if token_stream.index(token) == 0:
                print(f'Variable Type: {token_value}')

            elif token_stream.index(token) == 1 and token_type == 'IDENTIFIER':
                print(f'Variable Name: {token_value}')
            
            elif token_stream.index(token) == 1 and token_type != 'IDENTIFIER':
                print(f"ERROR: Invalid variable name '{token_value}'.")

                quit()
            
            elif token_stream.index(token) == 2 and token_type == 'OPERATOR':
                print(f"Assignment operator: {token_value}")
            
            elif token_stream.index(token) == 2 and token_type != 'OPERATOR':
                print(f"ERROR: Assignment operator '=' is missing.")

                quit()
            
            elif token_stream.index(token) == 3 and token_type in ['STRING', 'INTEGER']:
                print(f"Variable value: {token_value}")
            
            elif token_stream.index(token) == 3 and token_type not in ['STRING', 'INTEGER']:
                print(f"ERROR: Invalid variable assignment {token_value}")
            
                quit()