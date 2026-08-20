text=input("enter the text:")
words=text.split()
word_count={}
for word in words:
    word=word.lower()
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print("word count:")
print(word_count)