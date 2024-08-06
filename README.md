# pyarchon

**pyarchon** is a Python interface to Archon controllers using the camera-interface server. Originally adapted from CESL (**C**amera **E**xternal **S**cripting **L**anguage), it was initially developed for the Zwicky Transient Facility (ZTF). This library retains many of ZTF's unique features to ensure compatibility with existing scripts.

## Usage
To use pyarchon, start Python (or iPython) and import the interface as shown below:

```python
import pyarchon.interface as cam
```
Note: The alias cam is used here for demonstration purposes and can be replaced with any name of your choice.

## Example
Here is a brief example demonstrating how to use the pyarchon interface:

```python
import pyarchon.interface as cam

# Display help information for the module
help(cam)

# Example output:
# Help on module pyarchon.interface in pyarchon:
#
# NAME
#    pyarchon.interface
#
# FILE
#    /path/to/pyarchon/interface.py
#
# FUNCTIONS
#    close()
#        Close connection to camera

```

## Contributing
We welcome contributions to the pyarchon project. If you would like to contribute, please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements
pyarchon was adapted from CESL, which was initially developed for ZTF. We would like to thank the ZTF team for their contributions.
