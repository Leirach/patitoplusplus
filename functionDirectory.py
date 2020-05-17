
# 
# functionName: {
#       type: 'void',
#       paramsInfo: {'paramId': 'type'},
#       numParams: 1,
#       paramsOrder: ['type']
#       vars: {'varId': 'type'},
# }

functionsDirectory = { 
}

#add function to Directory
def addFunction(functionName, functionType):
    if functionName in functionsDirectory: 
        print("Función duplicada") #No stoi segura de que aquí se haga esta validación??
        return False #función ya existe
    else:
        function = {
            functionName : {'type': functionType, 'numParams': 0, 'paramsInfo': {}, 'paramsOrder': [], 'vars': {}},
        }
        functionsDirectory.update(function)
        return True

#add function to Directory
def addParam(functionName, paramId, paramType):
    if functionName in functionsDirectory: #Si la función existe
        if functionsDirectory[functionName]['paramsInfo'].get(paramId) == None: ## ??? no estoy segura de si se hace esta validación aquí o nel
            functionsDirectory[functionName]['numParams'] = functionsDirectory[functionName]['numParams'] + 1
            functionsDirectory[functionName]['paramsInfo'].update({paramId: paramType})
            functionsDirectory[functionName]['paramsOrder'].append(paramType)
            return True 
        else:
            print("Id de parámetro duplicado")
            return False
    else:
        print("Función no existe")
        return False

#add function to Directory
def addVar(functionName, varId, varType):
    if functionName in functionsDirectory: #Si la función existe
        if functionsDirectory[functionName]['vars'].get(varId) == None: ## ??? no estoy segura de si se hace esta validación aquí o nel
            functionsDirectory[functionName]['vars'].update({varId: varType})
            return True 
        else:
            print("Id duplicado")
            return False #Variable ya existe
    else:
        print("Función no existe")
        return False
    
'''functionName = 'main'
functionType = 'void'
param = 'x'
paramType = 'int'
print("........Empty dictionary.......")    
print(functionsDirectory)
print("........Adding Function to dictionary.......")  
addFunction(functionName, functionType)
print("........Function added.......")  
print(functionsDirectory)
print("........Adding param to function .......")  
addParam(functionName, param, paramType)
print("........Added param to function .......")  
print(functionsDirectory)
print("........Adding param to function .......")  
addParam(functionName, 'Y', paramType)
print("........Added param to function .......")  
print(functionsDirectory)
print("........Adding param to function .......")  
addParam(functionName, 'Y', paramType)
print("........Adding var to function .......")  
addVar(functionName, 'aux', 'bool')
print("........Added var to function .......")  
print("........Adding var to function .......")  
addVar(functionName, 'aux', 'bool')
print(functionsDirectory)
print("........Adding var to function .......")  
addVar(functionName, 'pop', 'float')
print("........Added var to function .......")  
print(functionsDirectory)
print("........Adding function .......")  
addFunction(functionName, functionType)
print(functionsDirectory)
print("........Adding function .......")  
addFunction('popRockCallejero', functionType)
print("........Added function .......")  
print(functionsDirectory)'''