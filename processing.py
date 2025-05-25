import PyPDF2
import nltk
import re
import os
import tkinter as tk
def read_pdf_text(path):
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + ' '
    return text
def stopword_removal(word):
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
    newword=list()
    count=0
    Collection = list()
    for w in word :
        if w not in stopwords:
            newword.append(w)
            count += 1
    Collection.extend([count ,newword])
    return Collection
def normalization(word):
    text = re.sub(r'[።፣፤፥፦፧""]', '', word)
    text = re.sub(r'\s+', ' ', word).strip()
    return text
def tokenization(word):
        # using re module the program can split
    parts = re.split(r'[]', word)# add amharic words
    clean=[s.strip() for s in parts if s.strip()]
    return clean
def stemming(word):
    pass
document = input("Give me a document as path: ")
String = read_pdf_text(document)
