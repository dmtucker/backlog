# Contributing Guidelines

[GitHub](https://github.com/) hosts the project.

[![GitHub repo size](https://img.shields.io/github/repo-size/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog)

## Development

Discuss changes by [creating an issue](https://help.github.com/articles/creating-an-issue).

[![GitHub issues](https://img.shields.io/github/issues/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog/issues)

### Version Control

Use [`git`](https://git-scm.com/doc) to retrieve and manage the project source code.

``` sh
git clone https://github.com/dmtucker/backlog.git
```

### Test Environment

Use [`tox`](https://tox.readthedocs.io/) to deploy and run the project source code.

``` sh
tox                        # Build and test the project
tox -e py39                # in a specific environment
tox -e py39 -- --pdb       # with extra options,
                           # or
tox -e py39 --devenv venv  # create a development environment
venv/bin/backlog --help    # and call scripts/binaries in it.
```

## Merges

Propose changes by [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

[![GitHub pull requests](https://img.shields.io/github/issues-pr/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog/pulls)

- [Branch protection](https://help.github.com/articles/about-protected-branches/) enforces acceptance criteria.
- [Milestones](https://help.github.com/en/articles/about-milestones) serve as a changelog for the project.
- [Labels](https://help.github.com/en/articles/about-labels) track the intent of each change.

## Releases

Distribute changes by [creating a release](https://help.github.com/en/articles/creating-releases).

[![GitHub release](https://img.shields.io/github/release/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog/releases)

1. [Change the version.](http://semver.org/)
2. [Create a tag.](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
3. [Release the tag.](https://help.github.com/en/articles/creating-releases)

### Package Repository

[PyPI](http://pypi.org/) distributes releases.

[![PyPI](https://img.shields.io/pypi/v/backlog.svg)](https://pypi.org/project/backlog)
