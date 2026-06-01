#platform info
import sys
def platform(): #current execution platform detection function
    if sys.platform  == "win32":
        system_os = "Windows"
        return system_os
    elif sys.platform  == "linux":
        system_os = "Linux"
        return system_os
    elif sys.platform == "darwin":
        system_os = "macOS"
        return system_os

#wahid-dl version info
channel = "Alpha" #channel[branch] = Stable[main], Beta[beta], Alpha[alpha]
number = "7.0" #number = x.x
build_number = "20260520.1" #build_number = xxxxxxxx.x
pl = "Python" #pl[programming language] = Batchfile[bat](Discard), Python[python](Current), Rust[rust]
def version_detail():
    vi = [channel, number, build_number, pl]
    return vi