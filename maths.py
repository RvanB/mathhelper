import sys
  
# Extended Euclidean Algorithm
def eea(a, b, c, silent):

  if not silent:
    print("x", "y", "c", "sol", sep='\t') 
  def p(x, y, r):
    if r != 0 and c % r == 0:
      f = c // r
      if not silent:
        print(x, y, r, '('+str(x*f)+', '+str(y*f)+')',sep='\t')
      return [x * f, y * f]
    else:
      if not silent:
        print(x, y, r, sep='\t')
      return None

  # ax + by = c
  xi, yi = 1, 0
  xj, yj = 0, 1
  ri, rj = a, b

  if (b > a):
    xi, yi = 0, 1
    xj, yj = 1, 0
    ri, rj = b, a

  solution = None
  s = p(xi, yi, ri)
  if solution is None:
    solution = s
  while rj != 0:
    f = ri // rj
    
    s = p(xj, yj, rj)
    if solution is None:
        solution = s
    ri, rj = rj, (ri % rj)
    xi, xj = xj, (xi - f * xj)
    yi, yj = yj, (yi - f * yj)

  s = p(xj, yj, rj)
  if solution is None:
    solution = s
  return solution

# Combine congruences with non-coprime mods
# x = a[0] (mod a[1]) = b[0] (mod b[1])
# gcd(a[1], b[1]) > 1
def reduce(congs):
  dk = abs(a[1] - b[1])
  dr = abs(a[0] - b[0])
  
# Chinese Remainder Theorem
# input congruences must have pairwise coprime moduli
def crt(congs, silent):

  N = 1
  for c in congs:
    N = N * c[1]

  for i in range(len(congs)):
    inv = eea(N // congs[i][1], congs[i][1], congs[i][0], silent)
    if inv is None:
      return
    congs[i] = (N // congs[i][1]) * inv[0]

  sum = 0
  for c in congs:
    sum = sum + c

  return [sum % N, N]

if __name__ == "__main__":
  s = sys.argv[1]
  if s == "eea":
    print(eea(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), False))
  elif s == "crt":
    print(crt([
      [4, 5],
      [5, 6],
      [0, 7],
      ], True))

