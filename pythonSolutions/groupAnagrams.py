'''Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

def groupAnagrams(strs):
  anagrams = {}

  # for every word in the list
  for word in strs:
      # if you are using anything before python 3, please uncomment the below line
      # word = word.encode('utf-8')
      # sort the letters and join the result into a "sorted word"
      sorted_word = ''.join(sorted(word))

      # if the sorted word is already in our anagram
      if sorted_word in anagrams:
          # append the actual word with the sorted word as our key
          anagrams[sorted_word].append(word)
      # else, it is not yet in our dictionary
      else:
          # store our new key with the word
          anagrams[sorted_word] = [word]
  
  # return the dictionary as a list
  return list(anagrams.values())

# If you would like to see this code working, please run the file and make sure you have python installed.
strs = ["eat","tea","tan","ate","nat","bat"]
print("Our strings are", strs)
print("Grouped Anagrams are:", groupAnagrams(strs))

strs = [""]
print("Our strings are", strs)
print("Grouped Anagrams are:", groupAnagrams(strs))

strs = ["a"]
print("Our strings are", strs)
print("Grouped Anagrams are:", groupAnagrams(strs))

strs = ["aba", "bc", "abb", "john", "hojn", "cameralistic", "acclimatiser"]
print("Our strings are", strs)
print("Grouped Anagrams are:", groupAnagrams(strs))