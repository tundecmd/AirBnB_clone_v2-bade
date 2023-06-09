#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents
"""
from fabric.api import local
import os
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['18.209.178.180']


def do_pack():
    """
    generates a .tgz archive from the contents
    """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)
        local("tar -czvf {} web_static".format(archive_path))
        if os.path.exists(archive_path):
            return archive_path
        else:
            return None
    except:
        return None
