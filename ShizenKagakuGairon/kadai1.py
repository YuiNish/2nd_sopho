day = 200

for m in range(1, 12):
    
    if day <= 31:
        break
        
    if m == 2:
        day = day - 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        day = day - 30
    else:
        day = day - 31
        
print("%d月%d日が200日目である" % (m, day))