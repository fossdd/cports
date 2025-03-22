pkgname = "hexagonfs-firmware-loader"
pkgver = "1.0.0"
pkgrel = 0
depends = ["msm-firmware-loader"]
pkgdesc = "Prepare the HexagonFS directory from msm-firmware-loader mounts"
license = "MIT"
url = "https://gitlab.postmarketos.org/postmarketOS/hexagonfs-firmware-loader"
source = f"https://gitlab.postmarketos.org/postmarketOS/hexagonfs-firmware-loader/-/archive/{pkgver}/hexagonfs-firmware-loader-{pkgver}.tar.gz"
sha256 = "9b48da8e914d38baa193c15599c1d839e3a57efdb56e4bc8efbd1a5578ecbea6"
file_modes = {
    "+usr/share/qcom": ("root", "root", 0o755, True),
}


def install(self):
    self.install_bin(
        "hexagonfs-firmware-loader.sh", name="hexagonfs-firmware-loader"
    )
    self.install_files("socinfo", "usr/share", name="hexagonfs-firmware-loader")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "hexagonfs-firmware-loader")
