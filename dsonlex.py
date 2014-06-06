# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
import re

reserved = {
  'such':'SUCH',
  'is':'IS',
  'wow':'WOW',
  'so':'SO',
  'many':'MANY',
  'yes':'YES',
  'no':'NO',
  'empty':'EMPTY',
  'very':'VERY',
  'and':'AND',
  'also':'ALSO',
}

tokens = [
  'STRING',
  'NUMBER',
  'NEXTOBJECT',
  'IDENT'
  ] + list(reserved.values())

t_NEXTOBJECT = r'[,.!?]'

def t_STRING(t):
  r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'
  t.value = t.value[1:len(t.value)-1]
  return t

def t_NUMBER(t):
  r'(\-?)([1-9]\d*|0)(.\d+)?((very|VERY)[+-]?\d+)?'
  values = re.split('very|VERY', t.value)
  t.value = float(values[0])*10**float(values[1])
  #t.value = float(t.value)
  return t

def t_IDEN(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENT')    # Check for reserved words
    if t.type == 'YES':
      t.value = True
    elif t.type == 'NO':
      t.value = False
    elif t.type == 'EMPTY':
      t.value = None
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def printTokens(input):
  lexer.input(input)

  for token in lexer:
    print token

if __name__ == "__main__":

  printTokens('such "foo" is "bar". "doge" is "shibe" wow')
  print ''
  printTokens('such "foo" is such "shiba" is "inu", "doge" is yes wow wow')
  print ''
  printTokens('such "foo" is so "bar" also "baz" and "fizzbuzz" many wow')
  print ''
  printTokens('such "foo" is 42very3 wow')
