from gi.repository import Gtk
import webbrowser

LINKS = {
    "Website":
        "https://infinity-linux-arch.github.io",
    "GitHub Issues":
        "https://github.com/EvansOgala/infinity-linux/issues",
    "SourceForge":
        "https://sourceforge.net/projects/infinity-linux/"
}

def open_link(url):
    webbrowser.open(url)

def create_community_page():
    box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=10
    )

    for title, url in LINKS.items():
        btn = Gtk.Button(label=title)
        btn.connect(
            "clicked",
            lambda b, u=url: open_link(u)
        )
        box.append(btn)

    return box
