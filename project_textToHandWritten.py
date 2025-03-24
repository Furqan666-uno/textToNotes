import pywhatkit as pw

text= "This is sample text to convert text to handwritten note. "
pw.text_to_handwriting(text,[255,0,0]) 
# we can also give file names like 'file.png' if we want to store notes in that specific file
print("END")
