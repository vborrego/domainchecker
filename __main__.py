#!/usr/bin/python
'''
Created on Oct 8, 2013

Checks when a domains expires and how much time until it expires.

Requires pywhois: http://code.google.com/p/pywhois/

whois *NIX command line, whois -H sapo.pt

Domains to check on <home user dir>/.domainChecker.plist

### Notes ####
Location of lib: /usr/lib/python2.7/site-packages/python_whois-0.2-py2.7.egg

### Patch generation ###
Patch to whois/parser.py required (Portugal)
chmod 666 whois/parser.py
diff /tmp/pywhois/whois/parser.py /usr/lib/python2.7/site-packages/python_whois-0.2-py2.7.egg/whois/parser.py > pywhoisPT_parser_py.patch

Patch submited to http://code.google.com/p/pywhois/issues/entry, issue 52

Project home: http://code.google.com/p/domainchecker/

@author Vitor Borrego
'''

from org.allowed.bitarus.domain.checker import Checker

if __name__ == '__main__':
    checker = Checker()