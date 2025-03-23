def bandingkan_string(str1, str2):
    if str1 == str2:
        return "kedua string sama"
    else:
        return "kedua string beda"
    
string1 = input("masukkan string 1: ")
string2 = input("masukkan sring 2 : ")

hasil = bandingkan_string(string1, string2)
print(hasil)