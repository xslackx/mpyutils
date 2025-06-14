try:
    machine.RTC().datetime()[0]
    is_loaded = True
except:
    is_loaded = False

def change_ntp(host: tuple):
    try:
        from socket import getaddrinfo
        from ntptime import settime
        getaddrinfo('www.google.com', 443)[0][-1]
        if host:
            settime(timezone=host[0], server=host[1])
        else:
            settime()
        return True
    except:
        return False

def ntp_is_on(first_try: bool):
    if first_try: change_ntp(())
        
    if is_loaded:
        if machine.RTC().datetime()[0] == 2000:
            change_ntp(())
    else:
        import machine
        change_ntp(())