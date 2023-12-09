#!/usr/bin/env python3
"""
The scripts create a new archive from the
web_static directory

"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """
    creating an archive file
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    current_time = datetime.now()
    formatted_date = current_time.strftime("%Y%m%d%H%M%S")

    filename = "versions/web_static_{}.tgz".format(formatted_date)
    print("Packing web_static to {}".format(filename))
    result = local("tar -cvzf {} web_static".format(filename))
    size = os.stat(filename).st_size
    print("web_static packed: {} -> {}Bytes".format(filename, size))
    if result.succeeded:
        return filename
    else:
        return None
