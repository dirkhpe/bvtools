#!/home/bv/bvenv/bin/python
"""
This script will set the database name for backup.
"""
import datetime
import logging
import os
import platform
from lib import my_env
from lib.my_env import run_script

cfg = my_env.init_env("bellavista", __file__)
dbname = "{host}_{date}.db".format(host=platform.node(), date=datetime.datetime.now().strftime("%Y%m%d"))
os.environ["LOCALDB"] = dbname
(fp, filename) = os.path.split(__file__)
for script in ["rebuild_sqlite.py", "murcs_Get.py"]:
    logging.info("Run script: {s}".format(s=script))
    run_script(fp, script)
