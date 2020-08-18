#!/usr/bin/python3
"""distributes an archive to
your web servers, using the
function do_deploy"""

import os.path
from fabric.api import env
from fabric.api import run
from fabric.api import put

env.hosts = ["104.196.204.4", "35.231.4.186"]


def do_deploy(archive_path):
    """create a .tgz file"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    filename = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(filename)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(filename)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, filename)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/"
           .format(filename, filename)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(filename)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(filename)).failed is True:
        return False
    return True
