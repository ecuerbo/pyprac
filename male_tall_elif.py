is_male = False
is_tall = True
if is_male and is_tall:
    print("you are a male or tall")
elif is_male and not(is_tall):
    print("you are a short male. eat more")
elif is_tall and not(is_male):
    print("you are short but not male. go away")
else:
    print("you are neither male nor tall")  