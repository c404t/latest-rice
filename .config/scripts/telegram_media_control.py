#!/usr/bin/env python

import subprocess

def send_telegram_command(command):
    subprocess.run(["dbus-send", "--print-reply", "--dest=org.mpris.MediaPlayer2.TelegramDesktop",
                    "/org/mpris/MediaPlayer2", "org.mpris.MediaPlayer2.Player." + command])

# Available commands:
# PlayPause, Next, Previous, Stop, Play, Pause, Seek
# AdjustVolume (volume level), SetPosition (time in microseconds)

# Example: send_telegram_command("PlayPause")


