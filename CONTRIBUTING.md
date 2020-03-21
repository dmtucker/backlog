# Contributing Guidelines

Service       | Vendor | Status
------------- | ------ | ------
Hosting       | [GitHub Hosting](https://github.com/features#hosting) | [![GitHub repo size](https://img.shields.io/github/repo-size/dmtucker/backlog.svg)](https://github.com/dmtucker/backlog)
Tracking      | [GitHub Project Management](https://github.com/features/project-management/) | [![GitHub issues](https://img.shields.io/github/issues/dmtucker/backlog)](https://github.com/dmtucker/backlog/issues)
Review        | [GitHub Code Review](https://github.com/features/code-review/) | [![GitHub pull requests](https://img.shields.io/github/issues-pr/dmtucker/backlog)](https://github.com/dmtucker/backlog/pulls)
Automation    | [GitHub Actions](https://github.com/features/actions) | [![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/dmtucker/backlog/Test/master)](https://github.com/dmtucker/backlog/actions?query=branch%3Amaster)
Distribution  | [PyPI](https://pypi.org/) | [![PyPI - Downloads](https://img.shields.io/pypi/dm/backlog)](https://pypi.org/project/backlog)
Documentation | [GitHub Pages](https://pages.github.com) | [![GitHub deployments](https://img.shields.io/github/deployments/dmtucker/backlog/github-pages)](https://dmtucker.github.io/backlog)

## Devlopment

Contributing to the project requires [understanding the GitHub flow](https://guides.github.com/introduction/flow/).

### Environment

Use [`tox`](https://tox.readthedocs.io/) to manage development environments:

``` sh
tox --devenv venv
```

#### Testing

``` sh
tox -e static
tox -e py -- $pytest_opts
```

#### Documentation

``` sh
tox -e docs -- $sphinx_outputdir
```

#### Publication

``` sh
tox -e publish -- $twine_optargs
```
