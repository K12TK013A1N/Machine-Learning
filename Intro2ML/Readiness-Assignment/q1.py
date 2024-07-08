# q21
def add_two_lists(a,b):
  c=[]
  for i,j in zip(a,b):
    c.append(i+j)
  return c

def dot(v1,v2):
  c=0
  for i,j in zip(v1,v2):
    c += i*j
  return c

def add_n(n):
  def fxn(arr):
    c = []
    for i in arr:
      c.append(i+n)
    return c
  return fxn

def array_mul(A,B):
  nRowsA = len(A)
  nRowsB = len(B)
  nColB = len(B[0])
  c = [[0 for _ in range(nColB)] for _ in range(nRowsA)]
  print(c);
  for i in range(nRowsA):
    for j in range(nColB):
      for k in range(nRowsB):
        c[i][j] += (A[i][k] * B[k][j])
  print(c)


if __name__ == "__main__":
  a = [1,2,-1]
  b = [4,5,7]
  print(add_two_lists(a,b))
  print(dot(a,b))
  print(add_n(10)([1,5,3]))
  M1 = [[1, 2, 3], [-2, 3, 7]]
  M2 = [[1,0,0],[0,1,0],[0,0,1]]
  array_mul(M1,M2)
  