pkgname = "hexagonrpcd"
pkgver = "0.3.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
pkgdesc = "Qualcomm HexagonFS daemon"
license = "GPL-3.0-or-later"
url = "https://github.com/linux-msm/hexagonrpc"
source = f"https://github.com/linux-msm/hexagonrpc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ff0b04153a29699463bb64195366d6fecc580473be75e7f2c695f1b1ce1bc806"


def post_install(self):
    self.install_file(self.files_path / "10-fastrpc.rules", "usr/lib/udev/rules.d")
    self.install_service(self.files_path / "hexagonrpcd-adsp-rootpd")
    self.install_service(self.files_path / "hexagonrpcd-adsp-sensorspd")
    self.install_service(self.files_path / "hexagonrpcd-sdsp")
    self.install_sysusers(self.files_path / "sysusers.conf")
