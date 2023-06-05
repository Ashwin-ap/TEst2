# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s):
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    for i in range(len(s)):
        if char_freq[s[i]] == 1:
            return i

    return -1

s = "leetcode"
print(firstUniqChar(s))