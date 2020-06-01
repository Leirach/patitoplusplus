import semanticTable as semantics
import functionDirectory as fm
import exceptions

class CodeGenerator:
    def __init__(self, filename="patito"):
        self.filename = filename
        self.code = ["GOSUB principal 0 0\n"]
        self.line = 2
        # expresions
        self.opStack = []
        self.idStack = []
        self.tpStack = []
        self.memStack = []
        self.dimStack = []
        self.arrStack = []
        # functions and variables
        self.funcDir = fm.FunctionManager()
        self.gotoStack = []
        self.pendingLines = []
        self.paramCounter = 0
        self.forIds = []
        self.temp = 1

    def saveObj(self):
        self.f = open(self.filename+".obj", "w")
        mem = self.funcDir.createConstTable()
        for line in self.code:
            self.f.write(line)
        self.f.write("\n")
        for line in mem:
            self.f.write(line)
        self.f.close()

    # -- Utilities --
    def writeQuad(self, tok1, tok2, tok3, tok4):
        buf = "%s %s %s %s\n" % (tok1, tok2, tok3, tok4)
        self.code.append(buf)
        self.line += 1

    def popVar(self):
        var = self.idStack.pop()
        tipo = self.tpStack.pop()
        mem = self.memStack.pop()
        return var, tipo, mem

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]    # this will get the last element of stack
        else:
            return None

    # -- BUILD EXPRESSIONS AND ASSIGMENT --
    def buildExp(self):
        op = self.opStack.pop()
        # pop ids from stack
        der, derType, derMemScope = self.popVar()
        izq, izqType, izqMemScope = self.popVar()
        # get next temp var
        aux = "t"+str(self.temp)
        auxType = semantics.match(op, izqType, derType)
        if auxType is None:
            exceptions.fatalError("Invalid operand %s for types %s and %s" % (op, izqType, derType))
        izqAddr = self.funcDir.getAddress(izq, izqType, izqMemScope)
        derAddr = self.funcDir.getAddress(der, derType, derMemScope)
        auxAddr = self.funcDir.getAddress(aux, auxType, 'temp')
        self.writeQuad(op, izqAddr, derAddr, auxAddr)
        self.idStack.append(aux)
        self.tpStack.append(auxType)
        self.memStack.append('temp')
        self.temp += 1

    # TODO incompleto
    def buildUnaryExp(self):
        op = self.opStack.pop()
        if op == '-': # no estoy seguro si esto funciona
            self.opStack.append('*')
            self.idStack.append('-1')
            self.tpStack.append('int')
            self.memStack.append('const')
            self.buildExp()
        # falta para '$', '^', '!'

    def buildAssign(self):
        op = '='
        val, valType, valMem = self.popVar()
        var, varType, varMem = self.popVar()
        matches = semantics.match(op, varType, valType)
        if matches is None:
            exceptions.fatalError("No se puede asignar tipo %s a variable de tipo %s" % (valType, varType))
        valAddr = self.funcDir.getAddress(val, valType, valMem)
        varAddr = self.funcDir.getAddress(var, varType, varMem)
        self.writeQuad('=', valAddr, '0', varAddr)

    # -- IF ELSE / SI ENTONCES SINO--
    def ifStart(self):
        cond, condType, condMemScope = self.popVar()
        if condType not in ['bool']:
            exceptions.fatalError("Se esperaba bool en condicional se leyó %s" % (condType))
        condAddr = self.funcDir.getAddress(cond, condType, condMemScope)
        buf = "GOTOF %s" %(condAddr)
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line)
        self.writeQuad('if', 'gotof', 'temp', '0') # temporal quadruple

    def ifElse(self):
        self.writeQuad('else', 'goto', 'temp', '0')
        self.ifEnd()
        buf = "GOTO"
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line-1)

    def ifEnd(self):
        target = self.line
        lineNo = self.gotoStack.pop()
        buf = "%s %d 0 0\n" % (self.pendingLines.pop(), target)
        self.code[lineNo-1] = buf

    # -- WHILE / MIENTRAS HAZ --
    def whileStart(self):
        self.gotoStack.append(self.line)

    def whileDo(self):
        cond, condType, condMemScope = self.popVar() # TODO Checar que sea bool (int tambien?)
        if condType not in ['bool']:
            exceptions.fatalError("Se esperaba bool en ciclo mientras, se recibió %s" % (condType))
        condAddr = self.funcDir.getAddress(cond, condType, condMemScope)
        buf = "GOTOF %s" % (condAddr)
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line)
        self.writeQuad('while', 'goto', 'temp', '0')

    def whileEnd(self):
        lineNo = self.gotoStack.pop()
        buf = "%s %d 0\n" % (self.pendingLines.pop(), self.line+1)
        self.code[lineNo-1] = buf
        retLine = self.gotoStack.pop()
        self.writeQuad('GOTO', retLine, '0', '0')

    # -- FOR / DESDE HASTA HACER --
    def forStart(self):
        val, valType, valMem = self.popVar()
        inc, incType, incMem = self.popVar()
        if  valType not in ['int', 'float']:
            exceptions.fatalError("Se esperaba variable int o float para iterar en 'desde', se recibió %s" %(valType))
        valAddr = self.funcDir.getAddress(val, valType, valMem)
        incAddr = self.funcDir.getAddress(inc, incType, incMem)
        self.writeQuad("=", valAddr, "0", incAddr)
        self.idStack.append(inc)
        self.tpStack.append(incType)
        self.memStack.append(incMem)
        self.forIds.append(incAddr)
        self.gotoStack.append(self.line)

    def forDo(self):
        self.opStack.append("<=")
        self.buildExp()
        cond, condType, condMemScope = self.popVar()
        condAddr = self.funcDir.getAddress(cond, condType, condMemScope)
        self.gotoStack.append(self.line)
        buf = "GOTOF %s" % (condAddr)
        self.pendingLines.append(buf)
        self.writeQuad('loop', 'gotof', 'temp', '0')

    def forEnd(self):
        incAddr = self.forIds.pop()
        # la maquina virtual puede hacer incrementos aunque en teoria se deberia 
        # usar un temporal para esta suma
        self.writeQuad('++', incAddr, '0', '0')
        pendingIdx = self.gotoStack.pop() - 1
        retLine = self.gotoStack.pop()
        self.writeQuad('GOTO', str(retLine), '0', '0')
        buf = "%s %d 0 0\n" % (self.pendingLines.pop(), self.line)
        self.code[pendingIdx] = buf


    # -- FUNCDIR Y VARIABLES --
    def registerVariable(self, var, varType, dim1=None, dim2=None):
        self.funcDir.registerVariable(var, varType, dim1, dim2)

    def getVarType(self, p):
        return self.funcDir.getVariable(p)['type']

    def registerFunc(self, functionName, functionType):
        self.funcDir.registerFunc(functionName, functionType, self.line)

    def registerFuncParams(self, paramId, paramType):
        self.funcDir.registerFuncParams(paramId, paramType)

    def endFunc(self):
        # calcular tamaño de todo, self.temp tiene el count
        self.temp = 1 # reset temp counter
        self.code.append("ENDFUNC 0 0 0\n")
        self.line += 1
        self.funcDir.endFunc()

    # -- LLAMADAS DE FUNCIONES --
    def funcCallStart(self, func_id):
        self.funcDir.callFunction(func_id)
        self.idStack.append(func_id)
        self.writeQuad('ERA', func_id, '0', '0')

    def funcCallParam(self):
        param, paramType, paramMemScope = self.popVar()
        calledFunc = self.peek(self.idStack)
        self.funcDir.validateParam(calledFunc, self.paramCounter, paramType)
        self.paramCounter += 1 # param counting starts at 0
        paramAddr = self.funcDir.getAddress(param, paramType, paramMemScope)
        aux = 'PAR'+str(self.paramCounter)
        self.writeQuad('PARAM', paramAddr, aux, '0')

    def funcCallEnd(self):
        func_id = self.idStack.pop()
        self.writeQuad('GOSUB', func_id, '0', '0')
        self.paramCounter = 0 # reset param counter

    def funcCallReturn(self, func_id):
        retVar = self.funcDir.getReturnVariable(func_id)
        temp = "t"+str(self.temp)
        self.temp += 1
        tempAddr = self.funcDir.getAddress(temp, retVar['type'], 'temp')
        self.writeQuad('=', retVar['address'], '0', tempAddr)
        self.idStack.append(temp)
        self.tpStack.append(retVar['type'])
        self.memStack.append('temp')

    # -- ARRAYS --
    def accessArray(self):
        idx, idxType, idxMem = self.popVar() # expresion que se leyo entre brackets [idx]
        if idxType != 'int':
            exceptions.fatalError("Se esperaba int para indexar arreglo, se recibió %s" % (idxType))
        idxAddr = self.funcDir.getAddress(idx, idxType, idxMem)
        arrId = self.peek(self.idStack) # variable presuntamente dimensionada
        arrVar = self.funcDir.getVariable(arrId)
        # verificacion de limites
        dim = self.dimStack.pop() + 1
        if dim == 1:
            dimKey = 'dim1'
            limit = arrVar[dimKey]
            if limit is None:
                exceptions.fatalError("Variable '%s' no es un arreglo dimensionado" % (arrId))
        else:
            dimKey = 'dim2'
            limit = arrVar[dimKey]
            if limit is None:
                exceptions.fatalError("Variable '%s' no es un arreglo de dos dimensiones" % (arrId))
        limitAddr = self.funcDir.getAddress(limit, 'int', 'const')
        zeroAddr = self.funcDir.getAddress(0, 'int', 'const')
        self.writeQuad('VER', idxAddr, zeroAddr, limitAddr) # checar si esta en rango
        if dim == 1 and arrVar['dim2'] is not None:
            dim2Addr = self.funcDir.getAddress(arrVar['dim2'], 'int', 'const')
            self.writeQuad('*', idxAddr, dim2Addr, idxAddr) # multiplicar offset de dim1 si hay 2 dimensiones
        # vuelve a meter al stack
        self.idStack.append(idx)
        self.tpStack.append(idxType)
        self.memStack.append(idxMem)
        self.dimStack.append(dim)

    # [idx1][idx2] son las ultimas 2 temps calculadas con accessArray, 
    # se deberian sumar y meter en la pila el resultado, el ultimo temporal es 
    # el offset total de la variable.
    # si solo hay una dimension popVar() ya es el offset total
    def offsetVariable(self):
        dims = self.dimStack.pop()
        if dims == 0: # no hacer nada si no es variable dimensionada
            return
        if dims == 2:   # sumar los ultimos 2 temps para el offset total
            self.opStack.append('+')
            self.buildExp()
        # sumar el offset a la direccion base
        offset, offType, offMem = self.popVar() # [exp] o [idx]+[idx2] = offset
        offsetAddr = self.funcDir.getAddress(offset, offType, offMem)
        arr, arrType, arrMem = self.popVar()
        baseAddr = self.funcDir.getAddress(arr, arrType, arrMem)
        # suma en un pointer temporal
        ptr = "pt"+str(self.temp)
        ptrAddr = self.funcDir.getAddress(ptr, 'ptr', 'temp')
        self.temp += 1
        self.writeQuad('+ADDR', baseAddr, offsetAddr, ptrAddr) # sumar y poner en pointer
        # append pointer, tipo de dato es el mismo que el arreglo (para semantica), no debe ser 'ptr'
        self.idStack.append(ptr)
        self.tpStack.append(arrType)
        self.memStack.append('temp')

    # -- RETORNA --
    def retorna(self):
        ret, retType, retMem = self.popVar()
        retAddr = self.funcDir.getAddress(ret, retType, retMem)
        gRetId = '&' + self.funcDir.scope
        globalRetVar = self.funcDir.getVariable(gRetId) # cambiar a get address
        if globalRetVar['type'] != retType:
            exceptions.fatalError("No se puede retornar '%s' en funcion '%s', se esparaba tipo '%s'" %(retType, self.funcDir.scope, globalRetVar['type']))
        self.writeQuad("=", retAddr, "0", globalRetVar['address'])

    # -- READ PRINT / QUACKIN QUACKOUT --
    def ioQuad(self, io):
        var, varType, varMemScope = self.popVar()
        varAddr = self.funcDir.getAddress(var, varType, varMemScope)
        self.writeQuad(io, varAddr, '0','0')

