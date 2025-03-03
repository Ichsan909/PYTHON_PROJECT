def hanya_angka(s):
    return s.isdigit()

string1 = "12345"
string2 = "123abc"

print(f"apakah '{string1}' hanya berisi angka?  {hanya_angka(string1)}")
print(f"apakah '{string2}' hanya berisi angka?  {hanya_angka(string2)}")