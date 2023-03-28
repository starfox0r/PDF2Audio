import PyPDF2
from gtts import gTTS

# PDF-Datei öffnen und Textinhalt extrahieren
pdf_file = open('test.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()

# Text-to-Speech-Konvertierung
tts = gTTS(text, lang='de')
tts.save("output.mp3")