import sys
import urllib2
import json 
import csv
from bs4 import BeautifulSoup
import httplib


def get_text(url) : 
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  """
  This is a method for extracting the text from a url using BeautifulSoup. 

  url- string of the url from which we want to extract text
  """
  try:
    response = opener.open(url)
  except urllib2.HTTPError as e:
    sys.stderr.write(str(e.code)+" " +url + "\n")
    return " "
  except httplib.BadStatusLine:
    sys.stderr.write(url + "\n")
    return " "
  except httplib.IncompleteRead, e:                                                                                                            
    page = e.partial
    pass
  except:
    return ""
    
  text = response.read()
  soup = BeautifulSoup(text,'html.parser')
 # except httplib.IncompleteRead, e:
  #  page = e.partial

  ret = ''
  for p in soup.find_all('p'): 
    ret += ' '.join(p.text.encode('utf-8').split())
  return ret

if __name__ == '__main__':

  for url in sys.stdin : 
    url = url.strip()
   # try: 
    txt = get_text(url)
   # except urllib2.HTTPError: 
    #  sys.stderr.write(url + "\n")
     # continue
    if not(txt.strip() == ''):
      print '%s\t%s'%(url,txt)
