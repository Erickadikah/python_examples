def hash_int(n_chars, num):
    hv = n_chars % num
    return (hv)

num = 10

students = {"std1": 5, "std2": 7, "std3": 9, "std4": 56, "std5": 67, "std6": 50}
hs = {}
for k,v in students.items():
    hs[k] = hash_int(v, num)
    print("{}: {}".format(k, v))

print(hs)


