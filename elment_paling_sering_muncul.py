from collections import Counter

def elment_terstring(lst):
    counter = Counter(lst)
    elment, jumlah = counter.most_common(1)[0]
    return elment, jumlah

data = [1,1,1,2,2,2,3,3,3,4,5,5,5,5]
elment, jumlah = elment_terstring(data)
print(f"element yang paling muncul: {elment} (sebanyak {jumlah} kali)")