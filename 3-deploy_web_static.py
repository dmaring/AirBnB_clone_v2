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


def do_pack():
    """
    Function that archives a version of a static site into tarball
    """

    if not os.path.exists('versions'):
        os.makedirs('versions')
    curr_time = datetime.now().strftime('%Y%m%d%H%M%S')
    name_time = "versions/web_static_{}.tgz".format(curr_time)
    command = "tar -czvf {} -C web_static .".format(name_time)
    result = local(command)
    if result.failed:
        return(None)
    else:
        return(name_time)


def do_deploy(archive_path):
    """
    Function that that distributes an archive to web servers
    """

    if not os.path.exists(archive_path):
        return False
    base_name = os.path.basename(archive_path)
    name = base_name.split(".")[0]
    with settings(abort_exception=Exception):
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
        except Exception:
            return False
    return True


def deploy():
    """
    A function that packs and deploys a webstatic site from a tarball
    """

    arch_name = do_pack()
    return(do_deploy(arch_name))
