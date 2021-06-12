pkgname = "bzip2"
version = "1.0.8"
revision = 1
bootstrap = True
short_desc = "Freely available, patent free, high-quality data compressor"
maintainer = "Orphaned <orphan@voidlinux.org>"
license = "bzip2-1.0.6"
homepage = "https://sourceware.org/bzip2/"
changelog = "https://sourceware.org/bzip2/CHANGES"
distfiles = [f"https://sourceware.org/pub/bzip2/bzip2-{version}.tar.gz"]
checksum = ["ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269"]

def init_build(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.build([
        "-f", "Makefile-libbz2_so",
        "CFLAGS=" + " ".join(self.CFLAGS + self.LDFLAGS)
    ])
    self.make.invoke(["bzip2recover", "libbz2.a"], [
        "CFLAGS=" + " ".join(self.CFLAGS),
        "LDFLAGS=" + " ".join(self.LDFLAGS)
    ])

def do_check(self):
    self.make.invoke("check")

def do_install(self):
    import os
    os.rename(self.abs_wrksrc / "bzip2-shared", self.abs_wrksrc / "bzip2")

    self.install_bin("bzip2")
    self.install_bin("bzip2recover")

    self.install_link("bzip2", "usr/bin/bunzip2")
    self.install_link("bzip2", "usr/bin/bzcat")

    self.install_bin("bzdiff", "bzmore")

    self.install_lib("libbz2.so." + version)
    self.install_link("libbz2.so." + version, "usr/lib/libbz2.so")
    self.install_link("libbz2.so." + version, "usr/lib/libbz2.so.1")
    self.install_link("libbz2.so." + version, "usr/lib/libbz2.so.1.0")

    self.install_file(self.abs_wrksrc / "libbz2.a", "usr/lib")
    self.install_file(self.abs_wrksrc / "bzlib.h", "usr/include")

    self.install_man("bzip2.1")
    self.install_link("bzip2.1", "usr/share/man/man1/bunzip2.1")
    self.install_link("bzip2.1", "usr/share/man/man1/bzcat.1")
    self.install_link("bzip2.1", "usr/share/man/man1/bzip2recover.1")

@subpackage("bzip2-devel")
def _devel(self):
    self.depends = [f"{pkgname}>={version}_{revision}"]
    self.short_desc = short_desc + " - development files"

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")

    return install
