pkgname = "libssc"
pkgver = "0.2.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "protobuf-c-devel",
]
makedepends = [
    "glib-devel",
    "libqmi-devel",
    "protobuf-c-devel",
    "python-devel",
    "python-gobject",
]
pkgdesc = "Library to expose Qualcomm Sensor Core sensors"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/DylanVanAssche/libssc"
source = f"https://codeberg.org/DylanVanAssche/libssc/archive/v{pkgver}.tar.gz"
sha256 = "4d9e2ae4b0548f19ad53a56d365d72e31d2bb72b4ce7b234a2b69875bc24268f"
# tests require running on-device or starting a mock server before
options = ["!check"]

@subpackage("libssc-devel")
def _(self):
    return self.default_devel()
