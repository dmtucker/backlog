# Development

Please [open an issue](https://help.github.com/articles/creating-an-issue/) to discuss any concerns or ideas for the project.

## Environment

The development environment is built around [`git`](https://git-scm.com/doc) and [`pipenv`](https://docs.pipenv.org/):
``` sh
git clone https://github.com/dmtucker/backlog
cd backlog/
pipenv install --dev
```

### Tests

[`tox`](https://tox.readthedocs.io/) and [`pytest`](https://docs.pytest.org/) are used for validation:
``` sh
pipenv run tox -- --pdb
```

## Submitting Changes

1. All change proposals are submitted by [creating a pull request (PR)](https://help.github.com/articles/creating-a-pull-request/).
   - PRs and [branch protection](https://help.github.com/articles/about-protected-branches/) are used to enforce acceptance criteria.

2. All PRs are associated with a [milestone](https://help.github.com/articles/about-milestones/).
   - Milestones serve as a change log for the project.

3. Any PR that directly changes any release artifact gets 1 of 3 [labels](https://help.github.com/articles/applying-labels-to-issues-and-pull-requests/): `Major`, `Minor`, `Patch`.
   - This helps with release versioning.

### Making Releases

1. Releases are versioned according to [Semantic Versioning](http://semver.org/).
   - https://semver.org/#why-use-semantic-versioning

2. All releases are tagged.
   - This permanently associates a version with a commit and triggers automatic deployment.

3. Every release closes a milestone.
   - Milestones serve as release notes for the project.
