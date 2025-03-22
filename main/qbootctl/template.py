pkgname = "qbootctl"
pkgver = "0.2.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
pkgdesc = "Tool for interacting with Android A/B slots"
license = "GPL-3.0-or-later"
url = "https://github.com/linux-msm/qbootctl"
source = f"https://github.com/linux-msm/qbootctl/archive/{pkgver}.tar.gz"
sha256 = "8039519c6fdc9d8409c06b512507377b79a2127ab67c8d0cc650abf4c4ef16fb"


def post_install(self):
    self.install_service(self.files_path / "qbootctl")
