pkgname = "gmobile"
pkgver = "0.2.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "glib-devel",
    "meson",
    "pkgconf",
    "gobject-introspection",
]
makedepends = [
    "json-glib-devel",
    "gobject-introspection-devel",
]
pkgdesc = "Functions useful in mobile related, glib based projects"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Phosh/gmobile"
source = f"https://sources.phosh.mobi/releases/gmobile/gmobile-{pkgver}.tar.xz"
sha256 = "add5d642bcdaf51f830e4b547481c6b031ecad1ebecfdd76e49fddbcd58c9f7e"


@subpackage("gmobile-devel")
def _(self):
    return self.default_devel()
