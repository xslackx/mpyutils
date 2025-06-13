try:
    machine.RTC().datetime()[0]
    is_loaded = True
except:
    is_loaded = False

def ntp_is_on():    
    if is_loaded:
        if machine.RTC().datetime()[0] == 2000:
            try:
                from socket import getaddrinfo
                from ntptime import settime
                getaddrinfo('www.google.com', 443)[0][-1]
                settime()
                return True
            except:
                return False

ntp_is_on()