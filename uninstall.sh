#!/bin/bash

# Exit if something fails
set -e

rm ~/.local/share/kservices5/plasma-runner-KRunnerTelePrefix.desktop
rm ~/.local/share/dbus-1/services/org.kde.KRunnerTelePrefix.service
kquitapp5 krunner
