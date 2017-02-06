import csv
import json

data = []
names = []
d = {}
duplicate_victims={}
deduped=[]

def main():
  for row in csv.DictReader(open('gun-database.tsv'), delimiter='\t'):
    data.append(json.loads(row['Json']))
  for record in data:
    if len(record['victim-section']) > 0:
      if record['victim-section'][0]['name']['value'] != '':
        tup = []
        tup.append(record['victim-section'][0]['name']['value']) #victim name
        tup.append(data.index(record)) # index of victim name's record
        names.append(tup) #names is list of victim name:record tuples

def dup(names):
  # names is list of tuples from victim name:record
  for name_pair in names:
    if name_pair[0] in d.keys():
      indices = d[name_pair[0]]
      # add new index
      indices.append(name_pair[1])
      #dictionary of victim name to indices of records it appears in
      #d[name_pair[0]] = indices
    else:
      d[name_pair[0]] = [name_pair[1]]

  for victim in d:
    #dictionary of victim name to record indices iff # of indices >1
    if len(d[victim]) > 1:
      duplicate_victims[victim] = d[victim]

  for record in duplicate_victims:
    indices = duplicate_victims[record]
    for index in range( 0, len(indices)): # step through list of indices
      if index >= len(indices):
        break
      else:
        first_record = data[indices[index]]
      for i in range(index + 1,len(indices)):
        if i >= len(indices):
          break
        else:
          second_record = data[indices[i]] 
        first = can_merge(first_record,second_record)
        if first:
          del indices[i]
          output(first)
      
def can_merge(first_record,second_record):
  count = 0

  #SHOOTER
  if len(first_record['shooter-section']) and len(second_record['shooter-section']) > 0:
    if first_record['shooter-section'][0]['name']['value'] == second_record['shooter-section'][0]['name']['value']:
      count+=1
    if first_record['shooter-section'][0]['name']['value'] == "" and \
      second_record['shooter-section'][0]['name']['value'] != "":
      count+=1
    if second_record['shooter-section'][0]['name']['value'] == "" and \
      first_record['shooter-section'][0]['name']['value'] != "":
      count+=1

  #DATE
  if len(first_record['date-and-time']) and len(second_record['date-and-time']) > 0:
    if first_record['date-and-time']['date'] == second_record['date-and-time']['date']:
      count+=1
    if first_record['date-and-time']['date'] == "" and \
      second_record['date-and-time']['date'] != "":
      count+=1
    if second_record['date-and-time']['date'] == "" and \
      first_record['date-and-time']['date']  != "":
      count+=1

  if count > 1:
    first = merge(first_record,second_record)
    return first
  else: return False
  
def merge(first,second):
  if len(first['victim-section']) <= len(second['victim-section']) :
    first['victim-section'] = second['victim-section']

  if len(first['shooter-section']) <= len(second['shooter-section']):
    first['shooter-section'] = second['shooter-section']

  if len(first['date-and-time']) <= len(second['date-and-time']) :
    first['date-and-time'] = second['date-and-time']

  if len(first['circumstances']) <= len(second['circumstances']) :
    first['circumstances'] = second['circumstances']

  if len(first['radio1']) <= len(second['radio1']) :
    first['radio1'] = second['radio1']

  if len(first['radio2']) <= len(second['radio2']) :
    first['radio2'] = second['radio2']

  if len(first['radio3']) <= len(second['radio3']) :
    first['radio3'] = second['radio3']

  return first


def output(first):
  deduped.append(first)
    
  
#initialize  
main()
dup(names)
json.dump(deduped, open('deduped-data.json', 'w'))

    
      
    
    
