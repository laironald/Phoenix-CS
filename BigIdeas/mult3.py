import copy
import random


def create_matrix(n):
  A = []
  for i in xrange(n):
    A.append([])
    for j in xrange(n):
      A[i].append(random.randint(0, 9))
  return A

def mult_matrix(a, b):
  C = [[0]*len(b[0]) for i in xrange(len(a))]
  for i in xrange(len(a)):
    for j in xrange(len(b[0])):
      C[i][j] = 0
      for k in xrange(len(a)):
        C[i][j] = C[i][j] + a[i][k] * b[k][j]
  return C

def make_bug(a):
  #switch two random numbers.  if same number try again
  import copy
  b = copy.deepcopy(a)
  while True:
    i = [random.randint(0, len(a)-1), random.randint(0, len(a)-1)]
    j = [random.randint(0, len(a)-1), random.randint(0, len(a)-1)]
    if a[i[0]][i[1]] != a[j[0]][j[1]]:
      c = b[i[0]][i[1]]
      b[i[0]][i[1]] = b[j[0]][j[1]]
      b[j[0]][j[1]] = c
      break
  return b

file = open("mult3.out", "wb")
for n in range(2, 33):
  a = create_matrix(n)
  b = create_matrix(n)
  c1 = mult_matrix(a,b)
  c2 = make_bug(c1)
  for i in xrange(100):
    file.write("{n},{i}")
    for k in xrange(10):
      k = k + 1
      r = [[[-1,1][random.randint(0,1)]] for j in xrange(len(a))]
      n1 = mult_matrix(c1, r)
      n2 = mult_matrix(c2, r)
      file.write(",{k}".format(k=1*(n1!=n2)))
    file.write("\n")
