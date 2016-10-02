from __future__ import print_function
import sys

ERR = "Please enter a confidence, as a decimal number."

def petersburg(v):
  flips = 0
  p = 1
  while p > v:
    flips += 1
    p *= 0.5
  pay = 2**flips
  return "There's only a %s chance that you'll win more than $%d" % (p, pay)

if __name__ == "__main__":
  if len(sys.argv) < 2 or "h" in sys.argv[1]:
    print("Argument missing:", ERR)
  else:
    try:
      v = float(sys.argv[1])
      print(petersburg(v))
    except ValueError:
      print("'%s' isn't a valid decimal number. %s" % (sys.argv[1], ERR))
