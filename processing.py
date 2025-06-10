
import fitz
import nltk
import re
import os
def read_pdf_text(path):
    with fitz.open("document.pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text
def stopword_removal(words):
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
    for w in words :
        if w not in stopwords:
            newword.append(w)
            count += 1
        else:
            knownstopwords.append(w)
    return newword
def normalization(word):
    text = re.sub(r'[።፣፤፥፦፧""]', '', word)
    text = re.sub(r'\s+', ' ', word).strip()
    return text
def tokenization(word):
        # using re module the program can split
    parts = re.split(r'[]', word)# add amharic words
    clean=[s.strip() for s in parts if s.strip()]
    return clean


document = input("Give me a document as path: ")
String = read_pdf_text(document)
print(String)
