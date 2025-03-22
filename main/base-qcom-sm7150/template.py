pkgname = "base-qcom-sm7150"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
depends = [
    "!base-full-firmware",  # We only want QCOM firmware files
    "bootmac",
    "firmware-linux-ath10k",
    "firmware-linux-qca",
    "firmware-linux-qcom",
    "hexagonfs-firmware-loader",
    "hexagonrpcd",
    "linux-qcom-sm7150",
    "make-dynpart-mappings",
    "msm-firmware-loader",
    "msm-modem",
    "qbootctl",
    "systemd-boot",
    "tqftpserv",
]
pkgdesc = "Chimera base package for Qualcomm SM7150"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(self.files_path / "cmdline", "usr/lib/systemd/boot")
    (self.destdir / "usr/lib/systemd/boot/relax-esp").touch()
    self.install_initramfs(self.files_path / "gpu_firmware")
    self.install_dir("usr/lib/dinit.d/boot.d")
    self.install_link(
        "usr/lib/dinit.d/boot.d/hexagonfs-firmware-loader",
        "../hexagonfs-firmware-loader",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/hexagonrpcd-adsp-sensorspd",
        "../hexagonrpcd-adsp-sensorspd",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/msm-firmware-loader",
        "../msm-firmware-loader",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/msm-modem-uim-selection",
        "../msm-modem-uim-selection",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/qbootctl",
        "../qbootctl",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/tqftpserv",
        "../tqftpserv",
    )
