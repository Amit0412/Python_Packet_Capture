#! /usr/bin/python
import pcapy
devices=pcapy.finalldevs() 
inf=devices[0]

cap=pcapy.open_live(inf, 65536,1,0) 

count=1

while count:
(header, payload) =cap.next() 
print count
count+=1
