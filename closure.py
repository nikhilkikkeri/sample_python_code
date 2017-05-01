def f(x):
  def g(y):
    return x + y
  return g

a = f(1)
b = a(5)

c = f(2)
d = c(5)

for i in range(10):
  print a(i)
