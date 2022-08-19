import sys
class analysedText(object):
    # This method should take the argument text, make it lower case, and remove all punctuation. 
    # Assume only the following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?). Assign this newly formatted text to a new attribute called fmtText.
    def __init__(self, text):
        self.fmtText = text.lower().replace(".", "").replace("!", "").replace(",", "").replace("?", "")
    # This method should create and return dictionary of all unique words in the text, along with the number of times they occur in the text. 
    # Each key in the dictionary should be the unique word appearing in the text and the associated value should be the number of times it occurs in the text. 
    # Create this dictionary from the fmtText attribute.
    def freqAll(self):
        new_dict = {}
        new_text_list = self.fmtText.split(" ")
        uniq_word = set(new_text_list) #return a set with all the unique elements in the list
        for word in uniq_word:
            new_dict[word] = new_text_list.count(word)
        return new_dict
    #This method should take a word as an argument and return the number of occurrences of that word in fmtText.
    def freqOf(self, word):
        new_dict = self.freqAll()
        if word in new_dict:
            return new_dict[word]
        else:
            return 0


sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}
def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )

