# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:19:59 2020

@author: Daniel

This script pings the YahooFinancials API to pull pricing information
for stocks at when an alert condition is met. A connection to 
the Twilio API allows for an easy way to send SMS and MMS texts to any phone
number on its whitelist. This script can be run locally or can be hosted on a server.

"pip install" can be used to install "yahoofinancials" and "twilio"

"""

from yahoofinancials import YahooFinancials as yf
from twilio.rest import Client
import threading
from datetime import *
import time



class YahooTrack:
    
    def __init__(self):
        
        global account_si, alert_price, auth_token, send_phone, rec_phone, ticker, time_period, yfinancials
        
        print("Object YahooTrack has been initialized. Please input the following parameters.")
        
        alert_price = float(input("Input alert price: "))
        account_si=str(input("Insert SI:"))
        auth_token=str(input("Insert Token: "))
        send_phone= "+1" + str(input("Insert sending phone: "))
        rec_phone = "+1" + str(input("Insert receiving phone: "))
        
        ticker=[input("Insert Ticker to Track:" )]
        time_period = int(input("Input number of days program will run: "))
        time_period = datetime.now() + timedelta(days=time_period)
        
        yfinancials=yf(ticker)
        
             
        
    def Messenger(self):
        
        #writing the message to be sent using Twilio
        message_body = r'Stock Alert:   {}'.format(yfinancials.get_current_price())

        cli=Client(account_si,auth_token)
        mess=cli.messages.create(from_=send_phone, body = message_body, to=rec_phone )
        

    def YahooPython(self):
        
        while datetime.now() < time_period:
            
            current_price = yfinancials.get_current_price()
            for i in current_price.values():
                current_price = float(i)
                
            if current_price >= alert_price:
                self.Messenger()
            else:
                pass
            time.sleep(120)

if __name__ == "__main__":
    
    tracker = YahooTrack()
    tracker.YahooPython()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

