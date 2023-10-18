with open('cza.txt', 'r') as f:
    L = [x.strip() for x in f]
    n, k, a, b = L[0].split()
    s = L[1]

litery_set = set(list(s))

def czatBBB():
    global s
    global k
    while len(s) < int(b):
        litery = {}
        for litera in litery_set:
            litery[litera] = 0
        r = s[len(s)-int(k)::]
        for i in range(len(s)-int(k)):
            if s[i:i+int(k)] == r:
                litery[s[i+int(k)]] += 1

        if max(litery.values()) != 0:    
            s += max(litery, key = litery.get)
        else:
            s += 'a'
            litery_set.add('a')

czatBBB()
print(s[int(a)-1:int(b)])
