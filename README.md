# domainchecker 
Checks expiration dates of domains.

## License
This software is released under the MIT license. Please the see the license in the LICENSE.md file, 
located at the root of the project. 

## Environment
The project was built using the following:
 * Slackware 14
 * Eclipse 3.8.2
 * python 2.7.3/2.6.6
 * pywhois (http://code.google.com/p/pywhois/)

## Requirements
The project requires the following:
 * python 2.6.6
 * pywhois (http://code.google.com/p/pywhois/) 
 * pywhois patch (pywhoisPT_parser_py.patch) applied, mentioned on issue 52 (Portuguese domains), if not yet on the most recent release 

## Installation on CentOS 6.3
 * su # as root
 * yum install mercurial # install mercurial
 * cd /tmp
 * hg clone https://code.google.com/p/pywhois # get pywhois
 * cd pywhois
 * python setup.py build
 * python setup.py install
 * exit #as normal user
 * cd ~
 * git clone https://code.google.com/p/domainchecker/
 * cd domainchecker
 * su # as root
 * patch /usr/lib/python2.6/site-packages/python_whois-0.2-py2.6.egg/whois/parser.py  pywhoisPT_parser_py.patch
 * exit # as normal user
 * cp dummyConfig.plist ~/.domainChecker.plist
 * cd ..
 * vim .domainChecker.plist # define the settings 

## Test  
 * python domainchecker/__main__.py 
 If all is well configured an email should arrive witn info about the defined domains.
 
## Crontab setup to send the info daily
 * crontab -e
 * @daily /usr/bin/python /home/vitor/domainchecker/__main__.py
 
  
  