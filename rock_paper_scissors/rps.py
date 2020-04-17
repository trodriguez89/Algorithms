#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  plays = []
  def rock_paper_scissors_helper(arr,n):
    if n == 0:
      plays.append(arr)
    else:
      for item in rps:
        rock_paper_scissors_helper(arr + [item], n - 1 )
  rock_paper_scissors_helper([],n)
  return plays

print(rock_paper_scissors(4))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')