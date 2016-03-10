#!/usr/bin/env python

from socket import * 

print ('====================================')
if __name__ == '__main__':
    target = raw_input('Enter host to scan: ')
    targetIP = gethostbyname(target)
    print '------------------------------------'
    print 'Starting scan on host ', targetIP

    for i in range(20, 1025):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print 'Port %d: OPEN' % (i,)
        s.close()

