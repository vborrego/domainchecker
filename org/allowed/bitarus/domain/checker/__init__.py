'''
Created on Oct 8, 2013

Check tcp data to smtp por 25 on pp0 interface:  
tcpdump -A -vv -i ppp0 port 25

@author Vitor Borrego
'''
import whois
import time
import datetime
import plistlib
from os.path import expanduser
import smtplib
import syslog
import os

class Logger(object):
    '''
    Logs messages to syslog, usually /var/log/messages
    '''
    @staticmethod
    def log(msg):
        syslog.syslog("[domainChecker] %s" % (msg))
        
class SendMail(object):
    '''
    Sends an email message
    '''
    def __init__(self, config, subject, message):
        s = smtplib.SMTP()
        header = 'From:%s\nTo:%s\nSubject:%s\n\n' % (config.getMailFrom(), config.getMailTo(), subject)
        try:
            (code, response) = s.connect(config.getServer() , config.getPort())  # expects 220
            if code == 220: 
                (code, response) = s.ehlo('domainChecker')  # expects 250
            else:
                raise Exception('Connect failed') 
            if code == 250: 
                (code, response) = s.starttls()  # expects 220
            else:
                raise Exception('Ehlo failed')
            if code == 220: 
                (code, response) = s.login(config.getUser(), config.getPassword())  # expects 235
            else:
                raise Exception('StartTLS failed')                
            if code == 235: 
                Logger.log("Before sendmail:%s" % (message))
                (code, response) = s.sendmail(config.getMailFrom(), config.getMailTo(), "%s%s" % (header, message))
            else:
                raise Exception('Login failed')            
        except Exception as e:
            Logger.log("SendMail exception: %s" % (e)) 
        s.quit()
        
class Domain(object):
    '''
    Stores info about domain expiration
    '''
    def __init__(self, domain, status, expirationDate, text):
        self.exception = ''
        try:  # may give an error if no expiration date is found in whois registry
            #print expirationDate
            currTime = time.time()
            self.domain = domain
            self.status = status        
            self.text = text
            self.expirationDate = expirationDate                
            self.expireDays = expirationDate - datetime.datetime.fromtimestamp(currTime)
        except Exception as ex:
            self.expireDays = 0
            self.expirationDate = None
            self.exception = str(ex)
    def __repr__(self):
        if len(self.exception) == 0:
            return "Domain:%s\nStatus:%s\nExpiration date: %s\nExpires in: %s\n\n" % (self.domain, self.status, self.expirationDate, self.expireDays)
        else:
            return "Domain:%s\nStatus:%s\nExpiration date: %s\nText: %s\nException: %s\n\n" % (self.domain, self.status, self.expirationDate, self.text, self.exception)

class Config(object):
    def __init__(self):
        homeDir = expanduser("~")  # get current user home dir
        configFilePath = os.path.join(homeDir, '.domainChecker.plist')
        config = plistlib.readPlist(configFilePath)  # load domains to check
        self.domains = config['domains']
        self.server = config['mailSettings']['server']
        self.port = config['mailSettings']['port']
        self.user = config['mailSettings']['user']
        self.password = config['mailSettings']['pass']
        self.mailfrom = config['mailSettings']['from']
        self.mailto = config['mailSettings']['to']
    def getDomains(self): 
        return self.domains
    def getServer(self): 
        return self.server
    def getPort(self): 
        return self.port
    def getUser(self): 
        return self.user
    def getPassword(self): 
        return self.password
    def getMailFrom(self): 
        return self.mailfrom
    def getMailTo(self): 
        return self.mailto
    @staticmethod
    def createDummyConfig():
        x = {}
        x['domains'] = ['aaa', 'bbb', 'ccc']
        x['mailSettings'] = {
                           'server':'mail.example.net',
                           'port':25,
                           'user':'test',
                           'pass':'test',
                           'from':'test@example.net',
                           'to':'tset@example.net' 
        }
        plistlib.writePlist(x, 'dummyConfig.plist')
        
class Checker(object):    
    def __init__(self):
        config = Config()
        domainStatus = []
        for domain in config.getDomains():
            whoisRes = whois.whois(domain)
            # a list of expire dates may be created with multiple types in it (datetime.datetime or string)
            expireDate = None
            if type(whoisRes.expiration_date) is list:
                for item in whoisRes.expiration_date:
                    if type(item) is datetime.datetime:
                        expireDate = item   
            else:
                expireDate = whoisRes.expiration_date
                
            domainStatus.append(Domain(whoisRes.domain_name, whoisRes.status , expireDate, str(whoisRes)))
            
        # send the results to the define email
        msg = ''
        for status in domainStatus:
            msg = "%s%s\n" % (msg , status)    
        Logger.log(msg)
        SendMail(config, 'Domain check', msg)
        
