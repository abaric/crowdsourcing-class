#!/usr/bin/python

import sys
import urllib
import urllib2
from cookielib import CookieJar
import lxml.etree
import lxml.html
import re


"""
This script was written to extract the external links from the New York Times 
Gun Report blog. The goal is to collect a set of training instances for a 
text classifier that can predict whether an article does or does not describe 
gun violence. 
"""

#we want to follow links that keep us on the gun report blog (i.e. we don't want to start crawling the entire web, just the gun report
DOMAIN = 'http://www.gunviolencearchive.org/' 

def crawl(root_url, domain=''):
  """ 
  Crawl the specified link and output a set of links from that page 
  root_url - string specifying the url to begin the crawl from
  domain - only following links within the given domain (will still print out all links found)
  Note: We are only going to look at pages within the domain DOMAIN. If you want to extend 
  this code to a larger domain (e.g. all of nytimes) you might want to add parameters to limit the depth of the search.
  """
  #Keep track of nodes we have alread visited, so we don't get caught in a loop
  visited = set()
  #Keep track of new links to explore
  stack = [root_url]

  # The NYTimes redirects you if you don't have cookies set.
  # It also limits you from viewing more than a handful of pages without a subscription.
  # So create a cookie jar and repeatedly empty it.
  cj = CookieJar()

  #Keep going until we run out of links to explore
  while len(stack) > 0: 
  # if you want to process the whole stack, then indent the remainder of this funciton.
  # Here we're just going to process one URL.

	url = stack.pop()

#  if url in visited: 
#    continue

	sys.stderr.write("Crawling from page %s\n"%url)
        
	#Clear our cookies so NYTimes doesn't catch on to us
	cj.clear() 
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	#Set some variables that makes it look like you are coming from a browser (in this case, Firefox) and not from a sketchy bot. :) 
	#Some sites will block you if they know you are a bot (you will get a 403 error).
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	#Grab the entire webpage
        site = opener.open(url).read() 
	#Parse the html into a data structure you can work with
        doc = lxml.etree.HTML(site) 

	#This is ugliness that pulls out all the elements of the html tree that are interesting. 
	#Honestly, I often play guess-and-check to get it right. You can read about the details of xpath if you care: http://lxml.de/xpathxslt.html
	#NOTE: You might need to change this for Step 4 of the assignment. You can get some more help with xpath here: http://crowdsourcing-class.org/xpath-examples.html
	result = doc.xpath("//tr//a") 
	#This is the pattern we match to know whether or not the thing we are looking at is a url
        link = re.compile('href="(.*?)"') 
        for item in result:
            source = lxml.html.tostring(item)
            #Returns None if there is nothing to look at in this item
            if link.search(source): 
	      #Get the actual url out of the link
              link_address = link.search(source).group(1) 
	      #Print it to standard out. Only print external http links, to avoid dealing iwth weird internal links like /incident/498052
	      if link_address.startswith('http'):
                print link_address 
              #If these links are in our domain of interest, add them to our stack, so we can crawl them too
              if link_address.startswith(DOMAIN) and link_address not in visited: 
	        stack.append(link_address)
	        visited.add(link_address)

if __name__ == "__main__":
   #There are 35 pages of gunreport posts. Nothing fancy, I just looked in my browswer to see how many there were: 
   #The pages are listed like this: http://nocera.blogs.nytimes.com/category/gun-report/page/PAGE_NUM/
   #So we will run a crawl starting from each page independently.
   for i in range(0,10): 
     crawl('http://www.gunviolencearchive.org/last-72-hours?page=%s'%i, domain=DOMAIN)



