# Contributing Guidelines

[GitHub](https://github.com/) hosts the project.

## Development

Please [open an issue](https://help.github.com/articles/creating-an-issue/) to discuss any concerns or ideas for the project.

### Version Control

Use [`git`](https://git-scm.com/doc) to retrieve and manage the project source code:
``` sh
git clone https://github.com/dmtucker/backlog.git
```

### Test Environment

Use [`tox`](https://tox.readthedocs.io/) to deploy and run the project source code:
``` sh
tox                     # Build and Test the entire project.
tox -e dev              # Run Python in an environment with the project deployed.
tox -e dev -- "$SHELL"  # Run $SHELL in an environment with the project deployed.
```

## Merges

1. All change proposals are submitted by [creating a pull request](https://help.github.com/articles/creating-a-pull-request/) (PR).
   - [Branch protection](https://help.github.com/articles/about-protected-branches/) is used to enforce acceptance criteria.

2. All PRs are [associated with a milestone](https://help.github.com/articles/associating-milestones-with-issues-and-pull-requests/).
   - Milestones serve as a change log for the project.

3. Any PR that directly changes any release artifact gets 1 of 3 [labels](https://help.github.com/articles/applying-labels-to-issues-and-pull-requests/): `major`, `minor`, `patch`.
   - This helps with release versioning.

### Continuous Integration

[Travis CI](https://travis-ci.org/) ensures the build never breaks and the tests always pass.

[![Build Status](https://travis-ci.org/dmtucker/backlog.svg?branch=master)](https://travis-ci.org/dmtucker/backlog)

It also deploys releases to the package repository automatically (see below).

## Releases

1. Releases are versioned according to [Semantic Versioning](http://semver.org/).
   - https://semver.org/#why-use-semantic-versioning

2. All releases are [tagged](https://git-scm.com/book/en/v2/Git-Basics-Tagging).
   - This permanently associates a version with a commit.

3. Every release closes a [milestone](https://help.github.com/articles/about-milestones/).
   - This permanently associates a version with a milestone.

### Package Repository

[PyPI](http://pypi.org/) serves releases publically.

[![Build Status](https://img.shields.io/pypi/v/backlog.svg)](https://pypi.org/project/backlog)
