from assignment9 import deduped

time1=['1',0,0]
time2=['2',0,0]
time3=['3',0,0]
time4=['4',0,0]
time5=['5',0,0]
time6=['6',0,0]
time7=['7',0,0]
time8=['8',0,0]
time9=['9',0,0]
time10=['10',0,0]
time11=['11',0,0]
time12=['12',0,0]
time13=['13',0,0]
time14=['14',0,0]
time15=['15',0,0]
time16=['16',0,0]
time17=['17',0,0]
time18=['18',0,0]
time19=['19',0,0]
time20=['20',0,0]
time21=['21',0,0]
time22=['22',0,0]
time23=['23',0,0]
time24=['24',0,0]

for i in range(0,len(deduped)):
    if deduped[i]['victim-section']!=[]:
        if deduped[i]['victim-section'][0]!=[]:
            if deduped[i]['victim-section'][0]['victim-was']!=[]:
                if deduped[i]['date-and-time']!=[]:
                    if deduped[i]['date-and-time']['time-day']!=[]:
                        if deduped[i]['date-and-time']['time-day']['value']!=[]:
                            if time1[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time1[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time1[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time1[2]+=1
                            if time2[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time2[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time2[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time2[2]+=1
                            if time3[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time3[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time3[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time3[2]+=1
                            if "early-morning" == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time4[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time4[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time4[2]+=1
                            if "early" == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time5[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time5[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time5[2]+=1
                            if time6[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time6[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time6[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time6[2]+=1
                            if time7[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time7[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time7[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time7[2]+=1
                            if "morning" == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time8[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time8[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time8[2]+=1
                            if time9[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time9[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time9[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time9[2]+=1
                            if time10[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time10[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time10[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time10[2]+=1
                            if time11[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time11[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time11[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time11[2]+=1
                            if time12[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time12[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time12[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time12[2]+=1
                            if "early afternoon" == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time13[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time13[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time13[2]+=1
                            if time14[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time14[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time14[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time14[2]+=1
                            if "afternoon" == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time15[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time15[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time15[2]+=1
                            if time16[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time16[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time16[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time16[2]+=1
                            if time17[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time17[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time17[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time17[2]+=1
                            if time18[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time18[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time18[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time18[2]+=1
                            if time19[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time19[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time19[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time19[2]+=1
                            if "night" == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time20[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time20[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time20[2]+=1
                            if time21[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time21[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time21[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time21[2]+=1
                            if "evening" == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time22[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time22[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time22[2]+=1
                            if time23[0] == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time23[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time23[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time23[2]+=1
                            if "midnight" == deduped[i]['date-and-time']['time-day']['value'].strip():
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "killed":
                                    time24[1]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "injured":
                                    time24[2]+=1
                                if deduped[i]['victim-section'][0]['victim-was'][0] == "hospitalized":
                                    time24[2]+=1
