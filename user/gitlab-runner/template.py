pkgname = "gitlab-runner"
pkgver = "18.2.1"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X gitlab.com/gitlab-org/gitlab-runner/common.VERSION={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "GitLab runner for CI/CD jobs"
license = "MIT"
url = "https://gitlab.com/gitlab-org/gitlab-runner"
source = f"{url}/-/archive/v{pkgver}/gitlab-runner-v{pkgver}.tar.gz"
sha256 = "254541563b75e6839f24c5cab1d2ed6ce0b9a7264b891e5ae1e7024eb60b15d5"
# need to be run in a git repo
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
