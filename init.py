from NumberToWord import NumberToWord

numbertoword = NumberToWord()

input_value = raw_input("Enter the number to convert: \n")
word = numbertoword.ConvertToWord(input_value)

print ("Your number expressed in words is:\n")
print (word)
