import sys
import urllib2
import json 
import csv
import lxml.etree
import lxml.html

#Paste your own API key here
api_key = 'RAkqmHZyaEbzzWL1MPBjIMGR9la/ZJmMivi4LFbbhIU' 
#This is the request we will submit to Bing. The parameters begin afer the '?' character. 
#The main parameter we care about is the Query one, which tells Bing what to search for. 
#Once you have an account, you can explore the API more thoroughly here: https://datamarket.azure.com/dataset/explore/bing/search
requeststr = 'https://api.datamarket.azure.com/Bing/Search/v1/News?Query=%%27%s%%27&$skip=%d' 


def get_urls(query, num_iters=10) : 
  """
  This is a method for collecting urls using the bing API.

  query- the query you want to issue to Bing search
  num_iters- the number of times to issue the command, helps to deal with pagination
  """
  #We have to give Bing our password. Python's urllib2 provides a nice class for doing this.
  credentials = 'Basic ' + (':%s' % api_key).encode('base64').strip()

  #Here, we will keep track of how many urls we have seen, so that we can paginate correctly.
  #I.e. if we have seen 10 urls, we want to issue another query telling Bing to start at the 11th url
  offset = 0
  for i in range(0,num_iters): 
    sys.stderr.write("Querying Bing (iteration %d out of %d)\n"%(i, num_iters))
    url = requeststr%(query, offset)

    #Here, we provide our password (API key) and then issue the request
    request = urllib2.Request(url)
    request.add_header('Authorization', credentials)
    requestOpener = urllib2.build_opener()
    response = requestOpener.open(request).read()
    #print response

    #The query returns our results in ugly xml format. We can use the etree module to parse it
    doc = lxml.etree.HTML(response) 
    #print(lxml.etree.tostring(doc, pretty_print=True)) //prints text
    #This says only to look at the 'url' attribute of each entry
    entries = doc.xpath("//entry")

    for entry in entries:
      for thing in entry.find("content"):
        date = thing.find("date")
        link = thing.find("url")
        title = thing.find("title")
        if date is not None:
          print link.text + "\t" + date.text + "\t" + title.text

        # print thing.find("url").text.encode('ascii', 'ignore').decode('ascii') + "\t" + \
        # entry.find("date").text.encode('ascii', 'ignore').decode('ascii') + "\t" +  \
        # entry.find("time").text.encode('ascii', 'ignore').decode('ascii')
    offset+=1



if __name__ == '__main__':
    #Here we call the method, passing it a string as our query ("shooting")
    get_urls("gun")
    get_urls("shooting")
    get_urls("killed")
