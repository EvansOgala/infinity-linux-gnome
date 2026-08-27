#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "4.0")

from gi.repository import Gtk
from modules.home import create_home_page
from modules.software import create_software_page
from modules.system import create_system_page
from modules.community import create_community_page
from pathlib import Path

MARKER = Path.home() / "s.config/infinity-welcome/seen"
if MARKER.exists():
    exit()
MARKER.parent.mkdir(parents=True, exist_ok=True)
MARKER.touch()
dont_show = Gtk.CheckButton(
    label="Don't run on startup"
)

class InfinityWelcome(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.infinity.welcome")

    def do_activate(self):
        win = Gtk.ApplicationWindow(application=self)
        win.set_title("Infinity Welcome")
        win.set_default_size(1000, 650)

        root = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        logo = Gtk.Picture.new_for_filename(
            "assets/infinity2.png"
        )
        logo.set_size_request(1, 1)

        stack = Gtk.Stack()
        switcher = Gtk.StackSwitcher()
        switcher.set_stack(stack)

        stack.add_titled(create_home_page(), "home", "Home")
        stack.add_titled(create_software_page(), "software", "Software")
        stack.add_titled(create_system_page(), "system", "System")
        stack.add_titled(create_community_page(), "community", "Community")

        root.append(logo)
        root.append(switcher)
        root.append(stack)

        win.set_child(root)
        win.present()

app = InfinityWelcome()
app.run()
