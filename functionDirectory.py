
# 
# functionName: {
#       type: 'void',
#       paramsInfo: {'paramId': 'type'},
#       numParams: 1,
#       paramsOrder: ['type']
#       vars: {'varId': 'type'},
# }
#TODO doble llamada de función
import exceptions as exception

functionsDirectory = { 'globals': {'type': 'void', 'numParams': 0, 'paramsInfo': {}, 'paramsOrder': [], 'vars': {}},
}

#add function to Directory
def addFunction(functionName, functionType):
    if functionName in functionsDirectory: 
        #No stoi segura de que aquí se haga esta validación??
        exception.throwError("Función '%s' fue definida anteriormente." % (functionName))
        return False #función ya existe
    else:
        function = {
            functionName : {'type': functionType, 'numParams': 0, 'paramsInfo': {}, 'paramsOrder': [], 'vars': {}},
        }
        functionsDirectory.update(function)
        print("Se agregó función")
        print(functionsDirectory)
        return True

#add function to Directory
def addParam(functionName, paramId, paramType):
    if functionName == None:
        functionName = list(functionsDirectory.keys())[-1]
    if functionName in functionsDirectory: #Si la función existe
        if functionsDirectory[functionName]['paramsInfo'].get(paramId) == None: ## ??? no estoy segura de si se hace esta validación aquí o nel
            if functionName == None:
                functionName = list(functionsDirectory.keys())[-1]
            functionsDirectory[functionName]['numParams'] = functionsDirectory[functionName]['numParams'] + 1
            functionsDirectory[functionName]['paramsInfo'].update({paramId: paramType})
            functionsDirectory[functionName]['paramsOrder'].append(paramType)
            print("Se agregó parámetro")
            print(functionsDirectory)
            return True 
        else:
            exception.throwError("ID '%s' duplicado en parámetros de función '%s'" % (paramId, functionName))
            return False
    else:
        exception.throwError("Función '%s' no existe" % (functionName))
        return False

#add function to Directory
def addVar(functionName, varId, varType):
    if functionName == None:
        functionName = list(functionsDirectory.keys())[-1]
    if functionName in functionsDirectory: #Si la función existe
        if functionsDirectory[functionName]['vars'].get(varId) == None: ## ??? no estoy segura de si se hace esta validación aquí o nel
            if varType == None:
                varType = functionsDirectory[functionName]['vars'][list(functionsDirectory[functionName]['vars'].keys())[-1]]
            functionsDirectory[functionName]['vars'].update({varId: varType})
            print("Se agregó a tabla de variables")
            print(functionsDirectory)
            return True 
        else:
            exception.throwError("ID '%s' duplicado en función '%s'" % (varId, functionName))
    else:
        exception.throwError("Función '%s' no existe" % (functionName))

def getVariableType(functionName, variable):
    if functionName in functionsDirectory: #Si la función existe
        print("Función existe")
        print(variable)
        if variable in functionsDirectory[functionName]["vars"]:
            varType = functionsDirectory[functionName]["vars"][variable]
            return varType
        else:
            if variable in functionsDirectory['globals']["vars"]:
                print(functionsDirectory['globals']["vars"][variable])
                varType = functionsDirectory['globals']["vars"][variable]
                return varType
            else:
                exception.throwError("Variable '%s' no existe en este scope" % (variable))
    else:
        exception.throwError("Función '%s' no existe" % (functionName))

def validateFunctionSemantics(functionName):
    if functionName in functionsDirectory: #Si la función existe
        print("Función existe")
        if functionName+"Call" in functionsDirectory:
            print("Llamada generada")
            funcParams = functionsDirectory[functionName]["numParams"]
            funcCallParams = functionsDirectory[functionName+"Call"]["numParams"]
            if funcParams == funcCallParams:
                print("Número de parámetros correcto")
                funcParamOrder = functionsDirectory[functionName+"Call"]["paramsOrder"]
                funcCallOrder = functionsDirectory[functionName]["paramsOrder"]
                if funcParamOrder == funcCallOrder:
                    print("Orden correcto de tipos")
                else:
                    exception.throwError("Se esperaba parámetros %s. Se recibió %s." % (str(funcParamOrder), str(funcCallOrder)))
            else:
                exception.throwError("Número de parámetros incorrecto (%s) para la función '%s'. Se esperaban %s." % (str(funcCallParams), str(functionName), str(funcParams)))
        else:
            exception.throwError("Ocurrió un problema llamando la función '%s'" % (functionName))
    else:
        exception.throwError("Función '%s' no existe" % (functionName))

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