"""
This file contains host information for the archon.interface package.
"""

# dictionary for the camera host IP addresses
#
camhost   = {}
__camhost = { 1:"127.0.0.1" }

# dictionary for the camera host ports
# 0 is port for guided
# 1-4 are ports for vicd
#
camport   = {}
__camport = { 1:3051 }

# dictionary for human-readable camera names
#
camname   = {}
__camname = { 1:"localhost" }
__emanmac = {v: k for k, v in __camname.items()}

# dictionary for camera sockets
#
camsocket   = {}
__camsocket = { 1:'' }

