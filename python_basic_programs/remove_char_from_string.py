inp_Str= "abcdefabcdef"
output=""
for ch in inp_Str:
    if ch not in output:
        output+=ch
print(output)
