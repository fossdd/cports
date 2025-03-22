pkgname = "tqftpserv"
pkgver = "1.1_git20241121"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "qrtr-devel",
    "zstd-devel",
]
pkgdesc = "Trivial File Transfer Protocol server over AF_QIPCRTR"
license = "BSD-3-Clause"
url = "https://github.com/linux-msm/tqftpserv"
_commit = "533779cb8a1843581d5422a7f0aae1a35e6ab956"
source = f"https://github.com/linux-msm/tqftpserv/archive/{_commit}.tar.gz"
sha256 = "7062a0e27dfc6c7b63ccf044b112aad8a55539f9ce4091945a3d6f72990ee9ef"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tqftpserv")
