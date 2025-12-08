'''Count Square Sum Triples
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
'''

# this could have definitely been done a lot simpler, probably using some maths
# for now though we stick with the brute force solution
class Solution(object):
  def countTriples(self, n):
    """
    :type n: int
    :rtype: int
    """

    count = 0

    # build up the dp table
    dp = [0 for _ in range(n)]
    for i in range(0, n):
      dp[i] = (i+1)**2
    
    vals = [x for x in range(0, n+1)]

    for i in range(0, n):
      for j in range(1, n):
        if i == j:
          continue

        if dp[i] + dp[j] > n**2:
          break
          
        if sqrt(dp[i] + dp[j]) in vals:
          count += 1
    
    return count