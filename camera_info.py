# --------------------------------------------------------------------------
# @file:     camera_info.py
# @brief:    CameraInfo class for the ztf package, see CIN #680
# @author:   David Hale <dhale@caltech.edu>
# @date:     2017-02-15
# @modified: 2017-02-22 DH allow basename=""
# @modified: 2017-03-22 DH  implement setting noisebits for FITS compression
#
# The CameraInfo class stores and retrieves current settings for
# the camera module of the ztf package.
# --------------------------------------------------------------------------
class CameraInfo(object):

    """
    This is the CameraInfo class, which is used to store
    and retrieve current settings, in particular the
    camera mode, image type, basename, exposure time,
    and compression type.
    
    This is for internal use only by the camera module
    of the ztf package. The user should never need to
    look in here.
    """

    # codes for types
    #
    TYPE = { "OBJECT"       :0,
             "BIAS"         :1,
             "DARK"         :2,
             "DOME_FLAT"    :3,
             "TWILIGHT_FLAT":4,
             "FOCUS"        :5,
             "POINTING"     :6,
             "TEST"         :7,
             "ILLUMINATION" :8,
             "FRINGE"       :9,
             "SEEING"       :10,
             "OTHER"        :11 }
    TYPE_NAME = {v: k for k, v in TYPE.iteritems()}

    # codes for FITS compression types
    #
    COMPRESSION = { "NONE":0,
                    "RICE":1,
                    "GZIP":2,
                    "PLIO":3 }
    COMPRESSION_NAME = {v: k for k, v in COMPRESSION.iteritems()}

    def __init__(self, mode="DEFAULT", \
                       imtype=TYPE["TEST"],  \
                       basename="",          \
                       compression=COMPRESSION["NONE"], \
                       noisebits=4,          \
                       iterations=1,         \
                       exptime=0             ):
        """
        initialize the class
        """
        self.imtype      = imtype
        self.mode        = mode
        self.exptime     = exptime
        self.iterations  = iterations
        self.compression = compression
        self.noisebits   = noisebits
        self.basename    = basename

    def get_basename(self):
        """
        Return the base name.
        """
        return self.basename

    def get_exptime(self):
        """
        Return the exposure time.
        """
        return self.exptime

    def get_iterations(self):
        """
        Return the iterations
        """
        return self.iterations

    def get_type(self):
        """
        Return the image type as a string.
        """
        return self.TYPE_NAME[self.imtype]

    def get_mode(self):
        """
        Return the camera mode as a string.
        """
        return self.mode

    def get_compression_type(self):
        """
        Return the compression type as a string.
        """
        return self.COMPRESSION_NAME[self.compression]

    def get_compression_noisebits(self):
        """
        Return the compression noisebits as a string.
        """
        return self.noisebits

    def set_type(self, imtype):
        """
        Set the image type.
        """
        if imtype in self.TYPE.keys():
            self.imtype = self.TYPE[imtype]
            return 0
        else:
            print "  valid CameraInfo types:",
            print self.TYPE.keys()
            return 1
        
    def set_compression(self, type, noisebits):
        """
        Set the compression type.
        """
        if type in self.COMPRESSION.keys():
            self.compression = self.COMPRESSION[type]
            self.noisebits   = noisebits
            return 0
        else:
            print "  valid CameraInfo compression types:",
            print self.COMPRESSION.keys()
            return 1

    def set_mode(self, mode_in):
        """
        Set the camera mode.
        Allow any mode here. The server will do the error checking.
        """
        self.mode = mode_in
        return 0

    def set_exptime(self, exptime):
        """
        Set the exposure time.
        """
        if exptime >= 0:
            self.exptime = exptime
            return 0
        else:
            print "  exptime must be >= 0"
            return 1
            
    def set_iterations(self, iterations):
        """
        Set the iterations
        """
        if iterations > 0:
            self.iterations = iterations
            return 0
        else:
            print "  iterations must be > 0"
            return 1
            
    def set_basename(self, basename):
        """
        Set the basename.
        """
        self.basename = basename
        return 0

