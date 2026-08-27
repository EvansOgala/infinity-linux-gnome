from gi.repository import Gtk

def create_home_page():
    box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=10
    )

    title = Gtk.Label()
    title.set_markup(
        "<span size='xx-large' weight='bold'>"
        "Welcome to Infinity Linux"
        "</span>"
    )

    desc = Gtk.Label(
        label="Fast • Customizable • Community Driven"
    )

    box.append(title)
    box.append(desc)

    return box
