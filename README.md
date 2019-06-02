[renovate]: https://github.com/renovatebot/renovate
[changelog episode 289]: https://changelog.com/podcast/289
[dependabot source code]: https://github.com/dependabot/dependabot-core
[list of approved licences]: https://opensource.org/licenses/alphabetical

This directory helps the author understand changes to software that he uses.

It uses Ansible to install JavaScript and Python packages. The versions of these
packages are pinned and updated with [renovate]. Each installed binary is run
with `--version` to test the installation or equivalent, where possible.

Each package uses a separate `main.yaml` to account for variations between
packages for example multiple binaries, the absence of support for `--version`
or a non-zero return code.

Packages are installed with `npm ci` or `pip`.

# Quick start

## Use a package

```sh
ansible-playbook -i, packages/jsonlint/main.yaml
```

## Setup a new Node.js package

Using `jsonlint` as an example, create the playbook and then try to run it. This
will fail because it doesn't install the binaries without a `package-lock.json`
so it cannot run the binaries. Instead create a `package-lock.json` with
`npm install`.

```sh
ansible-playbook -i, create-npm.yaml -e create_package=jsonlint
ansible-playbook -i, packages/jsonlint/main.yaml
cd /opt/jsonlint
npm install
```

Move the resulting `package-lock.json` into this repository and use the package
again. Add a line to `site.yaml`.

## Setup a new Python package

Using `autopep8` as an example:

```
mkdir packages/autopep8 &&
cd packages/autopep8 &&
cp ../black/main.yaml . &&
echo autopep8 >> requirements.in &&
pip-compile &&
cd ../.. &&
ansible-playbook -i, packages/autopep8/main.yaml
```

## Checks

A pre-commit hook checks that `site.yaml` is up to date:

```
git config core.hooksPath .githooks
```

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

When importing `npm.yaml` the follow variables can be set to control behaviour:

- `npm_name` is the name of the folder containing `package.json` and
  `package-lock.json`
- `npm_binaries` is a list of the binaries to link from `/usr/local/bin/`,
  defaults to the role name
- `npm_versions` is a list of the binaries that the role will run with
  `--version`, defaults to `npm_binaries`

# Licence

© 2018, 2019 Keith Maxwell

All code is subject to the terms of the Mozilla Public License, v. 2.0. You can
obtain a copy of the MPL at <http://mozilla.org/MPL/2.0/>.

<!--

SPDX-License-Identifier: MPL-2.0
SPDX-Copyright: 2019 Keith Maxwell

-->
