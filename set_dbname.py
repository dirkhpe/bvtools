"""
This script will set the database name for backup.
"""
import datetime
import os
import platform

dbname = "{host}_{date}".format(host=platform.node(), date=datetime.datetime.now().strftime("%Y%m%d"))
os.environ["LOCALDB"] = dbname
