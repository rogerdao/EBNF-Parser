import re
from functools import *

class recDescent:


    # constructor to initialize and set class level variables
    def __init__(self, expr = ""):

        # string to be parsed
        self.expr = expr

        # tokens from lexer tokenization of the expression
        self.tokens = []

    # lexer - tokenize the expression into a list of tokens
    # the tokens are stored in an list which can be accessed by self.tokens

    def lex(self):
        self.tokens = re.findall("[-\(\)]|[!<>=]=|[<>]|\w+|[^ +]\W+", self.expr)
        # transform tokens to lower case, and filter out possible spaces in the tokens
        self.tokens = list(filter((lambda x: len(x)), 
                           list(map((lambda x: x.strip().lower()), self.tokens))))    
    
    # parser - determine if the input expression is valid or not
    
    # validate() function will return True if the expression is valid, False otherwise 

    def validate(self):
        # Using the tokens from lex() tokenization,
        # this validate would first call lex() to tokenize the expression,
        # then call the top level parsing procedure for the outermost rule
        # and go from there
        
        self.lex()
        try:
            valid = self.parse_expression()
            # Must consume all tokens (no leftovers)
            return valid and not self.tokens
        except:
            return False
    
    # <expression> -> <term> { <logop> <term> }                     # EXPR: TERM {LOGOP TERM{
    def parse_expression(self):
        # just the first term
        if not (self.tokens and self.parse_term()):                 #       TERM
            return False

        # burn the rest, the while is more terms connected with and or nand 0-N TIMES (LOGOP, TERM)
        while self.tokens and self.tokens[0] in {'and', 'or', 'nand'}:          # LOGOP + TERM, (INDEX IS LOGOP)
            self.tokens.pop(0)  # iterate
            if not (self.tokens and self.parse_term()):                         # IS TERM??
                return False
        return True                                                 # 0-N: TERM {LOGOP, TERM}

    # <term> -> <range> | <relop> | (<expr>)                        # TERM: int-int / RELOP/ (EXPR)
    def parse_term(self):
        if not self.tokens:
            return False
                                                                    # of format (<expr>)
        if self.tokens[0] == '(':                                   # (  singular term
            self.tokens.pop(0)
            if not self.parse_expression():                         # (EXPR
                return False
            if not (self.tokens and self.tokens[0] == ')'   ):      # (EXPR)
                return False
            self.tokens.pop(0)
            return True                                             # (EXPR)

        return self.parse_intDashInt() or self.parse_relopInt()         # call other 2 cases

    # <int-int> -> <int> dash <int>
    def parse_intDashInt(self):                                         # of format int - int
        if not self.parse_int(): # INT                                  # int
            return False

        if not (self.tokens and self.tokens[0] == '-'): # DASH          # int -
            return False
        self.tokens.pop(0)

        if not self.parse_int(): # INT                                  # int - int
            return False
        return True

    # <relopInt> -> <relop> <int>                               # this is because int is always following a relop
    def parse_relopInt(self):                                   # needs to be in oreder RELOP INT, so cal lboth
        if not self.parse_relop():                              # call relop
            return False
        if not self.parse_int():                                # call int
            return False
        return True

    # <relop> -> '<' | '>' | '<=' | '>=' | '==' | '!=' | 'not'
    def parse_relop(self):                                      # parse singlar relop
        if not self.tokens:
            return False
        if self.tokens[0] in {'<', '>', '<=', '>=', '==', '!=', 'not'}:
            self.tokens.pop(0)
            return True
        return False

    # <int> -> digit{digit} but im lazy
    def parse_int(self):                                        # parse singular int (full number ,pos)
        if not self.tokens:
            return False
        if self.tokens[0].isdigit():  # isdigt goes for positive values too
            self.tokens.pop(0)
            return True
        return False  
