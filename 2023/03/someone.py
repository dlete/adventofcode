import re
with open('input_day03.txt')as N:O=[A.strip()for A in N.readlines()]
C,B,I,J=[],[],[],[]
for K in O:D=[{'n':A.group(1),'s':A.start()-1,'e':A.end()}for A in re.finditer('(\\d+)',K)];E=[{'c':A.group(1),'i':A.start()}for A in re.finditer('([^.\\d])',K)];B.append(D);C.append(E)
for(A,D)in enumerate(B):
	E=C[A]+(C[A-1]if A>0 else[])+(C[A+1]if A<len(B)-1 else[])
	for F in D:I+=(int(F['n'])for A in E if F['s']<=A['i']<=F['e'])
for(A,E)in enumerate(C):
	D=B[A]+(B[A-1]if A>0 else[])+(B[A+1]if A<len(B)-1 else[])
	for L in E:
		if L['c']=='*':
			G=[int(A['n'])for A in D if A['s']<=L['i']<=A['e']]
			if len(G)==2:J.append(G[0]*G[1])
print(sum(I),sum(J))