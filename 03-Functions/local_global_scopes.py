# There are four rules to tell whether a variable is in a local scope or global scope:

# If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

# If there is a global statement for that variable in a function, it is a global variable.

# Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

# But if the variable is not used in an assignment statement, it is a global variable.

def spam():
  global eggs
  eggs = 'spam' # this is now a global variable

def bacon():
  eggs = 'bacon' # this is a local
  return eggs

def ham():
  print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)
print(bacon())