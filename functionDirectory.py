
# TODO doble llamada de función
# type tipo de retorno esperado de la funcion
# params: lista de los id de parametros esperados para la llamada
#         la idea es que se indexe vars con estos strings para checar a que variable
#         pertenece cual parametro. sentiende claro diafano cristalino?
# vars: guarda parametros y variables en un diccionario para indexar facilmente

import exceptions as exception
import memory as mem
class FunctionManager:
    def __init__(self):
        self.scope = 'global'
        self.functionsDir = {
            'global': {'type': 'void', 'params': [], 'vars': {} },
        }
        self.memory = mem.MemoryManager()

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

    # TODO guardar tamaño de funcion
    def endFunc(self):
        self.memory.reset()

    #add function to Directory
    def registerVariable(self, varId, varType):
        #TODO creo que esto no es necesario
        if self.functionsDir.get(self.scope) is None: #Si la función no existe
            exception.throwError("Función '%s' no existe" % (self.scope))

        if self.functionsDir[self.scope]['vars'].get(varId) is None:
            memoryScope = "local" if self.scope != "global" else "global"
            address = self.memory.assignAddress(memoryScope, varType)
            self.functionsDir[self.scope]['vars'].update({varId: {'type': varType, 'address': address} })
            return True 
        exception.throwError("Variable '%s' duplicada en función '%s'" % (varId, self.scope))


    def getVariableType(self, functionName, varId):
        #si le mandas None en functionName se asume que es el scope
        if functionName is None:
            functionName = self.scope
        var = self.functionsDir[functionName]['vars'].get(varId)
        if var is not None:
            return var['type']
        # Si no estaba en el scope local intenta en global o ya de plano no existe
        var = self.functionsDir['global']['vars'].get(varId)
        if var is not None: 
            return var['type']
        exception.throwError("Variable '%s' no ha sido declarada" % (varId))

    # se supone que ya se valido que existe la variable
    def getVariableAddress(self, varId):
        var = self.functionsDir[self.scope]['vars'].get(varId)
        if var is not None:
            return var['address']
        var = self.functionsDir['global']['vars'].get(varId)
        if var is not None: 
            return var['address']
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

    # regresa direccion de variable
    # si no es variable regresa direccion con el modulo de memoria
    def getAddress(self, value, scope, tipo):
        if scope == 'var':
            return self.getVariableAddress(value)
        if scope == 'temp':
            return self.memory.getTemporal(value, tipo)
        if scope == 'const':
            return self.memory.getConstant(value, tipo)

    def createConstTable(self):
        return self.memory.createConstTable()