#!/usr/bin/python3
"""A Plasma runner."""
import dbus.service
import data
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

DBusGMainLoop(set_as_default=True)

OBJPATH = "/KRunnerTelePrefix"
IFACE = "org.kde.krunner1"
SERVICE = "org.kde.KRunnerTelePrefix"


class Runner(dbus.service.Object):
    def __init__(self):
        dbus.service.Object.__init__(
            self,
            dbus.service.BusName(SERVICE, dbus.SessionBus()),
            OBJPATH,
        )

    @dbus.service.method(IFACE, in_signature="s", out_signature="a(sssida{sv})")
    def Match(self, query: str):
        if query.startswith("+"):
            matched = []
            for country in data.prefix_data:
                if country['code'] == query:
                    matched.append(
                        (
                            country['name'],
                            country['code'],
                            data.get_flag_path(country['iso']),
                            100,
                            1.0,
                            {"subtext": country['name']},
                        )
                    )
            return matched
        return []

    @dbus.service.method(IFACE, out_signature="a(sss)")
    def Actions(self):
        # id, name, icon
        return [("copy", "Copy place name", "edit-copy")]

    @dbus.service.method(IFACE, in_signature="ss")
    def Run(self, data: str, action_id: str):
        klipper_iface = dbus.Interface(
            dbus.SessionBus().get_object("org.kde.klipper", "/klipper"),
            "org.kde.klipper.klipper",
        )
        klipper_iface.setClipboardContents(data)

runner = Runner()
loop = GLib.MainLoop()
loop.run()
