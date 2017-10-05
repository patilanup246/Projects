from xml.dom import minidom
f = open('outbound_all.txt','w')
for i in range(1,100):
    print i
    xmldoc = minidom.parse('Downloads/outbound'+str(i)+'.txt')
    itemlist = xmldoc.getElementsByTagName('loc')

    for s in itemlist:
        f.write(s.firstChild.nodeValue + '\n')
    f.flush()