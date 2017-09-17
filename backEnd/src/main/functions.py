# @Author: andreacasino
# @Date:   2017-09-15T12:25:00+01:00
# @Last modified by:   andreacasino
# @Last modified time: 2017-09-15T19:20:11+01:00
import string

def isPalindrome(text):
    #Remove any punctuation, new lines, capitalization and spaces
    exclude = set(string.punctuation)
    outputText = ''.join(ch for ch in text.lower().replace(" ", "").replace("\n", "") if ch not in exclude)

    if outputText == outputText[::-1] and outputText!="":

        return True

    return False
