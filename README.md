[renovate]: https://github.com/renovatebot/renovate
[changelog episode 289]: https://changelog.com/podcast/289
[dependabot source code]: https://github.com/dependabot/dependabot-core
[list of approved licences]: https://opensource.org/licenses/alphabetical

This repository helps the author understand changes to software that he uses.

It consists of Ansible roles to install JavaScript and Python packages. The
versions of these packages are pinned and updated with [renovate]. Each role
executes the installed binaries as a test.

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

For a role, `example`, the follow variables can be set to control behaviour:

- `example_binaries` is a list of the binaries that the role will link from
  `/usr/local/bin/`, defaults to the role name
- `example_versions` is a list of the binaries that the role will run with
  `--version`, defaults to `example_binaries`

# Licence

Copyright 2018 Keith Maxwell

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
