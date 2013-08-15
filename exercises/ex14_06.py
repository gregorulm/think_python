import urllib
import string

def get_zip():
    zip_code = raw_input("Enter valid US zip Code, e.g. 32707: \n>")
    conn_str = "http://www.uszip.com/zip/" + zip_code
    
    conn = urllib.urlopen(conn_str)
    
    lines = []
    town = ""
    population = 0

    for line in conn:
        lines += [line.strip()]

    for i in range(len(lines)):
        
        if lines[i][:8] == "<hgroup>":
            s = lines[i+2]
            s = s[len("<h2><strong>"):]
            s = s[:s.find("<")]
            s = s.strip()
            
            for c in string.punctuation:
                s = s.replace(c, "")
            
            town = s
                
        if lines[i].lower().find("total population") != -1:
            s = lines[i]
            start = s.find("Total population") + \
                    len("Total population") + len("</dt><dd>")
            end = s.find("<span", start)
            population = s[start:end]
        
    print "You entered %s, which is the zip code for %s." % (zip_code, town)
    print "Population: %s" % (population)

get_zip()


"""
Program:

import urllib
conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
    print line.strip()


================
Text displayed:

Secret Think Python Exercise

If you are reading this, you are probably working on the urllib
exercise from Think Python.

Next, you should read the documentation of the urllib module at
http://docs.python.org/lib/module-urllib.html

Then go to www.uszip.com, which provides information about every zip code
in the country.  For example, the URL http://www.uszip.com/zip/02492
provides information about Needham MA, including population, longitude
and latitude, etc.

Write a program that prompts the user for a zip code and prints the
name and population of the corresponding town.

Note: the text you get from uszip.com is in HTML, the language most
web pages are written in.  Even if you don't know HTML, you should be
able to extract the information you are looking for.

By the way, your program is an example of a "screen scraper."  You can
read more about this term at http://wikipedia.org/wiki/Screen_scraping

Sites that make money from advertising don't like screen scrapers
because they don't display the ads.  Using a screen scraper violates
the terms of service for some sites; that's why this is a secret
exercise!
"""
