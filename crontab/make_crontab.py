#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:08:04 2018

@author: crantu
"""

from os import path


def make_crontab():
    rsb_dirname = path.dirname(path.abspath(__file__)).rsplit("/", 1)[0]
    shutdown_button_crontab =\
        (r"@reboot python3 "
         r"{rsb_dir}/src/shutdown_button.py"
         r" >> {rsb_dir}/log/"
         r"shutdown_button_$(date +\%Y\%m\%d_\%H\%M\%S).log 2>&1")
    dir_name = path.dirname(path.abspath(__file__))

    shutdown_button_crontab =\
        shutdown_button_crontab.format(rsb_dir=rsb_dirname)

    with open(path.join(dir_name, "shutdown_button.crontab"), "w") as crontab:
        crontab.write(shutdown_button_crontab)
        crontab.write("\n")
    print(shutdown_button_crontab)


if __name__ == "__main__":
    make_crontab()
