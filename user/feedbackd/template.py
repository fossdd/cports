pkgname = "feedbackd"
pkgver = "0.8.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "glib-devel",
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala",
]
makedepends = [
    "json-glib-devel",
    "gobject-introspection-devel",
    "gmobile-devel",
    "gsound-devel",
    "libgudev-devel",
    "umockdev-devel",
]
depends = ["dbus"]
checkdepends = ["dbus"]
pkgdesc = "Daemon to provide haptic, LED, and audio feedback"
license = "GPL-3.0-or-later"
url = "https://source.puri.sm/Librem5/feedbackd"
source = (
    f"https://sources.phosh.mobi/releases/feedbackd/feedbackd-{pkgver}.tar.xz"
)
sha256 = "20c22656a89a207b592dc5c91a61285745e39b19248993d9f823fa7a834b8d9e"
# i dont care
options = ["!check"]


def post_install(self):
    self.install_file(self.files_path / "90-feedbackd-aw8695.rules", "usr/lib/udev/rules.d")
    self.install_file(self.files_path / "90-feedbackd-pm6150.rules", "usr/lib/udev/rules.d")
    self.uninstall("usr/lib/systemd/user")


@subpackage("feedbackd-devel")
def _(self):
    return self.default_devel()
