def palindrome(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(' ','')
    return sentence == sentence[::-1]
    
