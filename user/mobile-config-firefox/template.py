pkgname = "mobile-config-firefox"
pkgver = "4.4.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["FIREFOX_DIR=/usr/lib/firefox"]
pkgdesc = "Firefox tweaks for mobile and privacy"
license = "GPL-3.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/mobile-config-firefox"
source = f"{url}/-/archive/4.4.0/mobile-config-firefox-4.4.0.tar.gz"
sha256 = "39f4857ebb66ba9b4181e6d32265b3fc187861af601b868652923e895a295275"
# no tests
options = ["!check"]
