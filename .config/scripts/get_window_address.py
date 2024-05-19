#!/usr/bin/env python

import subprocess

# Get the window title of the focused window
title = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"]).decode("utf-8")

# Extract the address from the window title (you may need to adjust this based on the format of your window titles)
address = title.split(" - ")[-1]

print(address)

