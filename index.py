import numpy as np

Ai = [[1,2,3,4,5,6],[2,6,9,12,15,18],[3,10,18,24,30,36],[4,14,27,40,50,60],[5,18,36,56,75,90],[6,22,45,72,100,126]]

bi=[-12,20,3]

def inversa(A):
  n=len(A)
  ix=np.zeros((n,n))
  ix=np.linalg.inv(A)
  return ix

Z=inversa(Ai)
print("Z: \n%s" % Z)