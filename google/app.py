from googletrans import Translator
from gtts import gTTS
t = Translator()

# s = "mera naam Manikanta hai"
n = input("Enter the text to translate: ")
con = input("Enter convert language (te/hi/en/ta): ")
convert = t.translate(text=n,dest=con)

print(convert.text)
s=gTTS(text=convert.text)
s.save("gtts102.mp3")
