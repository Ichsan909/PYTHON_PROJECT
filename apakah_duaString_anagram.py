def apakah_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

kata1 = input("masukkan string 1: ")
kata2 = input("masukkan string 2: ")
if apakah_anagram(kata1, kata2):
    print("kedua string adalah anagram.")
else:
    print("kedua string bukan anagram.")