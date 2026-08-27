from gi.repository import Gtk
import subprocess

def install_package(pkg):
    subprocess.Popen([
        "kitty",
        "--hold",
        "sudo",
        "pacman",
        "-S",
        "--needed",
        pkg
    ])

CATEGORIES = {
    "Internet": [
        ("Firefox", "firefox"),
        ("Chromium", "chromium"),
    ],

    "Gaming": [
        ("Steam", "steam"),
        ("Heroic", "heroic-games-launcher"),
        ("Lutris", "lutris"),
    ],

    "Multimedia": [
        ("VLC", "vlc"),
        ("OBS Studio", "obs-studio"),
    ],

    "Development": [
        ("VS Code", "code"),
        ("Git", "git"),
    ],

    "Virtualization": [
        ("Virt Manager", "virt-manager"),
        ("VirtualBox", "virtualbox"),
    ],

    "Infinity Editions": [
    ("GNOME Edition", "infinity-gnome"),
    ("KDE Edition", "infinity-kde"),
    ("Hyprland Edition", "infinity-hypr"),
]
}

def create_software_page():
    scroll = Gtk.ScrolledWindow()

    box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=8
    )

    for category, apps in CATEGORIES.items():

        expander = Gtk.Expander(
            label=category
        )

        category_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=5
        )

        for name, pkg in apps:

            row = Gtk.Box(
                orientation=Gtk.Orientation.HORIZONTAL,
                spacing=10
            )

            label = Gtk.Label(label=name)

            button = Gtk.Button(
                label="Install"
            )

            button.connect(
                "clicked",
                lambda b, p=pkg:
                install_package(p)
            )

            row.append(label)
            row.append(button)

            category_box.append(row)

        expander.set_child(category_box)

        box.append(expander)

    scroll.set_child(box)

    return scroll
