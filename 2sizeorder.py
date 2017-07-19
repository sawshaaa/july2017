#rearranging the list a second time using only one list
L = ["ATGC","A","TT","CACTAT","TTT","ATATATATA"]

f = len(L) - 1
for m in range(f):
  x = L[m]
  for i in range(m,f):
    if len(x) > len(L[i]):
      x = L[m]
      y = L[i]

      z = x
      x = y
      y = z

      L[m] = x
      L[i] = y

print L
