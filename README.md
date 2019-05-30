[renovate]: https://github.com/renovatebot/renovate
[changelog episode 289]: https://changelog.com/podcast/289
[dependabot source code]: https://github.com/dependabot/dependabot-core
[list of approved licences]: https://opensource.org/licenses/alphabetical

This directory helps the author understand changes to software that he uses.

It uses Ansible to install JavaScript packages. The versions of these packages
are pinned and updated with [renovate]. Each installed binary is run with
`--version` to test the installation.

Each package uses a separate `main.yaml` to account for variations between
packages for example multiple binaries or the absence of support for
`--version`.

Packages are installed with `npm ci`.

# Quick start

## Use a package

```sh
ansible-console -i, localhost
```

```
setup
import_tasks prettier/main.yaml
```

## Setup a new package

Using `jsonlint` as an example.

```sh
ansible-playbook -i, create.yaml -e create_package=jsonlint
```

Then try to use the package. Using the package will fail with a message about
`package-lock.json`. Create a `package-lock.json` manually:

```sh
cd /opt/jsonlint
npm install
```

Copy the resulting `package-lock.json` and use the package again.

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

Copyright 2018, 2019 Keith Maxwell

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
