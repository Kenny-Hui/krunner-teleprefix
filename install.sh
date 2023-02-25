#!/bin/bash

# Exit if something fails
set -e

mkdir -p ~/.local/share/kservices5/
mkdir -p ~/.local/share/dbus-1/services/

cp plasma-runner-KRunnerTelePrefix.desktop ~/.local/share/kservices5/
sed "s|%{PROJECTDIR}/KRunnerTelePrefix.py|${PWD}/KRunnerTelePrefix.py|" "org.kde.KRunnerTelePrefix.service" > ~/.local/share/dbus-1/services/org.kde.KRunnerTelePrefix.service

kquitapp5 krunner
