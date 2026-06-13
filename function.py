def clean_split(email):
    valid_email=email.strip().lower()

    username,domain=valid_email.split("@")

    return { "username" : username, "doamin" : domain}

print(clean_split(" TanmAysahoo@gmail.com"))