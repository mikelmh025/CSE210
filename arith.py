#Followed these blog posts. Build AST and plug in the ARITH language. 

# https://ruslanspivak.com/lsbasi-part7/
# https://rosettacode.org/wiki/Arithmetic_evaluation#Python
# 
# Used pyinstaller for makefile, learn how to write one from this website
# https://github.com/operatorequals/covertutils/blob/master/makefile
# Which is just some random git repo used pyinstaller


import operator
 
class AstNode(object):
   def __init__( self, opr, left, right ):
      self.opr = opr
      self.l = left
      self.r = right
 
   def eval(self):
      return self.opr(IntExp(self.l.eval()), IntExp(self.r.eval())).eval()
        
 
class Exp(object):
	def __init__(self):
		self.e = None
	def eval (self):
		return

class IntExp(Exp):
	def __init__(self, n):
		self.e = int(n)
		# print("n",n)

	def eval(self):
		return self.e

class SumExp(Exp):
	def __init__(self,e1,e2):
		self.e1 = e1
		self.e2 = e2
	def eval(self):
		return self.e1.eval() + self.e2.eval()

class MultExp(Exp):
	def __init__(self,e1,e2):
		self.e1 = e1
		self.e2 = e2
	def eval(self):
		return self.e1.eval() * self.e2.eval()
	

class MinusExp(Exp):
	def __init__(self,e1,e2):
		self.e1 = e1
		self.e2 = e2
	def eval(self):
		return self.e1.eval() - self.e2.eval()

class PowExp(Exp):
	def __init__(self,e1,e2):
		self.e1 = e1
		self.e2 = e2
	def eval(self):
		return pow(self.e1.eval() , self.e2.eval())
	

 
class Yaccer(object):
   def __init__(self):
      self.operstak = []
      self.nodestak =[]
      self.__dict__.update(self.state1)
 
   def v1( self, valStrg ):
      # Value String
      # print("valStrg",valStrg)
      self.nodestak.append( IntExp(valStrg))
      self.__dict__.update(self.state2)
      #print 'push', valStrg
 
   def o2( self, operchar ):
      # Operator character or open paren in state1
      def openParen(a,b):
         return 0		# function should not be called
 
      opDict= { '+': ( SumExp, 2, 2 ),
         '-': (MinusExp, 2, 2 ),
         '*': (MultExp, 3, 3 ),
         '^': (PowExp, 4, 4 ),

         }
      operPrecidence = opDict[operchar][2]
      #print("opDict[operchar]",opDict[operchar])
      self.redeuce(operPrecidence)
 
      self.operstak.append(opDict[operchar])
      self.__dict__.update(self.state1)
      # print 'pushop', operchar
 
   def syntaxErr(self, char ):
      # Open Parenthesis 
      print ('parse error - near operator "%s"' %char)
 
   
   def end(self):
      self.redeuce(0)
      return self.nodestak.pop()
 
   def redeuce(self, precidence):
      # print("precidence",precidence,"self.operstak",self.operstak)
      while len(self.operstak)>0:
         tailOper = self.operstak[-1]
         if tailOper[1] < precidence: break
 
         tailOper = self.operstak.pop()
         vrgt = self.nodestak.pop()
         vlft= self.nodestak.pop()
         self.nodestak.append( AstNode(tailOper[0], vlft, vrgt))
         # print 'reduce'
 
   state1 = { 'v': v1, 'o':syntaxErr, 'po':o2 }
   state2 = { 'v': syntaxErr, 'o':o2, 'po':syntaxErr}
 
 
def Lex( exprssn, p ):
   bgn = None
   cp = -1
   for c in exprssn:
      cp += 1
      if c in '+*^':         # throw in exponentiation (^)for grins
        #  print("+-*cp, bgn", cp, bgn)
         if bgn is not None:
            #print("cp, bgn", cp, bgn, exprssn[bgn:cp])
            p.v(p, exprssn[bgn:cp])
            bgn = None
         
         p.o(p, c)
      elif c in ' \t':
         if bgn is not None:
            p.v(p, exprssn[bgn:cp])
            bgn = None
      elif c in '0123456789':
         if bgn is None:
            bgn = cp
      elif c in '-':
        #  print("cp, bgn", cp, bgn, exprssn[bgn:cp])
        #  print("length", exprssn[cp+1:cp+2])#==' ')
         if exprssn[cp+1:cp+2] == ' ':
            if bgn is not None:
                p.v(p, exprssn[bgn:cp])
                bgn = None
            p.o(p, c)
         else:
           if bgn is None:
             bgn = cp   
      else:
         print ('Invalid character in expression')
         if bgn is not None:
            p.v(p, exprssn[bgn:cp])
            bgn = None
   
   if bgn is not None:
      p.v(p, exprssn[bgn:cp+1])
      bgn = None
   return p.end()
 
 
expr = input("")
astTree = Lex( expr, Yaccer())
print (astTree.eval())
# print (expr, '=',astTree.eval())