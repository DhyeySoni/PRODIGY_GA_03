import markovify

filename="text.txt"

file=open(filename)
text=file.read()
model=markovify.Text(text,state_size=1)
print(model.make_sentence())