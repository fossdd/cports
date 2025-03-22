pkgname = "qrtr"
pkgver = "1.1_git20250301"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["linux-headers"]
pkgdesc = "Userspace reference for net/qrtr in the Linux kernel"
license = "BSD-3-Clause"
url = "https://github.com/linux-msm/qrtr"
_commit = "5923eea97377f4a3ed9121b358fd919e3659db7b"
source = f"https://github.com/linux-msm/qrtr/archive/{_commit}.tar.gz"
sha256 = "dde3f26b9745acb2eebfbae1466aac3283b6adbc558e07ee1f3033b16544bfb4"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("qrtr-devel")
def _(self):
    return self.default_devel()
