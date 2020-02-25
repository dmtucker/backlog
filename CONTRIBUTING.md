# Contributing Guidelines

[GitHub](https://github.com/) hosts the project.

https://guides.github.com/introduction/flow/

## Development

Develop changes by [cloning the repository](https://help.github.com/articles/cloning-a-repository).

[![GitHub repo size](https://img.shields.io/github/repo-size/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog)

### Environment

Use [`tox`](https://tox.readthedocs.io/) to build and manage test environments.

``` sh
tox --devenv venv                # Create a development environment.
tox $tox_opts -- $pytest_opts    # Build and test the project.
```

The primary test environment uses [`pytest`](https://pytest.readthedocs.io/) to test the project.

## Integration

Propose changes by [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

[![GitHub last commit](https://img.shields.io/github/last-commit/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog/commits)

### Automation

[GitHub Actions](https://github.com/features/actions) builds and tests all pull requests.

[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/dmtucker/backlog/Test/master)](https://github.com/dmtucker/backlog/actions)

## Publication

Publish changes by [creating a release](https://help.github.com/articles/creating-releases).

[![GitHub release](https://img.shields.io/github/release/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog/releases)

### Distribution

Release are distributed on [PyPI](https://pypi.org/).

[![PyPI - Status](https://img.shields.io/pypi/status/backlog.svg)](https://pypi.org/project/backlog)
