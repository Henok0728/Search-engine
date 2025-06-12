import fitz
import os
import nltk
import re
# check if it's working good
class file_reading:
    @staticmethod
    def read_pdf_text(path):
        with fitz.open(path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    # working good
    @staticmethod
    def stopword_removal(tokens):
        stopwords = [
            "እኔ", "አንቺ", "አንተ", "እሱ", "እሷ", "እኛ", "እናንተ", "እነሱ",
            "ይህ", "ያ", "የዚህ", "የዛ", "ይሄ", "እነዚህ", "እነዚያ",
            "እንደ", "ወደ", "ከ", "በ", "ላይ", "በታች", "በኩል",
            "ያለ", "ነው", "ና", "ነች", "ናት", "ነን", "ናቸው",
            "ማን", "ምን", "መቼ", "የት", "እንዴት", "ለምን",
            "እንዲሁ", "ከዚያ", "ከዛ", "እስከ", "ስለ", "ስለምን",
            "እንኳን", "ደግሞ", "እየ", "እንደኛ", "እንዲሁም", "ሁሉ", "ሁሉም",
            "ያን", "እርሱ", "እርሷ", "ያች", "ያንን", "አሁን", "በዚህ",
            "ያም", "እኔም", "እርስዎ", "ያህል", "እዚያ", "በዚያ", "በዚህም"
        ]
        newword=list() # storing non - stop words
        count=0
        knownstopwords = list() # storing known stop words
        for w in tokens :
            if w not in stopwords:
                newword.append(w)
            else:
                knownstopwords.append(w)
        return [knownstopwords,newword]
    # removing the  amharic quotations
    #normalization is working good
    @staticmethod
    def normalization(word):
        punctuations ='።፣፤፥፦፧"""()!'
        newstring = str()
        word_punctuations = str()
        # removing the quotations
        for i in word:
            if i not in punctuations:
                newstring += i
            else:
                newstring += ""
                word_punctuations += i
        return [newstring,word_punctuations]
    # tokenization of the string is working good
    @staticmethod
    def tokenization(word):
        return word.split()
