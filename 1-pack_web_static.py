#!/usr/bin/python3
"""script that generates a .tgz archive"""

import time
from fabric.api import local


def do_pack():
    """create .tgz file"""
    tt = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(tt))
        return ("versions/web_static_{}.tgz".format(tt))
    except:
        return None
