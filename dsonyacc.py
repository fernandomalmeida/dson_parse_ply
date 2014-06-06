import ply.yacc as yacc

from dsonlex import tokens

#def p_empty(p):
#	'empty :'
#	p[0] = None
#empty	:

def p_object(p):
	'''object : SUCH objectValue WOW'''
	p[0] = p[2]
#object	: SUCH objectValue WOW

def p_objectValue(p):
	'''objectValue	: 
					| STRING IS value
					| objectValue NEXT STRING IS value'''
	p[0] = {}
	if len(p) == 4:
		p[0][p[1]] = p[3]
	elif len(p) == 6:
		p[0] = p[1]
		p[0][p[3]] = p[5]
#objectValue	: empty
#			| STRING IS value
#			| objectValue NEXT STRING IS value

def p_array(p):
	'''array	: SO arrayValue MANY'''
	p[0] = p[2]
#array	: SO arrayValue MANY

def p_arrayValue(p):
	'''arrayValue	: 
					| value
					| arrayValue NEXT value'''
	p[0] = []
	if len(p) == 2:
		p[0].append(p[1])
	elif len(p) == 4:
		p[0].extend(p[1])
		p[0].append(p[3])
#arrayValue	: empty
#			| value
#			| arrayValue NEXT value

def p_value(p):
	'''value	: STRING
				| NUMBER
				| object
				| array
				| NOTFALSE
				| NOTTRUE
				| NULLISH'''
	p[0] = p[1]
#value	: STRING
#		| NUMBER
#		| object
#		| array
#		| NOTFALSE
#		| NOTTRUE
#		| NULLISH

def p_error(p):
	print "Syntax error", p.lineno

#parser = yacc.yacc(start='programa')
parser = yacc.yacc(start='object')

def printParse(input):
	result = parser.parse(input)

	print result

if __name__ == '__main__':
	import json

	printParse('such "foo" is "bar" wow')
	print ''
	printParse('such "foo" is so "bar" next "baz" next "fizzbuzz" many wow')
	print ''
	printParse('such "foo" is 42very3 wow')

	#print json.dumps(result)