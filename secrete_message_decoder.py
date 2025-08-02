def palin(st):
    return st==st[::-1]

def brut(s):
    m = ''
    x = []
    v=['a','e','i','o','u']
    for i in s:
        m = i + m

    for j in m:
        x.append(j)

    result = []
    for i in range(len(x)):
        if i % 3 != 0 or i==0:
            result.append(x[i])
        
    st=''.join(result)
    # print(st) 
    for k in st:
        if k in v:
            # print(k)
            u=k.upper()
            # print(u)
            st=st.replace(k,u)
    return st        
    
def main(s):
    i = 0
    while True:
        i += 1
        s = brut(s)  
        print(f"Iteration {i}: {s}")
        if palin(s):
            print("palindrome")
            break
        
        if i > 50:
            print("not possible")
            break
s='madamimadam'
# s='Programming'
# s='a'
# s='racecar'
main(s)
