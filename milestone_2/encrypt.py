abc = "abcdefghijklmnopqrstuvwxyz"
abc_shyfr = ""
line = "The quick brown fox jumps over the lazy dog."
key = int(input())
line_shyfr = ""
abc_shyfr = abc[-key:]
abc_shyfr += abc[:len(abc)-key]
if key >= len(abc):
    print("Error")
    exit(1)
for letter in line: 
    if not letter.isalpha():
        line_shyfr += letter
    elif letter.lower() in abc:
        is_upper = letter.isupper()
        index = abc.index(letter.lower())
        letter_shyfr = abc_shyfr[index]
        if is_upper:
            letter_shyfr = letter_shyfr.upper()
        line_shyfr += letter_shyfr
    else:
        line_shyfr += letter
        
print(line_shyfr)  


