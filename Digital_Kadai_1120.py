#入力した値まで「1×2−3×4+5×6−7×8+9×10−...」と続く式の答えが返ってくるプログラム

a=0
j=1
c=0
k=1
print("偶数を入力")
n=input()

for i in range(1, (int(n)+1),2):
    j=i
    if j == (4*k-1):
        a= -j*(j+1)
        c+=a
        k+=1
    else:
        a=j*(j+1)
        c+=a
    
print(c)
