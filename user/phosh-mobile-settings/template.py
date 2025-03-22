pkgname = "phosh-mobile-settings"
pkgver = "0.45.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
    "desktop-file-utils",
]
makedepends = [
    "glib-devel",
    "libadwaita-devel",
    "gmobile-devel",
    "gnome-desktop-devel",
    "gsound-devel",
    "phosh-devel",
    "wayland-protocols",
    "lm-sensors-devel",
]
pkgdesc = "Phosh Mobile Settings"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/guidog/phosh-mobile-settings"
source = f"https://sources.phosh.mobi/releases/phosh-mobile-settings/phosh-mobile-settings-{pkgver}.tar.xz"
sha256 = "535989d705f8705b5666769f91235fff7dad7d17a931f354446793375ec5a51c"
