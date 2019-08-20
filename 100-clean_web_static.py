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


@runs_once
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


def do_clean(number=0):
    """
    A function that deletes out-of-date archives
    """

    _number = int(number)
    if _number == 0 or number == 1:
        _number = 2
    else:
        _number = _number + 1

    # local("ls -t versions | tail -n +{} | xargs rm --".format(_number))
    cwd = os.getcwd()
    os.chdir("".join([cwd, "/versions"]))
    with settings(abort_exception=Exception):
        try:
            local("ls -t | grep web_static | tail -n +{} | xargs rm"
                  .format(_number))
        except Exception:
            pass
    os.chdir(cwd)
    with cd('/data/web_static/releases'):
        sudo("ls -t | grep web_static_ | tail -n +{} | xargs rm -R"
             .format(_number))

    # time_list = []
    # # for each file in the versions directory
    # _list = os.listdir('versions')
    # # strip the time info and put into a list
    # for item in _list:
    #     base_name = os.path.basename(item)
    #     file_name = base_name.split(".")[0]
    #     name = file_name.split("_")[2]
    #     time_list.append(name)
    # # sort the list
    # time_list.sort(reverse=True)
    # # slice from the number needed to the end
    # if number == 0 or number == 1:
    #     time_list = time_list[1:]
    # else:
    #     time_list = time_list[int(number):]
    # del_list = []
    # for time in time_list:
    #     file_name = "web_static_{}.tgz".format(time)
    #     del_list.append(file_name)
    # for _file in del_list:
    #     local("rm versions/{}".format(_file))
    # for _file in del_list:
    #     sudo("rm /data/web_static/releases/{}".format(_file))
