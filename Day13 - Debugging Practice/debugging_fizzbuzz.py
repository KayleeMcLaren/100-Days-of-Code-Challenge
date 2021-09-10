
############DEBUGGING#####################

# Debug FizzBuzz:
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])


# Solution:
for number in range(1, 20):
  if number % 3 == 0 and number % 5 == 0:  # it should print fizzbuzz if the number is divisible by 3 and 5, not or
    print("FizzBuzz")
  elif number % 3 == 0:  # change if statements to elif so that fizz or buzz are printed and not the number
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)  # square brackets aren't necessary, otherwise it's printing each number as a list consisting of only that number
