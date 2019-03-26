#!/usr/ash
source bvenv/bin/activate
python set_dbname.py
python rebuild_sqlite.py
python load_murcs/murcs_Get.py