pkgname = "xdg-user-dirs-gtk"
pkgver = "0.11"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["pkgconf", "meson", "gettext", "xdg-user-dirs"]
makedepends = ["gtk+3-devel", "xdg-user-dirs"]
depends = ["xdg-user-dirs"]
pkgdesc = "Gtk companion to xdg-user-dirs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/xdg-user-dirs-gtk"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "534bd563d3c0e3f8dcbf3578cb8ab0e49d3ba41c966d477c8af9438364121e7d"
