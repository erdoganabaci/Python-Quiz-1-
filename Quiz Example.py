print("*****Digit and Letter Calculator in any word******")
word = "abcd43264"
digit = []
letter = ["a","b","c","d","e","f"]
digit_list = []
letter_list = []
for i in range(0,10):
    digit.append(str(i))
for control in word:
    if control in digit:
        if control not in letter:
            digit_list.append(control)
    else:
        letter_list.append(control)
print(f"Your Word is :{word} Total digit in your word :{len(digit_list)} , Total letter in your word {len(letter_list)} ")

print("----Even Finder----")
def isEven(even):
    if even % 2 == 0:
        return True
    else:
        return False
num = int(input("Please Enter Number to Find is Even:"))
print(isEven(num))