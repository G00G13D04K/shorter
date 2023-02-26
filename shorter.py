import os
import time
import pyshorteners
import sys

def animated(text):
	for x in text:
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(.0005)


logo = '''\u001b[32m
   _____ _                _    __     __                _      _       _    
  / ____| |              | |   \ \   / /               | |    (_)     | |   
 | (___ | |__   ___  _ __| |_   \ \_/ /__  _   _ _ __  | |     _ _ __ | | __
  \___ \| '_ \ / _ \| '__| __|   \   / _ \| | | | '__| | |    | | '_ \| |/ /
  ____) | | | | (_) | |  | |_     | | (_) | |_| | |    | |____| | | | |   < 
 |_____/|_| |_|\___/|_|   \__|    |_|\___/ \__,_|_|    |______|_|_| |_|_|\_\
                                                                            
                                                                            
'''
animated(logo)
print("\u001b[31mNOTE: TO RUN THIS TOOL YOU NEED INTERNET CONNECTION")
link = input("\u001b[37mEnter Your Link : ")

s = pyshorteners.Shortener()

provide = s.tinyurl.short(link)

print(f"\u001b[33mYour New Link : {provide}")
