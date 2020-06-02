
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
    def registerFunc(self, functionName, functionType, line):
        if self.functionsDir.get(functionName) is not None:
            exception.fatalError("Función '%s' fue definida anteriormente." % (functionName))
        function = {
            functionName : {'type': functionType, 'params': [], 'vars': {}, 'goto': line, 'paramAddr': [] },
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
        addr = self.registerVariable(paramId, paramType)
        self.functionsDir[self.scope]['params'].append(paramType)
        self.functionsDir[self.scope]['paramAddr'].append(addr)

    def endFunc(self):
        counters = self.memory.reset() # regresa tamaños local y temp de self.memory
        localMem = []
        tempMem = []
        for key in mem.TYPES:
            localMem.append(str(counters['local'][key]))
            tempMem.append(str(counters['temp'][key]))
        localMem = " ".join(localMem)
        tempMem = " ".join(tempMem)
        self.functionsDir[self.scope].update({'local': localMem, 'temp': tempMem})

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
        return address

    def getVariable(self, varId):
        var = self.functionsDir[self.scope]['vars'].get(varId)
        if var is not None:
            return var
        var = self.functionsDir['global']['vars'].get(varId)
        if var is not None:
            return var
        exception.fatalError("Variable '%s' no ha sido declarada en '%s'." % (varId, self.scope))

    def getReturnVariable(self, func_id):
        func = self.functionsDir[func_id]
        if func['type'] == 'void':
            exception.fatalError("Función '%s' no tiene un tipo de retorno válido en expresión." % (func_id))
        return self.getVariable('&' + func_id)

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

    # orre al terminar la compilacion
    # contiene primero el directorio de funciones
    # "func_id goto\n" - id y goto
    # "local <int> <float> <bool> <char>" - tamaño de memoria local
    # "temp <int> <float> <bool> <char>" - tamaño de memoria temporal
    # memObj tiene el tamaño de global y const
    # y despues la lista de memoria constante en formato "address value"
    def createConstTable(self):
        func = []
        for key in self.functionsDir:
            if key != 'global': # no hay nada que imprimir para global el tamaño esta en memObj
                parCount = len(self.functionsDir[key]['paramAddr'])
                buf = "%s %d %d\n" % (key, self.functionsDir[key]['goto'], parCount)
                func.append(buf)
                for i in range(0, parCount):
                    buf = "PAR%d %d\n" % (i+1, self.functionsDir[key]['paramAddr'][i])
                    func.append(buf)
                func.append('local ' + self.functionsDir[key]['local'] + '\n')
                func.append('temp ' + self.functionsDir[key]['temp'] + '\n')
        func.append('\n') # separar dir func de memoria global/const
        memObj = self.memory.createConstTable()
        return func + memObj
