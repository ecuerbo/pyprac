is_male = bool(input("are you male? 1 or 0: "))
is_tall = bool(input("are you tall? 1 or 0: "))
if is_male and is_tall:
    print("you are a male or tall")
elif is_male and not(is_tall):
    print("you are a short male. eat more")
elif is_tall and not(is_male):
    print("you are a short but not male. go away")
else:
    print("you are neither male nor tall")  