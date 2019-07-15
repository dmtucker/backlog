# Contributing Guidelines

[GitHub](https://github.com/) hosts the project.

## Development

Develop changes by [cloning the repository](https://help.github.com/articles/cloning-a-repository).

[![GitHub repo size](https://img.shields.io/github/repo-size/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog)

### Version Control

Use [`git`](https://git-scm.com/doc) to manage the repository.

``` sh
git add -p
git status
git commit -S
git log
```

### Test Environment

Use [`tox`](https://tox.readthedocs.io/) to build and test the code.

``` sh
tox                        # Build and test the project
tox -e py39                # in a specific environment
tox -e py39 -- --pdb       # with extra options,
                           # or
tox -e py39 --devenv venv  # create a development environment
venv/bin/backlog --help    # and call scripts/binaries in it.
```

## Continuous Integration

Propose changes by [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

[![GitHub last commit](https://img.shields.io/github/last-commit/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog/commits)

### Build Automation

[GitHub Actions](https://github.com/features/actions) creates and tests builds before uploading them to [PyPI](https://pypi.org/).

[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/dmtucker/backlog/Test/master)](https://github.com/dmtucker/backlog/actions)
[![PyPI - Status](https://img.shields.io/pypi/status/backlog.svg)](https://pypi.org/project/backlog)

## Releases

Publish changes by [creating a release](https://help.github.com/articles/creating-releases).

[![GitHub release](https://img.shields.io/github/release/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog/releases)

1. [Change the version.](https://semver.org/)
2. [Create a tag.](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
3. [Release the tag.](https://help.github.com/articles/about-releases)
