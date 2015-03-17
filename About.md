# domainchecker #
Checks expiration dates of domains.

## License ##
This software is released under the MIT license. Please the see the license in the LICENSE.md file,
located at the root of the project.

## Environment ##
The project was built using the following:
  * Slackware 14
  * Eclipse 3.8.2
  * python 2.7.3/2.6.6
  * pywhois (http://code.google.com/p/pywhois/)

## Requirements ##
The project requires the following:
  * python 2.6.6
  * pywhois (http://code.google.com/p/pywhois/)
  * pywhois patch (pywhoisPT\_parser\_py.patch) applied, mentioned on [issue 52](https://code.google.com/p/domainchecker/issues/detail?id=52) (Portuguese domains), if not yet on the most recent release

## Installation on CentOS 6.3 ##
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
  * patch /usr/lib/python2.6/site-packages/python\_whois-0.2-py2.6.egg/whois/parser.py  pywhoisPT\_parser\_py.patch
  * exit # as normal user
  * cp dummyConfig.plist ~/.domainChecker.plist
  * cd ..
  * vim .domainChecker.plist # define the settings

## Test ##
  * python domainchecker/main.py

If all is well configured an email should arrive with information about the defined domains.

## Crontab setup to send the info daily ##
  * crontab -e
  * @daily /usr/bin/python /home/vitor/domainchecker/main.py

## Check whois entries in a specific WHOIS server ##
Requests made to different servers, for the same domain, may give different outputs.

In 2013-10-13, for the domain moovetruck.com, the expiration date for the domain was different between two whois servers. The data structure is also different.

Requests made in a bash shell that shown the differences:
  * WHOIS\_SERVER=whois.verisign-grs.com whois -H moovetruck.com
  * WHOIS\_SERVER=whois.gandi.net whois -H moovertruck.com
  * nc whois.gandi.net 43 < req.txt > gandiReply.txt  #with netcat
  * nc whois.verisign-grs.com 43 < req.txt > verisignGrsReply.txt  #with netcat

Request file with domain used [Req.txt](http://wiki.domainchecker.googlecode.com/git/req.txt).

Responses obtained from the whois servers:
  * [VerisignGrs](http://wiki.domainchecker.googlecode.com/git/verisignGrsReply.txt)
  * [Gandi](http://wiki.domainchecker.googlecode.com/git/gandiReply.txt)
