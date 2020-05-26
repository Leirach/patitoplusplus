
# TODO doble llamada de función
# type tipo de retorno esperado de la funcion
# params: lista de tipos de parametros esperados para la llamada
# vars: guarda parametros y variables en un diccionario para indexar facilmente

import exceptions as exception
import memory as mem
class FunctionManager:
    def __init__(self):
        self.scope = 'global'
        self.lastType = ''
        self.functionsDir = {
            'global': {'type': 'void', 'params': [], 'vars': {} },
        }
        self.memory = mem.MemoryManager()

    #add function to Directory
    def registerFunc(self, functionName, functionType):
        if self.functionsDir.get(functionName) is not None:
            exception.fatalError("Función '%s' fue definida anteriormente." % (functionName))
        function = {
            functionName : {'type': functionType, 'params': [], 'vars': {} },
        }
        self.functionsDir.update(function)
        self.scope = functionName
        if functionType != 'void':
            # agrega una var global para retorno, prefix & para evitar conflictos
            returnVar = '&' + functionName
            address = self.memory.assignAddress('global', functionType)
            self.functionsDir['global']['vars'].update({
                returnVar: {'type':functionType, 'address':address, 'dim1':None, 'dim2':None}
            })
        return True

    #add function to Directory
    def registerFuncParams(self, paramId, paramType):
        self.registerVariable(paramId, paramType)
        self.functionsDir[self.scope]['params'].append(paramType)

    # TODO guardar tamaño de funcion
    def endFunc(self):
        self.memory.reset()

    #add function to Directory
    def registerVariable(self, varId, varType, dim1=None, dim2=None):
        if varType is None: # Si no se manda tipo usar el anterior
            varType = self.lastType
        else:               # Si se manda tipo guardarlo para siguientes vars
            self.lastType = varType
        if self.functionsDir[self.scope]['vars'].get(varId) is not None:
            exception.fatalError("Variable '%s' duplicada en función '%s'" % (varId, self.scope))
        if dim1 == 0 or dim2 == 0:
            exception.fatalError("Variable dimensionada %s no puede tener tamaño 0" % (varId))
        memoryScope = "local" if self.scope != "global" else "global"
        address = self.memory.assignAddress(memoryScope, varType, dim1, dim2)
        self.functionsDir[self.scope]['vars'].update({varId: {'type': varType, 'address': address, 'dim1': dim1, 'dim2':dim2} })
        return True

    def getVariable(self, varId):
        var = self.functionsDir[self.scope]['vars'].get(varId)
        if var is not None:
            return var
        var = self.functionsDir['global']['vars'].get(varId)
        if var is not None:
            return var
        exception.fatalError("Variable '%s' no ha sido declarada" % (varId))

    # func: functionName, paramNum: Number, type: Type sent
    # se asume que ya se valido que la funcion existe
    def validateParam(self, func, paramNum, paramType):
        length = len(self.functionsDir[func]['params'])
        if paramNum >= length:
            exception.fatalError("Número de parámetros incorrecto para la función '%s'. Se esperaban %s." % ( func, length) )
        expected = self.functionsDir[func]['params'][paramNum] # deberia regresar tipo de la variable local
        if expected != paramType:
            exception.fatalError("Se esperaba parámetro de tipo %s. Se recibió %s." % (expected, paramType))
        return True

    def callFunction(self, functionName):
        if self.functionsDir.get(functionName) is None:
            exception.fatalError("Función '%s' no existe" % (functionName))
        return True

    # regresa direccion de variable
    # si no es variable regresa direccion con el modulo de memoria
    def getAddress(self, value, tipo, scope):
        if scope == 'var': # para local y global
            return self.getVariable(value)['address']
        else: # para const y temp
            return self.memory.getAddress(value, tipo, scope)

    def createConstTable(self):
        return self.memory.createConstTable()