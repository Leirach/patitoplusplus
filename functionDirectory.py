
#TODO doble llamada de función
import exceptions as exception

# type: tipo de retorno esperado de la funcion
# params: lista de los id de parametros esperados para la llamada
#         la idea es que se indexe vars con estos strings para checar a que variable
#         pertenece cual parametro. sentiende claro diafano cristalino?
# vars: guarda parametros y variables en un diccionario para indexar facilmente
class FunctionManager:
    def __init__(self):
        self.scope = 'global'
        self.functionsDir = {   
            'global': {'type': 'void', 'params': [], 'vars': {} },
        }

    #add function to Directory
    def registerFunc(self, functionName, functionType):
        if self.functionsDir.get(functionName) is not None:
            exception.throwError("Función '%s' fue definida anteriormente." % (functionName))
        function = {
            functionName : {'type': functionType, 'params': [], 'vars': {} },
        }
        self.functionsDir.update(function)
        self.scope = functionName
        return True

    #add function to Directory
    def registerFuncParams(self, paramId, paramType):
        self.registerVariable(paramId, paramType)
        self.functionsDir[self.scope]['params'].append(paramId)

    #add function to Directory
    def registerVariable(self, varId, varType):
        #TODO creo que esto no es necesario
        if self.functionsDir.get(self.scope) is None: #Si la función no existe
            exception.throwError("Función '%s' no existe" % (self.scope))

        if self.functionsDir[self.scope]['vars'].get(varId) is None:
            self.functionsDir[self.scope]['vars'].update({varId: varType})
            return True 
        exception.throwError("Variable '%s' duplicada en función '%s'" % (varId, functionName))


    def getVariableType(self, functionName, varId):
        #si le mandas None en functionName se asume que es el scope
        if functionName is None:
            functionName = self.scope
        varType = self.functionsDir[functionName]['vars'].get(varId)
        if varType is not None:
            return varType
        # Si no estaba en el scope local intenta en global o ya de plano no existe
        varType = self.functionsDir['global']['vars'].get(varId)
        if varType is not None:
            return varType
        exception.throwError("Variable '%s' no ha sido declarada" % (varId))

    # func: functionName, paramNum: Number, type: Type sent
    # se asume que ya se valido que la funcion existe
    def validateParam(self, func, paramNum, paramType):
        length = len(self.functionsDir[func]['params'])
        if paramNum >= length:
            exception.throwError("Número de parámetros incorrecto para la función '%s'. Se esperaban %s." % ( func, length) )
        var = self.functionsDir[func]['params'][paramNum]
        expected = self.getVariableType(func, var) # deberia regresar tipo de la variable local
        if expected != paramType:
            exception.throwError("Se esperaba parámetro de tipo %s. Se recibió %s." % (expected, paramType))
        return True

    def callFunction(self, functionName):
        if self.functionsDir.get(functionName) is None:
            exception.throwError("Función '%s' no existe" % (functionName))
        return True

# deje esto pero creo que ya no es necesario
# pero se veia muy complicado y me da cosa borrarlo
def validateFunctionSemantics(functionName):
    if functionsDir.get(functionName): #Si la función existe
        print("Función existe")
        if functionName+"patitoFuncCall" in functionsDir:
            print("Llamada generada")
            funcParams = functionsDir[functionName]["numParams"]
            funcCallParams = functionsDir[functionName+"patitoFuncCall"]["numParams"]
            if funcParams == funcCallParams:
                print("Número de parámetros correcto")
                funcCallOrder = functionsDir[functionName+"patitoFuncCall"]["paramsOrder"]
                funcParamOrder = functionsDir[functionName]["paramsOrder"]
                if funcParamOrder == funcCallOrder:
                    print("Orden correcto de tipos")
                    print(functionsDir)
                    del functionsDir[functionName+"patitoFuncCall"]
                    print("REMOVED")
                    print(functionsDir)
                else:
                    exception.throwError("Se esperaba parámetros %s. Se recibió %s." % (str(funcParamOrder), str(funcCallOrder)))
            else:
                exception.throwError("Número de parámetros incorrecto (%s) para la función '%s'. Se esperaban %s." % (str(funcCallParams), str(functionName), str(funcParams)))
        else:
            exception.throwError("Ocurrió un problema llamando la función '%s'" % (functionName))
    else:
        exception.throwError("Función '%s' no existe" % (functionName))

# para probar errores
'''
functionName = 'main'
functionType = 'void'
param = 'x'
paramType = 'int'
print("........Empty dictionary.......")    
print(functionsDir)
print("........Adding Function to dictionary.......")  
registerFunc(functionName, functionType)
print("........Function added.......")  
print(functionsDir)
print("........Adding param to function .......")  
registerFuncParams(functionName, param, paramType)
print("........Added param to function .......")  
print(functionsDir)
callFunction(functionName) # checa que existe
validateParam(functionName, 0, 'int') # llamando x siendo entero: main(x)
validateParam(functionName, 1, 'int') # llamando x siendo entero: main(x, x)

print("........Adding param to function .......")  
registerFuncParams(functionName, 'Y', paramType)
print("........Added param to function .......")  
print(functionsDir)
print("........Adding param to function .......")  
registerFuncParams(functionName, 'Y', paramType)
print("........Adding var to function .......")  
registerVariable(functionName, 'aux', 'bool')
print("........Added var to function .......")  
print("........Adding var to function .......")  
registerVariable(functionName, 'aux', 'bool')
print(functionsDir)
print("........Adding var to function .......")  
registerVariable(functionName, 'pop', 'float')
print("........Added var to function .......")  
print(functionsDir)
print("........Adding function .......")  
registerFunc(functionName, functionType)
print(functionsDir)
print("........Adding function .......")  
registerFunc('popRockCallejero', functionType)
print("........Added function .......")  
print(functionsDir)
'''