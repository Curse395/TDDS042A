# this is that and that is this we all are that but we all can be this
# you can use the above text for testing the code it looks fun nothing else 

def calculate(given_text):
    import string 
    text=""
    for ch in given_text:
        if ch not in string.punctuation:
            text+=ch
            
            words=text.split()
            word_frequncy={}
            for word in words:
                if word in word_frequncy:
                    word_frequncy[word]+=1
                else:
                    word_frequncy[word]=1
    return word_frequncy

text=input("Enter the text: ")
wfrequency=calculate(text)
for word,frequency in wfrequency.items():
    print(f"{word}: {frequency}")