# Follow these blog posts. Build AST and plug in the ARITH language.

# https://ruslanspivak.com/lsbasi-part7/
# https://rosettacode.org/wiki/Arithmetic_evaluation#Python
import operator


class AstNode(object):
    def __init__(self, opr, left, right):
        self.opr = opr
        self.l = left
        self.r = right

    def eval(self, store):
        # print("self.opr",self.opr)
        return self.opr(IntAexp(self.l.eval(store)), IntAexp(self.r.eval(store))).eval(store)


class CstNode(object):
    def __init__(self, opr, left, right, type):
        self.opr = opr
        self.l = left
        self.r = right
        self.type = type

    def eval(self, store):
        # return self.opr('x', IntAexp(self.r.eval(store))).eval(store)
        # print('self.l = left', self.l )
        # print('self.type', self.type)
        if self.type == 'assign':
            return self.opr(self.l, IntAexp(self.r.eval(store))).eval(store)
        return


class Aexp(object):
    def __init__(self):
        self.e = None

    def eval(self, store):
        return


class IntAexp(Aexp):
    def __init__(self, n):
        self.e = int(n)
        # print("n",n)

    def eval(self, store):
        return self.e


class VarAexp(Aexp):
    def __init__(self, n):
        self.str = n

    def eval(self, store):
        # print("self.str",self.str)
        # print("store",store)
        self.str = self.str.replace(" ", "")
        # print("self.str after",self.str)
        return store[self.str]


