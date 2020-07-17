
is_male = False
is_tall = True

if is_male and is_tall:
     print("You are a tall male.")
elif not(is_male) and is_tall:
    print("you are a tall female")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and not(is_tall):
    print("You are a short female.")


