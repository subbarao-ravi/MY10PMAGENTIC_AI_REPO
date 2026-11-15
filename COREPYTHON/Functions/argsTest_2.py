def defaultargs(number, name='DURGA'):
    pass

defaultargs(20,'RAMA')
defaultargs(10)
defaultargs(20,name='SIVA')
#defaultargs(name='SIVA',20)


def varArgs(*n):
    pass

varArgs()
varArgs(10,20,30)
varArgs(10,20,'RAMA')

def varArgsCombo_1(name, *n):
    pass

varArgsCombo_1('RAMA','SITA')

def varArgsCombo_2(*n, name):
    pass

varArgsCombo_2('RAMA',name='SITA')

def keywordVarArgs(**kwargs):
    print(kwargs.items())

keywordVarArgs()
keywordVarArgs(a=10,b=20,c=30,d=40)