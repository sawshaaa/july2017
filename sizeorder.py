#goal: re-order strings from shortest to longest
L = ["ATGC","A","TT","CACTAT"]
A = []

while len(L) > 0:
  x = L[0]
  pos = 0
  for i in range(len(L)):
    if len(x) > len(L[i]):
      x = L[i]
      pos = i
     
  A.append(x)
  del L[pos]

print A
