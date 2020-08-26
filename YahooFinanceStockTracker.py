# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:19:59 2020

@author: Daniel

This script pings the YahooFinancials API to pull pricing information
for stocks at predefined times Monday through Friday. A connection to 
the Twilio API allows for an easy way to send SMS and MMS texts to any phone
number on its whitelist. This script can be run locally or hosted on a server.

"""

from yahoofinancials import YahooFinancials as yf
from twilio.rest import Client
import threading
from datetime import *
import time

#predefined parameters
z=0
r=range(1,6)
ti=['8:20','8:30','11:30','13:00','15:00','12:44']
tickers=['MSFT','AAPL']

def YahooPython():
    
    #configure login parameters for connection to Twilio
    yfinancials=yf(tickers)
    account_si=str(input("Insert SI: "))
    auth_token=str(input("Insert Token: "))
    from_=str(input("Insert sending telephone: "))
    to = str(input("Insert receiving telephone: "))
    #ping Twilio and Yahoo API to send the latest pricing info for stocks in variable tickers
    cli=Client(account_si,auth_token)
    mess=cli.messages.create(from_,body='Daily Stocks          '+str(yfinancials.get_current_price()),to )
    pass


#loop continuously with a 60 second loop delay and 30 second timer delay to reduce load
while z<=500000:
    timenow=datetime.now()
    stimenow=timenow.strftime("%H:%M")
    if timenow.isoweekday() in r and stimenow in ti:
        t=threading.Timer(30.0,YahooPython)
        t.start()
        pass
    time.sleep(60)
    print('Message Sent at:',stimenow)
    z+=1
    
    
    