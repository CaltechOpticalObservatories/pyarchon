"""
This file contains host information for the archon.interface package.

All dictionaries below should contain the same number of items.

camhost should contain IP addresses of the hosts on which camerad is running.

camport should contain the port numbers for each server.
TODO: should this be the blocking or non-blocking port?

camname is an arbitrary name for the camera.

camsocket is the socket for each server connection.
"""

# dictionary for the camera host IP addresses
#
camhost = {1: "127.0.0.1"}
# camhost = {1: "192.168.1.3",
#            2: "192.168.1.4",
#            3: "192.168.1.5",
#            4: "192.168.1.6"}

# dictionary for the camera host ports
# 0 is port for guided
# 1-4 are ports for vicd
#
camport = {1: 3031}
# camport = {1: 62018,
#            2: 62018,
#            3: 62018,
#            4: 62018}

# dictionary for human-readable camera names
#
camname = {1: "localhost"}
# camname = {1: "camera1",
#            2: "camera2",
#            3: "camera3",
#            4: "camera4"}

# dictionary for camera sockets
#
camsocket = {1: ""}
# camsocket = {1: '',
#              2: '',
#              3: '',
#              4: ''}
