#!/bin/env python3
#
# Sample for getting OS info in python
#
# Output of this sample for Windows 11
#                         os.name: nt
#               platform.system(): Windows
#              platform.release(): 10
#            platform.processer(): AMD64 Family 25 Model 97 Stepping 2, AuthenticAMD
#              platform.machine(): AMD64
#             platform.platform(): Windows-10
#       platform.python_version(): 3.11.9
# platform.python_version_tuple(): ('3', '11', '9')
#
# Output of this sample for WSL on Windows 11
#                         os.name: posix
#               platform.system(): Linux
#              platform.release(): 5.15.153.1-microsoft-standard-WSL2
#            platform.processer(): x86_64
#              platform.machine(): x86_64
#             platform.platform(): Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
#       platform.python_version(): 3.10.12
# platform.python_version_tuple(): ('3', '10', '12')
#
#
import os
import platform

print( '                platform.node():', platform.node() )
print( '                        os.name:', os.name )
print( '              platform.system():', platform.system() )
print( '             platform.release():', platform.release() )
print( '           platform.processer():', platform.processor() )
print( '             platform.machine():', platform.machine() )
print( '            platform.platform():', platform.platform(aliased=True,terse=True) )
print( '      platform.python_version():', platform.python_version() )
print( 'platform.python_version_tuple():', platform.python_version_tuple() )
