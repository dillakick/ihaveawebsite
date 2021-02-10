import dominate
from dominate.tags import *
import http.server
import socketserver

doc = dominate.document(title='Dominate your HTML')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header'):
        h1('I Haz A Webzite!')
        for i in ['home', 'about', 'contact']:
            a(i.title(), href='/%s.html' % i)

    with div():
        attr(cls='body')
        p('If you are seeing this, I need to know: Who is Joe?')
        
print(doc)
        
  # confirmation  
good = input("good? ")

if good == "yes" or "yea" or "yeah" or "ye" :
    print(doc, file=open("index.html", "w"))