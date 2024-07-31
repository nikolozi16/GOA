lst = ["cindelaini", "subeliani", "margiani", "nika", "gio"]
count = 0

for i in lst:
    count += i.lower().count("a")
print(count)