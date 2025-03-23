pkgname = "xdg-desktop-portal-phosh"
pkgver = "0.45.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "cargo-auditable",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libadwaita-devel",
    "gnome-desktop-devel",
    "xdg-desktop-portal-devel",
]
pkgdesc = "Backend implementation for xdg-desktop-portal using GTK/GNOME/Phosh"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/guidog/xdg-desktop-portal-phosh"
source = f"https://sources.phosh.mobi/releases/xdg-desktop-portal-phosh/xdg-desktop-portal-phosh-{pkgver}.tar.xz"
sha256 = "0e149fe95c21a6eec6185a4f473ef3f1616534bec458cafa206c451f513fd224"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="subprojects/pfs")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
