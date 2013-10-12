# domainchecker 
Checks expiration dates of domains.

## License
This software is released under the MIT license. Please the see the license in the LICENSE.md file, 
located at the root of the project. 

## Environment
The project was built using the following:
 * Slackware 14
 * Eclipse 3.8.2
 * python 2.7.3
 * pywhois (http://code.google.com/p/pywhois/)

## Requirements
The project requires the following:
 * python 2.7.3
 * pywhois (http://code.google.com/p/pywhois/) 
 * pywhois patch (pywhoisPT_parser_py.patch) applied, mentioned on issue 52 (Portuguese domains), if not yet on the most recent release 

### Python 2.7.3 on RHEL 6.4
As mentioned in http://stackoverflow.com/questions/4149361/on-linux-suse-or-redhat-how-do-i-load-python-2-7
 * su
 * cd /tmp
 * wget http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz 
 * tar xvfz Python-2.7.3.tgz 
 * cd Python-2.7.3 
 * ./configure
 * make # build
 * make altinstall

ln -s /lib64/libz.so.1 libz.so 
cd /tmp
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz
tar xvzf setuptools-1.1.6.tar.gz
cd setuptools-1.1.6
/usr/local/bin/python2.7 setup.py build

 