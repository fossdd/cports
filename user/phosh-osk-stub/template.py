pkgname = "phosh-osk-stub"
pkgver = "0.45.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gnome-desktop-devel",
    "wayland-devel",
    "wayland-protocols",
    "gmobile-devel",
    "feedbackd-devel",
    "libhandy-devel",
    "elogind-devel",
    "hunspell-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "Phosh OSK"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/guidog/phosh-osk-stub"
source = f"https://sources.phosh.mobi/releases/phosh-osk-stub/phosh-osk-stub-{pkgver}.tar.xz"
sha256 = "5b68ad0bfbc6b62bf841d9279b9875bc047e4a1dcf69535b1fbba421953f59c3"
# assertion 'GDK_IS_SEAT (seat)' failed (same as in main/libhandy)
options = ["!check"]
