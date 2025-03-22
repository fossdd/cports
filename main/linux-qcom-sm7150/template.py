pkgname = "linux-qcom-sm7150"
pkgver = "6.13.7"
pkgrel = 0
archs = ["aarch64"]
build_style = "linux-kernel"
configure_args = ["FLAVOR=sm7150", f"RELEASE={pkgrel}"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0 : pkgver.rfind('.')]}.x"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://github.com/sm7150-mainline/linux/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fedd063d199ad36aed869969dde35951c8de45d7fe0951dc6cdd05a0a8191aaf"
# no meaningful checking to be done
options = [
    "!check",
    "!debug",
    "!strip",
    "!scanrundeps",
    "!scanshlibs",
    "!lto",
    "textrels",
    "execstack",
    "foreignelf",  # vdso32
]

if self.current_target == "custom:generate-configs":
    hostmakedepends += ["base-cross", "ncurses-devel"]


@subpackage("linux-qcom-sm7150-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-qcom-sm7150-dbg", self.build_dbg)
def _(self):
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "usr/lib/modules/*/apk-dist/boot/System.map-*"]
