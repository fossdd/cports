pkgname = "rmtfs"
_commit = "f24570816b3234f0885c2897fb9c094848df2835"
pkgver = "1.1_git20250213"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
make_use_env = True
makedepends = ["udev-devel", "qrtr-devel", "linux-headers", "udev-devel"]
pkgdesc = "Qualcomm Remote Filesystem Service Implementation"
license = "BSD-3-Clause"
url = "https://github.com/linux-msm/rmtfs"
source = f"https://github.com/linux-msm/rmtfs/archive/{_commit}.tar.gz"
sha256 = "2553425ef5a556e9ebaefe499138b397b20a83054ebdd63a1217256c88aa0751"
# no tests
options = ["!check"]


def post_install(self):
    self.install_file(self.files_path / "udev.rules", "usr/lib/udev/rules.d", name="65-rmtfs.rules")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "rmtfs")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.uninstall("usr/lib/systemd/system")
