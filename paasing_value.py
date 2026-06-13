def clean_name(first_name):
    lo=first_name.lower()
    up=first_name.upper()
    return lo, up

cl = clean_name("TANMAY")
print(cl)
print(type(clean_name))