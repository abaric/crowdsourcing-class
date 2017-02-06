from assignment9 import deduped
city=""
count = 0

for i in range(0,len(deduped)):
    if deduped[i]['date-and-time']!=[]:
        if deduped[i]['date-and-time']['state']!=[]:
            city = deduped[i]['date-and-time']['state']
            count += 1
        else:
            continue
    else:
        continue
                
    print ("%s" "%s")%(city, count)
    count = 0

