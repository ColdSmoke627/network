#!/usr/bin/env python

#created by Caleb Meeson
#follow me on instagram: @fawkespickshop
#check out the website I admin: http://ninjacache.com

import os

ans=True
while ans:

    print
    print("Main Menu")
    print '===================================='
    print("1. Scan The Network")
    print("2. Scan An IP Address")
    print("3. Look Up A MAC Address")
    print("4. Clear The Terminal")
    print("5. Exit")
    print '===================================='
    print 

    ans=raw_input("What would you like to do? Enter your selection: ")
    if ans=="1":
      print
      os.system("sudo python scan.py")
    elif ans=="2":
      print
      os.system("sudo python port-scanner.py")
    elif ans=="3":
      print
      os.system("sudo python mac-lookup.py")
    elif ans=="4":
      print
      os.system('cls' if os.name == 'nt' else 'clear')
    elif ans=="5":
      print
      print("Peace Out Girl Scout!") 
      print
      ans = None
    else:
       print("Not Valid Choice Try again")

