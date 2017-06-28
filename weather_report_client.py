

#Importing request library for making connection and posting soap request.
import requests

#importing  sax util library to perform unescape
from xml.sax import saxutils as su

#importing ElementTree library for parsing 
import xml.etree.ElementTree as p

#importing hashlib for performing reload and switchcase.
import hashlib



#Header type.
headers_data_type = {'content-type': 'text/xml'}

#SOAP REQUEST ENCODED in XML STYLE
SOAPREQUEST = """<?xml version="1.1" encoding="UTF-8"?>
<SOAP:Envelope xmlns:SOAP="http://schemas.xmlsoap.org/soap/envelope/" xmlns:A="http://www.w3.org/2001/XMLSchema" xmlns:B="http://www.w3.org/2001/XMLSchema-instance" xmlns:namespace="http://schemas.xmlsoap.org/soap/encoding/" SOAP:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<SOAP:Body>
<ns3591:NDFDgen xmlns:ns3591="uri:DWMLgen">
<latitude B:type="A:string">30.2672</latitude>
<longitude B:type="A:string">-97.7431</longitude>
<product B:type="A:string">time-series</product>
<startTime B:type="A:string">2017-05-01T02:00:00-04:00</startTime>
<endTime B:type="A:string">2017-05-03T14:00:00-04:00</endTime>
<Unit B:type="A:string">e</Unit>
<weatherParameters>
<maxt B:type="A:boolean">1</maxt>
<mint B:type="A:boolean">1</mint>
<temp B:type="A:boolean">1</temp>
<snow B:type="A:boolean">1</snow>
<waveh B:type="A:boolean">1</waveh>
<wdir B:type="A:boolean">1</wdir>
<td B:type="A:boolean">1</td>
<wspd B:type="A:boolean">1</wspd>
<maxrh B:type="A:boolean">1</maxrh>
</weatherParameters>
</ns3591:NDFDgen>
</SOAP:Body>
</SOAP:Envelope> """


#End Point connection URL
url = "https://graphical.weather.gov:443/xml/SOAP_server/ndfdXMLserver.php"

#Performing the requst to the NDFD SOAP server and posting the soaprequest , requesting the data.
response = requests.post(url, data=SOAPREQUEST, headers=headers_data_type)

#print(response.content)

#COllecting the soap response
data=response.content

result=su.unescape(data) #As the response that i was getting from the server in the XML format the "<" are getting converted in to &lt and the ">" are getting converted to &gt.
print(result)  #printing out the Soap request

#parse= p.fromstring(result)  #//// (this part of the code is been commented with the # because it is  now working as excpeted...)

#TEMP=parse.findall("temperature")

#for x in TEMP:
    #x.find("name")
    #print(x)  
   # x.find("value")
   # print(x)
#parse= p.fromstring()

#WS=parse.findall("wind-speed") 

#for y in WS:
    #y.find("name")
   # print(y)  
   # y.find("value") 
   # print(y)

#snow=parse.findall("precipitation") 

#for s in snow:
    #s.find("name")
    #print(s)  
   # s.find("value") 
   # print(s)


#Hmd=parse.findall("humidity") 

#for j in Hmd:
  #  j.find("name")
  #  print(j)  
   # j.find("value") 
   # print(j)

#ENding the Soap connection using the timeout functionality and get method.
end = requests.get(url, timeout=10.0) 

#Function to terminate the server.
def DONOT():
            print "TERMINATED....."

#Function to Reload the data abd refresh the Soaprequest
def refresh():
              print " RELOADING......SENDING THE SOAP REQUEST..."
              print(result)

#Options to chose form the command line and then calling the function.
options = {0 : DONOT,
           1 : refresh,
}

#CHoosing the options.
re='The Request is been closed do you want to refresh : 0=TERMINATE 1=RELOAD'

#Printing the options.
print(re)

#Defining the num variable with its initial characters
num=input("0,1")

#hashstring for taking inputs from the users on the command line.
hashString=options[num]()
