pkgname = "ruby"
pkgver = "3.3.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--disable-rpath",
    "--disable-install-doc",
    "ac_cv_func_isnan=yes",
    "ac_cv_func_isinf=yes",
]
make_cmd = "gmake"
make_build_args = ["all", "capi"]
make_install_env = {"MAKE": "gmake"}
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "gmake",
    "mandoc",
    "pkgconf",
]
makedepends = [
    "libedit-devel",
    "libffi-devel",
    "libyaml-devel",
    "openssl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Ruby scripting language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Ruby OR BSD-2-Clause"
url = "https://www.ruby-lang.org/en"
source = (
    f"https://cache.ruby-lang.org/pub/ruby/{pkgver[:-2]}/ruby-{pkgver}.tar.xz"
)
sha256 = "1caaee9a5a6befef54bab67da68ace8d985e4fb59cd17ce23c28d9ab04f4ddad"
# until verified; gonna need removing arch prefix from compiler name
# tests mostly pass but there are some portability issues in the test
# suite (stat usage) + chown not working in the sandbox + locale issues
options = ["!cross", "!check"]

match self.profile().arch:
    case "aarch64" | "x86_64":
        # yjit only has backends here
        configure_args += ["--enable-yjit"]
        hostmakedepends += ["rust"]
        makedepends += ["rust-std"]
    case "ppc64":
        # just ELFv2
        configure_args += ["--with-coroutine=ppc64le"]

if self.profile().cross:
    hostmakedepends += ["ruby"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("ruby-devel")
def _devel(self):
    return self.default_devel(extra=[f"usr/lib/ruby/{pkgver[:-2]}.0/mkmf.rb"])


@subpackage("ruby-ri")
def _ri(self):
    self.depends += [self.parent]

    return ["usr/bin/ri"]
