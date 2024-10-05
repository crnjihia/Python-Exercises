def modify_string(s):
    if s.startswith("Is"):
        return s
    return "Is" + s

print(modify_string("Hello"))
