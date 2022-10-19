from langdetect import detect

text = input("Enter your text : ")
print("Language of text is : "+detect(text))
