from gi.repository import Gtk
import subprocess


def open_system_info():
    subprocess.Popen([
        "kitty",
        "--hold",
        "fastfetch"
    ])


def create_system_page():
    box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=10
    )

    title = Gtk.Label()
    title.set_markup(
        "<span size='large' weight='bold'>System Information</span>"
    )

    description = Gtk.Label(
        label="View detailed system information using Fastfetch."
    )

    sys_btn = Gtk.Button(
        label="Open System Information"
    )

    sys_btn.connect(
        "clicked",
        lambda b: open_system_info()
    )

    box.append(title)
    box.append(description)
    box.append(sys_btn)

    return box
