# -*- coding: utf-8 -*-
#######################################
#
#   user_module.py
#   ユーザ定義関数用のmodule
#
#######################################


class user_module_demo():

    def __init__(self, txt):
        self.txt = txt
        self.init()

    def init(self):
        self.funk(self.txt)

    def funk(self,s):
        print s


def factorial(n):
	s=1;
	for k in range(1,n+1):
		s = s * k
	return s

def binomal(n,k):
	'''nCk'''
	return factorial(n)/ ( factorial(n-k) * factorial(k) )

def binomalVec(n):
	m = []
	for k in range(0,n+1):
		m.append(binomal(n,k))
	return m

if __name__ == '__main__':
    txt = '== user_module_demo =='
    # user_module_demo(txt)
    for j in range(0,10):
    	print j, ': ', factorial(j)

    n=5
    k=1
    m=[]
    for k in range(0,n+1):
		print binomal(n,k)
		b= binomal(n,k)
		m.append(b)
		print m

