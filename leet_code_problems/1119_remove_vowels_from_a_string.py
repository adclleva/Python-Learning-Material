class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = "aeiou"
        newStr = ""

        for character in S:
            if character not in vowels:
                newStr += character

        return newStr

# Runtime: 8 ms, faster than 97.53% of Python online submissions for Remove Vowels from a String.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Remove Vowels from a String.