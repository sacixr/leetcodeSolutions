'''Power of Three
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.
'''

# @param {Integer} n
# @return {Boolean}
def is_power_of_three(n)
  if n <= 0
    return false
  elsif n == 1
    return true
  else
    while true do
      if n == 1
        return true
      elsif n % 3 == 0
        n = n / 3
      else
        return false
      end
    end
    return false
  end
end

def is_power_of_three_rewritten(n)
  return false if n < 1
  while n % 3 == 0
    n /= 3
  end
  n == 1