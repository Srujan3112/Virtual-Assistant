from speak_module import speak
import os
import sys
import PyPDF2
doc_path = "/home/srujan/Documents/"
def pdf_handler():
    speak("Boss enter the name of the book which you want to read")
    n = input("Enter the book name: ")
    n = n.strip()+".pdf"
    book_n = open(doc_path+n,'rb')
    pdfReader = PyPDF2.PdfFileReader(book_n)
    pages = pdfReader.numPages
    speak(f"Boss there are total of {pages} pages in this book")
    speak("please enter the page number Which I need to read")
    num = int(input("Enter the page number: "))
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)