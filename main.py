def factorial(n):
  if n == 1:
    return 1
  return(n*factorial(n-1))


def main():
    factorial_of_5 = factorial(5)
    print(factorial_of_5)


if __name__== "__main__":
  main()
