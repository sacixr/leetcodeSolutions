=begin Roman Numerals to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
Given a roman numeral, convert it to an integer.
=end

# @param {String} s
# @return {Integer}
def roman_to_int(s)
  result = 0
  index = 0
  while index <= s.length - 1
    case s[index]
    when 'I'
      if index + 1 < s.length && %w[V X].include?(s[index + 1])
        if s[index + 1] == 'V'
          result += 4
          index += 2
        elsif s[index + 1] == 'X'
          result += 9
          index += 2
        end
      else
        result += 1
        index += 1
      end
    when 'V'
      result += 5
      index += 1
    when 'X'
      if index + 1 < s.length && %w[L C].include?(s[index + 1])
        if s[index + 1] == 'L'
          result += 40
          index += 2
        elsif s[index + 1] == 'C'
          result += 90
          index += 2
        end
      else
        result += 10
        index += 1
      end
    when 'L'
      result += 50
      index += 1
    when 'C'
      if index + 1 < s.length && %w[D M].include?(s[index + 1])
        if s[index + 1] == 'D'
          result += 400
          index += 2
        elsif s[index + 1] == 'M'
          result += 900
          index += 2
        end
      else
        result += 100
        index += 1
      end
    when 'D'
      result += 500
      index += 1
    when 'M'
      result += 1000
      index += 1
    end
  end
  result
end