class SumAexp(Aexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        return self.e1.eval(store) + self.e2.eval(store)


class MultAexp(Aexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
      #   print('in mult e1',self.e1.eval(store), 'e2', self.e2.eval(store))
        return self.e1.eval(store) * self.e2.eval(store)


class MinusAexp(Aexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        return self.e1.eval(store) - self.e2.eval(store)


class PowAexp(Aexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        return pow(self.e1.eval(store), self.e2.eval(store))


# New
class Bexp(object):
    def __init__(self):
        self.b = None

    def eval(self, store):
        return


class TrueBexp(Bexp):
    def __init__(self, b1, b2):
        self.b = None

    def eval(self, store):
        return True


class FalseBexp(Bexp):
    def __init__(self, b1, b2):
        self.b = None

    def eval(self, store):
        return False


class AndBexp(Bexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        # print('AndBexp', self.e1.eval(store) and self.e2.eval(store))
      #   print('AndBexp', self.e1.eval(store) , self.e2.eval(store))
        return (self.e1.eval(store) and self.e2.eval(store))


class OrBexp(Bexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        # print('AndBexp', self.e1.eval(store) and self.e2.eval(store))
      #   print('OrBexp', self.e1.eval(store) , self.e2.eval(store))
        return (self.e1.eval(store) or self.e2.eval(store))


class GreaterBexp(Bexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        return self.e1.eval(store) > self.e2.eval(store)


class LessBexp(Bexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        return self.e1.eval(store) < self.e2.eval(store)


class EqualBexp(Bexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
      #   print('e1',self.e1.eval(store), 'e2', self.e2.eval(store))
        return self.e1.eval(store) == self.e2.eval(store)


class GreaterEqualBexp(Bexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        return self.e1.eval(store) >= self.e2.eval(store)


class LessEqualBexp(Bexp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
        return self.e1.eval(store) <= self.e2.eval(store)


class NotBexp(Bexp):
    def __init__(self, e1,e2):
      #   print('e1', e1, 'e2',e2)
        self.e1 = e1
        self.e2 = e2

    def eval(self, store):
      #   print('eval e1 ', self.e1.eval(store))
      #   print('eval e2 ', self.e2.eval(store))
      #   print('eval e2 ', not self.e2.eval(store))
        return (not self.e2.eval(store))


class Comm(object):
    def __init__(self):
        self.C = None

    def eval(self, store):
        return


class SkipComm(Comm):
    def __init__(self):
        self.C = None

    def eval(self, store):
      #   print('in skip eval', store)
        return store


class Assign(Comm):
    def __init__(self, X, val):
        self.X = X
        self.val = val

    def eval(self, store):
        # print("tst: before", store)
        store[self.X] = self.val.eval(store)
        # print("tst:after ", store)
        # print("self.val.eval(store)",self.val.eval(store))
        return store


class If(Comm):
    def __init__(self, b, c1, c2):
        self.b = b
        self.c1 = c1
        self.c2 = c2

    def eval(self, s):
        if b.eval(s):
            return c1.eval(s)
        else:
            return c2.eval(s)

class fen(Comm):
   def __init__(self, c1, c2):
      self.c1 = c1
      self.c2 = c2
   def eval(self, s):
      s1 = self.c1.eval(s)
      return self.c2.eval(s1)   


class Yaccer(object):
    def __init__(self):
        self.operstak = []
        self.nodestak = []
        self.__dict__.update(self.state1)

    def v1(self, valStrg, char_flag):
        # Value String
        # print("valStrg",valStrg)
        if char_flag == 1:
            if valStrg in store:
                #    print("blah")
                self.nodestak.append(VarAexp(valStrg))
                self.__dict__.update(self.state2)
            else:
                self.nodestak.append(IntAexp(0))
                self.__dict__.update(self.state2)

        else:
            self.nodestak.append(IntAexp(valStrg))
        self.__dict__.update(self.state2)
        # print 'push', valStrg

    def o2(self, operchar):
        # Operator character or open paren in state1
        def openParen(a, b):
            return 0		# function should not be called

        opDict = {'+': (SumAexp, 2, 2),
                  '-': (MinusAexp, 2, 2),
                  '*': (MultAexp, 3, 3),
                  '^': (PowAexp, 4, 4),
                  '(': (openParen, 0, 8),
                  }
      #   print("opDict[operchar][2]",opDict[[operchar]])
        operPrecidence = opDict[operchar][2]
        # print("opDict[operchar]",opDict[operchar])
        self.redeuce(operPrecidence)

        self.operstak.append(opDict[operchar])
        self.__dict__.update(self.state1)
        # print 'pushop', operchar

    def syntaxErr(self, char):
        # Open Parenthesis
        print('parse error - near operator "%s"' % char)

    def pc2( self,operchar ):
      # Close Parenthesis
      # reduce node until matching open paren found 
      self.redeuce( 1 )
      if len(self.operstak)>0:
         self.operstak.pop()		# pop off open parenthesis
      else:
         print ('Error - no open parenthesis matches close parens.')
      self.__dict__.update(self.state2)

    def end(self):
        self.redeuce(0)
        return self.nodestak.pop()

    def redeuce(self, precidence):
        # print("precidence",precidence,"self.operstak",self.operstak)
        while len(self.operstak) > 0:
            tailOper = self.operstak[-1]
            if tailOper[1] < precidence:
                break

            tailOper = self.operstak.pop()
            vrgt = self.nodestak.pop()
            vlft = self.nodestak.pop()
            self.nodestak.append(AstNode(tailOper[0], vlft, vrgt))
            # print 'reduce'

    state1 = {'v': v1, 'o': syntaxErr, 'po': o2, 'pc': syntaxErr}
    state2 = {'v': syntaxErr, 'o': o2, 'po': syntaxErr, 'pc': pc2}


def Lex(exprssn, p, store):
    bgn = None
    cp = -1
    char_flag = 0
   #  print('in Lex', exprssn)
    for c in exprssn:
        cp += 1
        if c in '+*^()':         # throw in exponentiation (^)for grins
            #  print("+-*cp, bgn", cp, bgn)
            if bgn is not None:
                #print("cp, bgn", cp, bgn, exprssn[bgn:cp])
                p.v(p, exprssn[bgn:cp], char_flag)
                bgn = None
            if c == '(':
                p.po(p,c) 
            elif c == ')':
                p.pc(p,c)
            else:   
                p.o(p, c)
        elif c in ' \t':
            if bgn is not None:
                p.v(p, exprssn[bgn:cp], char_flag)
                bgn = None
                char_flag = 0
        elif c in '0123456789':
            if bgn is None:
                bgn = cp
        elif c in '-':
            #  print("cp, bgn", cp, bgn, exprssn[bgn:cp])
            #  print("length", exprssn[cp+1:cp+2])#==' ')
            if exprssn[cp+1:cp+2] == ' ':
                if bgn is not None:
                    p.v(p, exprssn[bgn:cp], char_flag)
                    bgn = None
                p.o(p, c)
            else:
                if bgn is None:
                    bgn = cp
        elif c == ':':
            if bgn is not None:
                print(exprssn[bgn:cp])
                p.v(p, exprssn[bgn:cp], char_flag)
                bgn = None
            p.o(p, c)

        else:
            char_flag = 1
            if bgn is None:
                bgn = cp
            #  if exprssn[cp+2] == ':':
                # char_flag = 1
                # if bgn is None:
                #    bgn = cp
            #  else:
            #     print ('Invalid character in expression')
            #     if bgn is not None:
            #        p.v(p, exprssn[bgn:cp],char_flag)
            #        bgn = None

    if bgn is not None:
        p.v(p, exprssn[bgn:cp+1], char_flag)
        bgn = None
    return p.end()


class YaccerBool(object):
    def __init__(self):
        self.operstak = []
        self.nodestak = []
        self.__dict__.update(self.state1)

    def v1(self, valStrg, char_flag, store):
        # Value String
      #   print("valStrg",valStrg)
        number_val = Lex(valStrg,Yaccer(),store).eval(store)
      #   print("number_val",number_val)
        if char_flag == 1:
            # print("in bool v1", store)
            if valStrg in store:
                #    print("blah")
                self.nodestak.append(IntAexp(number_val))
                self.__dict__.update(self.state2)
                return store

            else:
                #   command = valStrg + " : 0"
                #   temp = LexComm(command,Yaccer_Comm(),store, 0)
                #   temp.eval(store)
                self.nodestak.append(IntAexp(number_val))
                self.__dict__.update(self.state2)
            #    print(command, 'flag',char_flag)
            #    print(temp)
            #    print(temp.eval(store))
                return store

        self.nodestak.append(IntAexp(number_val))
        self.__dict__.update(self.state2)
        return store
        # print 'push', valStrg

    def o2(self, operchar):
        # Operator character or open paren in state1
        def openParen(a, b):
            return 0		# function should not be called
        opDict = {'=': (EqualBexp, 2, 2),
                  '>': (GreaterBexp, 2, 2),
                  '<': (LessBexp, 2, 2),
                  'True': (TrueBexp, 5, 5),
                  'False': (FalseBexp, 5, 5),
                  '∧': (AndBexp, 1, 1),
                  '∨': (OrBexp, 1, 1),
                  '¬':(NotBexp, 4, 4),
                  '(': (openParen, 0, 8 ),

                  }
        operPrecidence = opDict[operchar][2]
        # print("opDict[operchar]",opDict[operchar])
        self.redeuce(operPrecidence)

        self.operstak.append(opDict[operchar])
        self.__dict__.update(self.state1)
        # print 'pushop', operchar

    def syntaxErr(self, char):
        # Open Parenthesis
        return
        # print ('parse error - near operator "%s"' %char)
        
    def pc2( self,operchar ):
      # Close Parenthesis
      # reduce node until matching open paren found 
      self.redeuce( 1 )
      if len(self.operstak)>0:
         self.operstak.pop()		# pop off open parenthesis
      else:
         print ('Error - no open parenthesis matches close parens.')
      self.__dict__.update(self.state2)

    def end(self):
        self.redeuce(0)
        return self.nodestak.pop()

    def redeuce(self, precidence):
        # print("precidence",precidence,"self.operstak",self.operstak)
        while len(self.operstak) > 0:
            tailOper = self.operstak[-1]
            if tailOper[1] < precidence:
                break

            tailOper = self.operstak.pop()
            vrgt = self.nodestak.pop()
            vlft = self.nodestak.pop()
            self.nodestak.append(AstNode(tailOper[0], vlft, vrgt))
            # print 'reduce'

    state1 = {'v': v1, 'o': o2, 'po': o2, 'pc': pc2}
    state2 = {'v': v1, 'o': o2, 'po': o2, 'pc': pc2}


def LexBool(exprssn, p, store):
    bgn = None
    cp = -1
    flag_double = 0
    char_flag = 0
   #  print("exprssn",exprssn)
    exprssn = exprssn.replace("true","@")
    exprssn = exprssn.replace("false","#")
   #  print("exprssn after",exprssn, 'store', store)
    for c in exprssn:
        cp += 1
        if c in '=∧∨()':         # throw in exponentiation (^)for grins
            # print("=∧∨¬ cp, bgn", cp, bgn)
            if bgn is not None:
                #print("cp, bgn", cp, bgn, exprssn[bgn:cp])
                temp = p.v(p, exprssn[bgn:cp], char_flag, store)
                # print('store',store.eval(store))
                bgn = None
            #  print('bgn',bgn)
            if c == '(': 
                p.po(p,c)
            elif c == ')': 
                p.pc(p,c)
            else:
                char_flag = 0
                p.o(p, c)
        elif c in '¬' :
            # print("¬ cp, bgn", cp, bgn)
            # if bgn is not None:
            #     #print("cp, bgn", cp, bgn, exprssn[bgn:cp])
            #     temp = p.v(p, exprssn[bgn:cp], char_flag, store)
            #     # print('store',store.eval(store))
            #     bgn = None
            # #  print('bgn',bgn)
            # char_flag = 0
            p.v(p,'1',char_flag,store)
            p.o(p, c)   
        elif c in '<>':
            #  print('bgn',bgn)
            if bgn is not None:
                #print("cp, bgn", cp, bgn, exprssn[bgn:cp])
                # print('char_flag',char_flag)
                temp = p.v(p, exprssn[bgn:cp], char_flag, store)
                # print('store',temp.eval(store))
                bgn = None
            #  print('bgn',bgn)
            char_flag = 0
            p.o(p, c)

        elif c in ' \t':
            a = 1
            # if bgn is not None:
            #     temp = p.v(p, exprssn[bgn:cp], char_flag, store)
            #     # checkBool = LexBool('x < 1',YaccerBool(), store)
            #     # print ('checkBool',checkBool)
            #     # print('cp',cp)
            #     # print('store',temp.eval(store))
            #     # print(store)
            #     bgn = None
        elif c in '0123456789':
            #  print(store)
            if bgn is None:
                bgn = cp
        elif c in '-':
            #  print("cp, bgn", cp, bgn, exprssn[bgn:cp])
            #  print("length", exprssn[cp+1:cp+2])#==' ')
            if exprssn[cp+1:cp+2] != ' ':
                if bgn is None:
                    bgn = cp
        elif c in "@":
            # print("in true")
                #print("cp, bgn", cp, bgn, exprssn[bgn:cp])
            p.v(p, '1', char_flag, store)
            # p.o(p, 'True')
            # p.v(p, '1', char_flag, store)
            bgn = None
        elif c in "#":
           
            p.v(p, '0', char_flag, store)
            bgn = None
            # p.o(p, 'False')
            # p.v(p, '1', char_flag, store)

        else:
            char_flag = 1
            # print('in else')
            if bgn is None:
                bgn = cp

    if bgn is not None:
      #   print('pv bng', bgn)
        temp = p.v(p, exprssn[bgn:cp+1], char_flag, store)
      #   print('end', temp.eval(store))
        bgn = None

   #  print('end of Lex bool', store)

    return p.end(), store


class Yaccer_Comm(object):
    def __init__(self):
        self.operstak = []
        self.nodestak = []
        self.__dict__.update(self.state1)

    def v1(self, valStrg, char_flag):
        # Value String
        # print("valStrg",valStrg)
        if char_flag == 1:
            self.nodestak.append(VarAexp(valStrg))
        else:
            self.nodestak.append(IntAexp(valStrg))
        self.__dict__.update(self.state2)
        # print 'push', valStrg

    def v1_assign(self, valStrg, char_flag):
        # Value String
        # print("valStrg",valStrg)
        if char_flag == 1:
            self.nodestak.append(valStrg.replace(" ", ""))
        else:
            self.nodestak.append(IntAexp(valStrg))
        self.__dict__.update(self.state2)
        # print 'push', valStrg

    def v1_if(self, command):
        nodestak.append(Comm(command))
        self.__dict__.update(self.state2)

    def o2(self, operchar):
        # Operator character or open paren in state1
        def openParen(a, b):
            return 0		# function should not be called

        opDict = {
            ':': (Assign, 2, 2, 'assign'),
            '@': (If, 4, 4, 'If'),
            '!': (SkipComm, 2, 2, 'skip'),
            '{': (openParen, 0, 8, 'openParen'),
            ';': (fen, 5, 5, 'fen'),
        }
        operPrecidence = opDict[operchar][2]
        # print("opDict[operchar]",opDict[operchar])
        self.redeuce(operPrecidence)

        self.operstak.append(opDict[operchar])
        # print("self.operstak",self.operstak)
        self.__dict__.update(self.state1)
        # print 'pushop', operchar

    def syntaxErr(self, char):
        # Open Parenthesis
        print('parse error - near operator "%s"' % char)

    def pc2( self,operchar ):
      # Close Parenthesis
      # reduce node until matching open paren found 
      self.redeuce( 1 )
      if len(self.operstak)>0:
         self.operstak.pop()		# pop off open parenthesis
      else:
         print ('Error - no open parenthesis matches close parens.')
      self.__dict__.update(self.state2)

    def end(self):
        self.redeuce(0)
        return self.nodestak.pop()

    def redeuce(self, precidence):
        # print("precidence",precidence,"self.operstak",self.operstak)
        while len(self.operstak) > 0:
            tailOper = self.operstak[-1]
            if tailOper[1] < precidence:
                break
            # print('self.operstak',self.operstak)   
            tailOper = self.operstak.pop()
            vrgt = self.nodestak.pop()
            vlft = self.nodestak.pop()
            #  print("tailOper[0]",tailOper[0])
            self.nodestak.append(CstNode(tailOper[0], vlft, vrgt, tailOper[3]))
            # print 'reduce'

    state1 = {'v': v1, 'o': syntaxErr, 'po': o2, 'v1_assign': v1_assign, 'pc': pc2}
    state2 = {'v': syntaxErr, 'o': o2, 'po': syntaxErr, 'v1_assign': v1_assign, 'pc': pc2}


def LexComm(exprssn, p, store, flag_care):
    bgn = None
    cp = -1
    flag_if = -1
    flag_then = -1
    flag_else = -1
    flag_while = -1
    flag_do = -1
    flag_assign = -1
    flag_while_do = -1 #-1 for no, 1 for while, 2 for if
    flag_else_if = -1
    flag_then2 = -1 #second then in elif
   #  print("in Lexcomm", exprssn)
    for c in exprssn:
        cp += 1
        if c in ':':
            if bgn is not None:
                # print(exprssn[cp+1:len(exprssn)])
                flag_assign = cp
                p.v1_assign(p, exprssn[bgn:cp], char_flag)
                bgn = None
            p.o(p, c)
            # print(exprssn[cp])
           
        elif c == '{':
            if bgn is not None:
               p.v(p, exprssn[bgn:cp],char_flag)
               bgn = None
            p.po(p, c)
        elif c == '}':
            if bgn is not None:
               p.v(p, exprssn[bgn:cp],char_flag)
               bgn = None
            p.pc(p,c)
        elif c == '@':  # if
            #   print('in if')
            if flag_else_if != -1: continue
            if flag_while_do == -1: flag_while_do = 2
            if flag_if == -1: flag_if = cp
        elif c == '#':  # then
            if flag_then != -1:
               flag_then2 = cp
            else:
               if flag_then == -1: flag_then = cp
        elif c == '$':  # else
            # print ('in esle',exprssn[cp+2])
            if exprssn[cp+2] == '@':
               flag_else_if = cp + 2
               bgn = cp + 2
               # if_command1 = exprssn[flag_then+2:cp]  
            else:      
               if_command3 = exprssn[flag_then2+2:cp]
               flag_else = cp
               bgn = cp
        elif c == '%':  # while
            # print('in while')
            if flag_while_do == -1: flag_while_do = 1
            if flag_while == -1: flag_while = cp
            
        elif c == '&':  # do
            if flag_do == -1: flag_do = cp
        elif exprssn.replace(" ","") == '!': #c == '!':# 
            # print('in skip', store)
            return SkipComm(), store

        elif cp == len(exprssn)-1:
            # print('in lasst',flag_do, " else ",flag_else)
            # print("flag_while_do",flag_while_do)
            if flag_else != -1 and flag_while_do != 1:
                #  print("in Lexcomm2", store)
                condition = exprssn[flag_if+2:flag_then]
                condition2 = exprssn[flag_else_if+2:flag_then2]
                if flag_else_if != -1:
                  if_command1 = exprssn[flag_then+2:flag_else_if-2] 
                else:
                   if_command1 = exprssn[flag_then+2:flag_else] 
                if_command2 = exprssn[flag_else+2:cp+1]
               #  print('condition',condition,'if_command1',if_command1)
               #  print('condition2', condition2,'if_command3',if_command3)
               #  print('if_command2',if_command2)

                if flag_else_if != -1:
                  #  print('in elif')
                   temp_condition, store = LexBool(condition, YaccerBool(), store)
                   temp_condition2, store = LexBool(condition2, YaccerBool(), store)
                   if temp_condition.eval(store):
                      temp, store = LexComm(if_command1, Yaccer_Comm(), store, 1)
                      return temp,store  
                   elif temp_condition2.eval(store):
                     #  print('in condition 2')
                      temp, store = LexComm(if_command3, Yaccer_Comm(), store, 1)
                      return temp,store  
                   else:
                      temp, store = LexComm(if_command2, Yaccer_Comm(), store, 1)
                      return temp,store  



                temp_condition, store = LexBool(condition, YaccerBool(), store)
                if temp_condition.eval(store):
                  #   print('in true')
                    temp, store = LexComm(if_command1, Yaccer_Comm(), store, 1)
                  #   print('temp', temp.eval(store))
                    return temp, store
                else:
                  #   print('false')
                    temp, store = LexComm(if_command2, Yaccer_Comm(), store, 1)
                  #   print('temp', temp.eval(store))
                    return temp, store



            elif flag_do != -1 and flag_while_do != 2:
               # print('in process do')
               condition = exprssn[flag_while+2:flag_do]
               while_command = exprssn[flag_do+2:cp+1] 
               # print('start process do ',condition, '|command|', while_command)
               temp_condition, store = LexBool(condition, YaccerBool(), store)
               # print("condition", temp_condition.eval(store), store)
               if temp_condition.eval(store):
                  while_command = while_command.split(";")
                  for command in while_command:
                     # print('executed command ', command, "before store", store)
                     temp, store = LexComm(command, Yaccer_Comm(), store, 1)
                     temp.eval(store)
                     if command == '!':
                        return temp, store
                     # print('executed command ', command, "after store", store)

                  temp_result = temp.eval(store)
                  # print("temp_result",temp_result)
                  # print('in while true',store)

                  temp, store = LexComm(exprssn, Yaccer_Comm(), store, 1)
                  return temp, store
               else:
                  temp, store= LexComm('!', Yaccer_Comm(), store, 1)
                  # print('while fase',store)
                  # print(SkipComm().eval(store))
                  # print('temp test', temp.eval(store))
                  return temp,store
                  # print('aha')

        
        else:
            char_flag = 1
            if bgn is None:
                bgn = cp
    # print(exprssn[flag_if])
    if bgn is not None:
        if 1 == 1:
            #  print('care')
            temp = Lex(str(exprssn[bgn:cp+1]), Yaccer(), store)
            temp_result = temp.eval(store)
            p.v(p, temp_result, store)
        else:
            p.v(p, exprssn[bgn:cp+1], store)
            bgn = None
#   print("end of lexCom", store)
    return p.end(), store


store = dict()

# temp = fen(Assign('i',IntAexp(0)),Assign('i',IntAexp(0)))
# print("yooo",temp.eval(store))

expr = input("")

# temp = Lex('1', Yaccer(), store)
# print("arith", temp.eval(store))


# expr = "x := 1 * 9 ; y := x + 1 ; if 5 > x then x := 2 - 2 else y := 9"
# expr = "x := 10 ; while x < 10 do x := x + 1"
# expr = "while ¬ ( x < 0 ) do x := -1"
# expr = "if ¬ ( x < 0 ) then x := 1 else x := 3"

# expr = "z := ( x8 + 1 ) * 4"
# expr = "if ( -1 < 0 ) then k := ( 49 ) * 3 + k else k := 2 * 2 * 2 + 3"

# expr = "i := -1 ; fact := 1 ; while 0 < i do { i := i + 1 }"
# # expr = "if "
# expr = " i := 1; x := 2"

# expr = "a := 369 ; b := 1107 ; while ¬ ( a = b ) do { if a < b then b := b - a else a := a - b }"
# expr = "i := -1 ; fact := 1 ; while 0 < i do { fact := fact * i ; i := i - 1 }"

# expr = "if false then while true do skip else x := 2"

# expr = "a := 369 ; b := 1107 ; while ¬ ( a = b ) do { if a < b then b := b - a else a := a - b }"

# expr = "i := -1 ; fact := 1 ; while 0 < i do { fact := fact * i ; i := i - 1 }"
# expr = "i := 5 ; fact := 1 ; while 0 < i do { fact := fact * i ; i := i - 1 }"
# expr = "if false then while true do skip else x := 2"

# expr ="while ( ¬ ( 0 - -1 < 2 + z ) ) do skip"
# expr = "if 1 = z * 4 then z := -1 else z := 2"
# expr = "while 0 + 1 = z do z := 1"

# expr = "while false do x := 1 ; y := 1"

# expr = "if x = 1 then x := 2 else if x = 0 then x := 4 else x := 10"
# expr = "if true then y := 1 else z := 1"

# expr = while ( ¬ ( 0 - -1 < 2 + z ) ) do skip ; while -1 * IY = 2 - L ∧ 0 + x < 2 + 2 do while ( ¬ ( z + S = z - -1 ) ) do if ( false ∨ NT + -3 = 3 ) then y := k * 0 else y := 0 - y
# expr = "while -1 * IY = 2 - L ∧ 0 + x < 2 + 2 do while ( ¬ ( z + S = z - -1 ) ) do if ( false ∨ NT + -3 = 3 ) then y := k * 0 else y := 0 - y"

expr = expr.replace(":=", ":")
expr = expr.replace("if", "@")
expr = expr.replace("then", "#")
expr = expr.replace("else", "$")
expr = expr.replace("while", "%")
expr = expr.replace("do", "&")
expr = expr.replace("skip","!")
# expr = expr.replace("{","")
# expr = expr.replace("}","")

expr_split = expr.split(";")

# print("yoo")
cp = -1
mark = -1
input_list = []
input_list_index = 0
for expr in expr_split:
   cp += 1
   # print("expr_split[cp]", expr_split[cp])
   if '{' in expr and '}' not in expr:
      expr_split[cp] = expr_split[cp].replace("{","")
      mark = cp
   elif '}' in expr and mark != -1:
      # print("in }")
      expr_split[cp] = expr_split[cp].replace("}","")
      temp = ""
      for i in range(mark, cp):
         temp += expr_split[i] + ';'
      temp += expr_split[cp]
      # print(temp)
      input_list.append(temp)
      mark = -1
   elif mark == -1:
      expr = expr.replace("{","")
      expr = expr.replace("}","")
      input_list.append(expr)
      # input_list_index += 1
   # print(expr)
# print('input list',input_list)
# print("aha")

for expr in input_list:
    # print("expr",)
    astTree, store = LexComm(expr, Yaccer_Comm(), store, 0)
    final_result = astTree.eval(store)
   #  print("final_result",final_result)

# test = SkipComm()
# print('test', test.eval(store))

# astTree = LexComm( expr_split[0], Yaccer_Comm(),store,0)
# print(astTree.eval(store))

# print('storeee', store)
# astTree2 = LexComm(expr_split[1], Yaccer_Comm(),store,0)


# print(astTree.eval(store))

# print("@#######")

#######
final_result = astTree.eval(store)

import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# sorted_x = sorted(x.items(), key=operator.itemgetter(1))
# print("test", sorted_x)
# print("sorted(mydict.keys())", sorted(final_result.items()))

output_string = "{"

for key, value in sorted(final_result.items(), key=lambda item: item[0]):
   #  print("%s → %s" % (key, value))
    output_string = output_string +  key + ' → ' + str(value) + ', '

if len(output_string) > 1:
   print (output_string[:-2]+ '}')
else:
    print (output_string+ '}')

# final_result = str(final_result)
# # print(final_result)

# final_result = final_result.replace(":", ' →')
# final_result = final_result.replace("'", '')
# print(final_result)
#

# print (astTree.eval(store))


# print('input expr',expr)
# expr = expr.replace("do", "&")
# astTree = LexComm( expr1, Yaccer_Comm(),store)
# print(store)
# print ('final',astTree.eval(store))
# print(store)

# if 'x' in store:
#   print("blah")
# else:
#   print("boo")
# test = Assign('xyz',IntAexp(233)).eval(store)

# test = Assign('xyzzz',IntAexp(astTree.eval())).eval(store)
# store = dict()


# test = Assign('xyz',IntExp(233)).eval(s)
# print(test)

# # a = GreaterBexp(IntExp(3),IntExp(3)).eval()
# # a = NotBexp(a).eval()

# a = Assign('x', IntExp(0)).eval(store)
# # # b = GreaterBexp(a,IntExp(3)).eval(store)
# print(a)

# # if a :
# #   print("yoo")
# # else:
# #   print("emmm")
# # print (expr, '=',astTree.eval())
