def add(*args):
  sum = 0
  for n in args:
    sum += n
  return sum

print(add(3, 5, 6, 9, 8))


def calculate(n, **kwargs):
  print(kwargs)
  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)


calculate(6, add=5, multiply=5)
