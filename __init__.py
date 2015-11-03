################################################################################
#
# Copyright 2015 Crown copyright (c)
# Land Information New Zealand and the New Zealand Government.
# All rights reserved
#
# This program is released under the terms of the 3 clause BSD license. See the 
# LICENSE file for more information.
#
################################################################################

from Plugin import Plugin

#debugging
try:
    import sys
    sys.path.append('/opt/eclipse/plugins/org.python.pydev_4.4.0.201510052309/pysrc')
    from pydevd import settrace
    settrace()
except:
    pass

def name():
    return Plugin.LongName

def description():
    return Plugin.Description

def version():
    return Plugin.Version

def qgisMinimumVersion():
    return Plugin.QgisMinimumVersion

def authorName():
    return Plugin.Author

def classFactory(iface):
    return Plugin(iface)

def icon():
    return 'loadaddress.png'


