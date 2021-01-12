# pyarchon

This is a Python interface to Archon using the camera-interface server. It was adapted from CESL (**C**amera **E**xternal **S**cripting **L**anguage) which was initially developed for ZTF. As such, this carries over a lot of ZTF's peculiarities so that old scripts can still be used.

## Python Requirements

pyarchon requires Python 2.7 which is no longer supported but 2.7 compatibility can be achieved with Anaconda. Install Anaconda on your system using the appropriate method (e.g. `sudo apt-get anaconda`). Then create an environment for a 2.7 python package. For example:

```
$ sudo apt-get anaconda
$ sudo sh /tmp/Anaconda3-2020.11-Linux-x86_64.sh
$ conda install python=2.7
$ sudo /opt/anaconda3/bin/conda create –name py2 python=2.7
```

That last command creates an environment named “py2”. You can now activate a Python 2.7 environment using the following command:

```
(base) $ conda activate py2
(py2) $
```

You are now in a Python 2.7 environment suitable for running pyarchon.

### Using pyarchon

From a py2 environment run Python (or iPython) then import the interface as follows:

```
(py2) $ python
>>> from pyarchon import interface as cam
```

Note that `cam` can be anything and is just used as an example here:

```
>>> help(cam)

Help on module pyarchon.interface in pyarchon:

NAME
    pyarchon.interface

FILE
    /home/user/Software/pyarchon/interface.py

FUNCTIONS
    close()
        close connection to camera
    
```
etc.

