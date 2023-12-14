#!/usr/bin/python3
"""
The scripts create a new archive from the
web_static directory

"""
import os
from datetime import datetime
from fabric.api import local
from fabric.api import run, put, env

env.hosts = ["3.94.185.80", "54.173.97.239"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_pack():
    """
    creating an archive file
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    current_time = datetime.now()
    formatted_date = current_time.strftime("%Y%m%d%H%M%S")

    file_name = "versions/web_static_{}.tgz".format(formatted_date)
    print("Packing web_static to {}".format(file_name))
    result = local("tar -cvzf {} web_static".format(file_name))
    size = os.stat(file_name).st_size
    print("web_static packed: {} -> {}Bytes".format(file_name, size))
    if result.succeeded:
        return file_name
    else:
        return None


def do_deploy(archive_path):
    """
    deploying the archile file
    """

    if not os.path.exists(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        file_name_no_ext = os.path.splitext(file_name)[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}/".format(
            path, file_name_no_ext))
        run("sudo tar -xzf /tmp/{} -C {}{}/".format(
            file_name, path, file_name_no_ext))
        run("sudo rm -f /tmp/{}".format(file_name))
        run("sudo mv {0}{1}/web_static/* {0}{1}/".format(
            path, file_name_no_ext))
        run("sudo rm -rf {}{}/web_static".format(path, file_name_no_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(
            path, file_name_no_ext))
        run('echo "New version deployed!"')
        return True
    except BaseException:
        return False


def deploy():
    """ full deployment archile file"""
    archive_file = do_pack()
    if archive_file is None:
        return False
    return do_deploy(archive_file)
