""""
FUNCTION hash_integer(hash_key, number_of_slots)
    // Generate the hash value using the modulo operator
    hash_value = hash_key MOD number_of_slots

    // Return the hash value
    RETURN hash_value
ENDFUNCTION
"""
def hash_int(n_chars, num):
        hv = n_chars % num
        return (hv)


num = 10
"""
std1 = 5
std2 = 4
std3 = 6
std4 = 4
std5 = 7
std6 = 15

a = hash_int(std1, num)
print(a)
"""
students = {"std1": 5, "std2": 4, "std3": 6, "std4": 4, "std5":7, "std6": 15}
hs = {}
for k,v in students.items():
    hs[k] = hash_int(v, num)
    print("{}: {}".format(k, v))

print(hs)