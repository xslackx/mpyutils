import machine
import platform
import network
import esp
import os
from time import ticks_ms, ticks_diff


def esp_info():
    sta_if: bool = network.WLAN(network.WLAN.IF_STA)
    ap_if: bool = network.WLAN(network.WLAN.IF_AP)
    freq: int = machine.freq()
    uid = machine.unique_id()
    osinfo = platform.platform()
    flash_size = esp.flash_size()
    user_space_start = esp.flash_user_start()
    freemem: int = esp.freemem()
    sysname = os.uname()[0]
    netname = os.uname()[1]
    release = os.uname()[2]
    addr4 = ap_if.ifconfig("addr4") if ap_if.active() else False
    addr6 = ap_if.ifconfig("addr6") if ap_if.active() else False
    station = True if sta_if.active() else False
    
    return {
        "frequency": freq,
        "uid": uid,
        "platform": osinfo,
        "flash": [
            {
                "size": flash_size,
                "start_user_space": user_space_start          
            }
        ],
        "freemem": freemem,
        "sysname": sysname,
        "release": release,
        "net": [
            {
                "name": netname,
                "interface": "On" if addr4 else "Off",
                "ap_station": "On" if station else "Off",
                "addr4": addr4 if addr4 else "",
                "addr6": addr6 if addr6 else ""
            }
        ]
    
    } 
    
def idle_counter(duration=1):
    ini = ticks_ms()
    counter = 0
    while ticks_diff(ticks_ms(), ini) < duration * 1000:
        counter += 1
    return counter

def cpu_usage(idle, duration=1):
    ini = ticks_ms()
    idle_round = 0
    while ticks_diff(ticks_ms(), ini) < duration * 1000:
        idle_round += 1
    usage = 100 - int((idle_round / idle) * 100)
    if usage < 0:
        return 0
    return usage