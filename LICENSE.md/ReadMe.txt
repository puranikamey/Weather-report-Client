 Weather client using XML.
? This application is developed using developed on the integrated development environment
Pycharm, in Python 2.7 (r27:82525, Jul 4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)]
on win32
The Modules for this application that need to be installed are
• Pip install requests
• Install requests (Security)
? Once all the modules are been installed we can run this application through the Python
Idle or through command prompt or through Python terminal.
? The soap request is been sent using request. Post method of the python request library.
? The response that is been received is in XML format.
? The name of the file is Weather_report_client.py.
Challenges faced while creating this application:- When the SOAP request was sent to the
NDFD soap servers, the response that got back in xml was not in proper xml format. The
tags "<, > " got changer to "&lt , &gt" and "" in to &quot. To overcome this challenge I
have used saxutils library to un-escape the data coming as a response.

References :
The entire application is developed independently, however I have taken some references to from
following links understand and clear some doubts.
Endpoint link:-https://graphical.weather.gov:443/xml/SOAP_server/ndfdXMLserver.php
Link:- http://stackoverflow.com/questions/18175489/python-soap-using-requests
Link :- https://graphical.weather.gov/xml/docs/SOAP_Requests/NDFDgen.xml