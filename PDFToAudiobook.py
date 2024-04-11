import PyPDF2
import pyttsx3
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

# path of the PDF file
path = open('/home/johnx/Documents/Business/001CompTIA-Security-SY0-701-Study-Guide.pdf', 'rb')

# creating a PdfReader object
pdfReader = PyPDF2.PdfReader(path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.pages[24]

# extracting the text from the PDF
text = from_page.extract_text()

# Splitting text into sentences
sentences = sent_tokenize(text)

# Reading and highlighting each sentence
speak = pyttsx3.init()
for sentence in sentences:
    # Highlighting functionality here
    # For simplicity, I'm using printing the sentence with some markers
    print("\n*** Highlight Start ***")
    print(sentence)
    print("*** Highlight End ***\n")
    speak.say(sentence)
    speak.runAndWait()