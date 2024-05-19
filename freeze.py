# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5

from py2exe import freeze
import os
import shutil

from Common._AppVersion import APP_VERSION

if os.path.exists("dist"):
    shutil.rmtree("dist")

build_exe_option = {
    "excludes" : [],
    "compressed" : 1,
    "optimize" : 1,
    "bundle_files" : 3,
}

freeze(
    options = build_exe_option,
    console= [
        {"script" : "main.py"}
    ],
    zipfile=None,
    version_info={
        "version" : APP_VERSION,            # Major.Minor.Patch
        "product_name" : "ChronoLab",
        "copyright" : "(C) 2024 yumekasa5"
    }
)

# shutil.copytree("Settings", "dist/Settings")
# shutil.copytree("LICENSES", "dist/LICENSES")