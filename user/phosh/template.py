pkgname = "phosh"
pkgver = "0.46_rc1"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "appstream-devel",
    "callaudiod-devel",
    "elogind-devel",
    "evince-devel",
    "evolution-data-server-devel",
    "feedbackd-devel",
    "gcr3-devel",
    "gmobile-devel",
    "gnome-bluetooth-devel",
    "gnome-desktop-devel",
    "gobject-introspection-devel",
    "libgudev-devel",
    "libhandy-devel",
    "libpulse-devel",
    "linux-pam-devel",
    "modemmanager-devel",
    "networkmanager-devel",
    "polkit-devel",
    "upower-devel",
    "wayland-protocols",
]
depends = [
    "bash",  # FIXME
    "dbus",
    "gnome-session",
    "gnome-settings-daemon",
    "phoc",
    "phosh-osk-stub",  # TODO: use virtual provider
    "xwayland",
]
checkdepends = ["xwayland-run"]
pkgdesc = "Wayland shell for GNOME on mobile devices"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Phosh/phosh"
source = f"https://sources.phosh.mobi/releases/phosh/phosh-{pkgver.replace("_", ".")}.tar.xz"
sha256 = "6690523006ef2221640256ba50202c81801208ce9efa6ce2b69fbba1959ac574"
# assertion 'GDK_IS_SEAT (seat)' failed (same as in main/libhandy)
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("phosh-devel")
def _(self):
    return self.default_devel()
