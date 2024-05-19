# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
from py2exe import freeze
import os
import shutil

from Common._AppVersion import APP_VERSION

if os.path.exists("ChronoLab-" + APP_VERSION + "-win32"):
    shutil.rmtree("ChronoLab-" + APP_VERSION + "-win32")
if os.path.exists("ChronoLab-" + APP_VERSION + "-win32.zip"):
    os.remove("ChronoLab-" + APP_VERSION + "-win32.zip")

build_exe_option = {
    "excludes" : [],
    "compressed" : 1,
    "optimize" : 1,
    "bundle_files" : 3,
}

freeze(
    options = build_exe_option,
    windows = [
        {
            "script" : "ChronoLab.py",
            "icon_resources" : [(1, "data/icon/ChronoLab.ico")]
        }
    ],
    zipfile=None,
    version_info={
        "version" : APP_VERSION,            # Major.Minor.Patch
        "product_name" : "ChronoLab",
        "copyright" : "(C) 2024 yumekasa5"
    }
)

shutil.copytree("data", "dist/data")
# shutil.copytree("LICENSES", "dist/LICENSES")
os.rename("dist", "ChronoLab-" + APP_VERSION + "-win32")
shutil.make_archive("ChronoLab-" + APP_VERSION + "-win32", "zip", "ChronoLab-" + APP_VERSION + "-win32")