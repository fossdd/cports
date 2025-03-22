pkgname = "msm-firmware-loader"
pkgver = "1.6.0"
pkgrel = 0
pkgdesc = "Automatically load firmware from Android device partitions"
license = "MIT"
url = "https://gitlab.postmarketos.org/postmarketOS/msm-firmware-loader"
source = f"https://gitlab.postmarketos.org/postmarketOS/msm-firmware-loader/-/archive/{pkgver}/msm-firmware-loader-{pkgver}.tar.gz"
sha256 = "d818f65034ef0fe7192d639d48bdd8fc879e8b577e8f90e0fed6f94a17d67ea8"


def install(self):
    self.install_bin("msm-firmware-loader.sh", name="msm-firmware-loader")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "msm-firmware-loader")
