
A LL(1) recursive descent parser for validating simple expressions.

grammar rules (non-terminals) in EBNF  
recursive descent parsing procedures for validating expressions


one parsing procedure for each one of the non-terminals (grammar rules),  
starting from the top of the parse tree, then into lower hierachical levels.

The procedures work together to handle all combinations of the grammar  
rules, and they automatically handle the nested compositions of terms  
with multi-level priority brackets. 

----------------------------------------------------------------------------
Usage (more cases below)

r = recDecsent('7 - 17')  
print(r.validate()) # will print True as '7 - 17' is a valid expression

r = recDecsent('7 - ')  
print(r.validate()) # will print False as '7 - ' is an invalid expression

----------------------------------------------------------------------------
Follows are examples of valid expressions based on the expression patterns specified above:  
•	7 - 17  
•	> 90  
•	(1 - 100 and not 50) or > 200  
•	(7 - 17) or > 90  
•	> 50 or == 20  
•	1 - 100 and != 50  
•	(5 - 100) and (not 50) or (>= 130 or (2 - 4))

Examples of invalid expressions:  
•	>  
•	2 - - 4  
•	- 7  
•	7 -  
•	= 6  
•	(!= 5) and  
•	2 - 4 and >< 300  
•	>= 5) nand < 10  


# sample test code
r = recDescent('5 - 100')  
print(r.validate()) # should return True

r = recDescent('5 - ')  
print(r.validate()) # should return False


# TRUE
r = recDescent('7 - 17')  
print(r.validate())

r = recDescent('> 90')  
print(r.validate())

r = recDescent('(1 - 100 and not 50) or > 200')  
print(r.validate())

r = recDescent('(7 - 17) or > 90')  
print(r.validate())

r = recDescent('> 50 or == 20')  
print(r.validate())

r = recDescent('1 - 100 and != 50')  
print(r.validate())

r = recDescent('(5 - 100) and (not 50) or (>= 130 or (2 - 4))')  
print(r.validate())


# FALSE
r = recDescent('>')  
print(r.validate())

r = recDescent('2 - - 4')  
print(r.validate())

r = recDescent('- 7')  
print(r.validate())

r = recDescent('7 -')  
print(r.validate())

r = recDescent('= 6')  
print(r.validate())

r = recDescent('(!= 5) and')  
print(r.validate())

r = recDescent('2 - 4 and >< 300')  
print(r.validate())

r = recDescent('>= 5) nand < 10')  
print(r.validate())
