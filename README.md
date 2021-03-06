[renovate]: https://github.com/renovatebot/renovate
[changelog episode 289]: https://changelog.com/podcast/289
[dependabot source code]: https://github.com/dependabot/dependabot-core
[list of approved licences]: https://opensource.org/licenses/alphabetical

[![reuse compliant](https://reuse.software/badge/reuse-compliant.svg)](https://reuse.software/)

This repository helps the author understand changes to software that he uses.

It uses Ansible to install JavaScript and Python packages. The versions of these
packages and their dependencies are pinned and updated with [renovate]. Where
possible each installed binary is run with `--version`, or equivalent, to test
the installation.

Each package uses a separate `main.yaml` to account for variations between
packages for example multiple binaries, the absence of support for `--version`
or a non-zero return code.

Packages are installed with `npm ci` or `pip`. Installation is tested in GitLab
CI on Alpine Linux edge.

On Alpine Linux the repository does not compile C code. Instead the playbooks
pull in system packages.

# Quick start

## Use a package

    ansible-playbook -c local -i localhost, \
      -e apk_version= packages/fava/main.yaml

## Use all packages

    python3 site.yaml.py | tee site.yaml \
    && ansible-playbook -c local -i localhost, -e apk_version= site.yaml

## Setup a new Node.js package

Using `jsonlint` as an example, create the playbook and then try to run it. This
will fail because it doesn't install the binaries without a `package-lock.json`
so it cannot run the binaries. Instead create a `package-lock.json` with
`npm install`.

    ansible-playbook -i, create-npm.yaml -e create_package=lint-staged \
    && ansible-playbook -c local -i localhost, packages/lint-staged/main.yaml \
    && cd /opt/lint-staged \
    && npm install

Move the resulting `package-lock.json` into this repository and use the package
again.

## Setup a new Python package

The main task is to create a suitable `requirements.txt`. Using `autopep8` as an
example:

    package=pre-commit \
    && mkdir packages/$package \
    && cd packages/$package \
    && cp ../isort/main.yaml . \
    && echo $package > requirements.in \
    && pip-compile \
    && cd ../.. \
    && ansible-playbook -c local -i localhost, packages/$package/main.yaml

For `pip-compile` on Alpine Linux, depending on the package, compilers may be
required:

    podman run -ti --rm --volume $PWD:/srv:z --workdir /srv alpine:edge

    apk upgrade \
    && apk add alpine-sdk py3-pip python3-dev libffi-dev libxslt-dev \
    && python3 -m pip install pip-tools

    pip-compile

`pre_tasks` that install Alpine Linux packages with the `apk` Ansible module do
not have `become: yes` set because when:

1. running on CI, `ansible-playbook` will be run as root
2. running locally the pre-task will fail unless the packages are already
   installed.

# Choice of renovate

Rhys Arkins, the author of renovate spoke on the [Changelog Episode 289].
Renovate is licensed with the GNU Affero General Public License version 3
(AGPL-3.0).

An online discussion in the local Python community endorsed
<https://dependabot.com/>. The main [dependabot source code] is licensed under
the License Zero Prosperity Public License. This licence does not appear on the
Open Source Initiative's [list of approved licences].

Both dependabot and renovate appear to offer similar functionality, but renovate
is open source.

# Variables

In the two roles, `npm` and `pip` the following variables are used:

- `???_name` is the name of the folder containing `main.yaml` and the lock files
- `???_binaries` is a list of the binaries to link from `/usr/local/bin/`,
  defaults to the role name
- `???_versions` is a list of the binaries that the role will run with
  `--version`, defaults to `npm_binaries`

# Changes

## Forthcoming

- Only builds a package if its files change, needs
  https://gitlab.com/gitlab-org/gitlab/-/issues/34272 to be merged
- Support for Fedora

## Version 2

- Installs happen in parallel in GitLab CI; run time went from approximately 7
  minutes to approximately 1 minute
- Pin package versions on Alpine Linux
- Support only for Alpine Linux

## Version 1

- Initial prototype
- Support for Alpine, Debian and Ubuntu

# Licence

© 2018, 2019, 2020 Keith Maxwell

All code is subject to the terms of the Mozilla Public License, v. 2.0. You can
obtain a copy of the MPL at <http://mozilla.org/MPL/2.0/>.

<!--

SPDX-License-Identifier: MPL-2.0
SPDX-Copyright: 2019 Keith Maxwell

-->
