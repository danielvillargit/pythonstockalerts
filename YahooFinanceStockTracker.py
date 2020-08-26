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
from datetime import *
import time


#predefined parameters

def YahooPython():
    
    #setting time list
    b=8
    c=30
    ti=[]
    for i in range(8,16):
        time_ = r'{}:{}'.format(b,c)
        ti.append(time_)
        b+=1
    tickers=['MSFT','AAPL']

    #configure login parameters for connection to Twilio
    yfinancials=yf(tickers)
    account_si=str(input("Insert SI: "))
    auth_token=str(input("Insert Token: "))
    from_=str(input("Insert sending telephone: "))
    to = str(input("Insert receiving telephone: "))
    
    #ping Twilio authentication
    cli=Client(account_si,auth_token)
    
    #loop continuously with a 60 second loop delay and 30 second timer delay to reduce load
    time_end=datetime.now().strftime("%d")+timedelta(days =5)
    
    while datetime.now().strftime("%d") < time_end:
        timenow=datetime.now().strftime("%H:%M")
        if timenow in ti:
            mess=cli.messages.create(from_,body='Daily Stocks          '+str(yfinancials.get_current_price()),to )
            print('Message Sent at: ',stimenow)
        time.sleep(20)
        
    
    
    
    