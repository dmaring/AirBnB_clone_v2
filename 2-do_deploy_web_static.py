#!/usr/bin/python3
"""
Python fabric that manages archives for web servers
"""
import os
from fabric.api import *
from datetime import datetime


env.hosts = ['35.231.178.39', '34.73.236.42']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Function that that distributes an archive to web servers
    """

    if not os.path.exists(archive_path):
        return(False)
    base_name=os.path.basename(archive_path)
    name=base_name.split(".")[0]
    with settings(abort_exception = FabricException):
        try:
            put(archive_path, "/tmp")
            sudo("mkdir -p /data/web_static/releases/{}".format(name))
            sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                 .format(base_name, name))
            sudo("rm /tmp/{}".format(base_name))
            sudo("rm /data/web_static/current")
            sudo("ln -fs /data/web_static/releases/{} /data/web_static/current"
                 .format(name))
            sudo("service nginx restart")
        except FabricException:
            return(False)
    return(True)
