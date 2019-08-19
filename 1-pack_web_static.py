#!/usr/bin/python3
"""
Python fabric module to archive a static website into .tgz file
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function that archives a version of a static site into tarball
    """

    if not os.path.exists('versions'):
        os.makedirs('versions')
    curr_time = datetime.now().strftime('%Y%m%d%H%M%S')
    name_time = "versions/web_static_{}.tgz".format(curr_time)
    command = "tar -czvf {} web_static".format(name_time)
    result = local(command)
    if result.failed:
        return(None)
    else:
        return(name_time)
