def approximate_pi(n_terms):
  list_of_numbers = []
  sign = 1
  denom = 1
  for i in range(n_terms):
    num = sign/denom
    list_of_numbers.append(num)
    sign *= -1 #sign = sign *(-1)
    denom += 2
  pi = sum(list_of_numbers)
  pi *= 4
  return pi
