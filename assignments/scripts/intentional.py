from assignment9 import deduped
city=""
intent=0

for i in range(0,len(deduped)):
    if deduped[i]['date-and-time']!=[]:
         if deduped[i]['date-and-time']['city']!=[]:
             if deduped[i]['date-and-time']['city']['value']!=[]:
                 city = deduped[i]['date-and-time']['city']['value']
             else:
                 city=""
         else:
             city=""
                
    if deduped[i]['radio3']!=[]:
        if deduped[i]['radio3']['The shooting was unintentional.'] != []:
            if deduped[i]['radio3']['The shooting was unintentional.'] == "No":
                intent += 1
            else:
                intent += 0
        else:
            intent += 0

    print ( "[" + "'" + '%s' + "'" +","+"%s"+"]" + "," )%(city,str(intent))
    count = 0

