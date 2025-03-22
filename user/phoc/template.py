pkgname = "phoc"
pkgver = "0.45.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "xwayland",
]
makedepends = [
    "glib-devel",
    "gnome-desktop-devel",
    "libinput-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "gmobile-devel",
    "wlroots0.18-devel",
]
# mutter's schemas are used
depends = [
    "dbus",
    "mutter",
    "gsettings-desktop-schemas",
]
pkgdesc = "Phone compositor for the Phosh shell"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Phosh/phoc"
source = f"https://sources.phosh.mobi/releases/phoc/phoc-{pkgver}.tar.xz"
sha256 = "6015e674c45b0b14c26476179e2b0308060b2cee426c1818d81f67466173ff95"
# needs fullblown EGL
options = ["!check"]
