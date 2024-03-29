"""Interact with Backlogs on the command line."""

import os
import re
from typing import Optional, Pattern

import click

import backlog


class PatternParamType(click.ParamType):
    """Validate regular expressions pattern parameters."""

    name = "pattern"

    def convert(
        self,
        value: str,
        param: Optional[click.Parameter],
        ctx: Optional[click.Context],
    ) -> Pattern[str]:
        """Convert a pattern string to a Pattern."""
        try:
            return re.compile(value)
        except re.error as exc:
            # return does nothing here but make pylint happy:
            # https://github.com/PyCQA/pylint/issues/3299
            return self.fail(str(exc), param, ctx)


PATTERN = PatternParamType()


@click.group(invoke_without_command=True)
@click.option(
    "--path",
    type=click.Path(),
    help="Specify the path to use for the backlog file.",
    default=os.path.join(click.get_app_dir("backlog"), "entries.json"),
)
@click.version_option(version=backlog.__version__)
@click.pass_context
def main(ctx: click.Context, path: str) -> None:
    """Manage a Backlog."""
    ctx.obj = {
        "backlog": (
            backlog.Backlog.load(path) if os.path.isfile(path) else backlog.Backlog()
        ),
        "path": path,
    }
    if ctx.invoked_subcommand is None:
        ctx.invoke(show)


@main.command()
@click.option(
    "--note",
    type=str,
    help="Add a note.",
    default="",
)
@click.option(
    "--priority",
    type=int,
    help="Specify a priority level.",
    default=0,
)
@click.argument("title", type=str)
@click.pass_context
def add(ctx: click.Context, title: str, note: str, priority: int) -> None:
    """Add an entry to the backlog."""
    ctx.obj["backlog"].entries.append(
        backlog.Backlog.Entry(
            note=note,
            priority=priority,
            title=title,
        ),
    )
    ctx.obj["backlog"].save(ctx.obj["path"])


@main.command()
@click.pass_context
def random(ctx: click.Context) -> None:
    """Select a random entry from the backlog."""
    entry = ctx.obj["backlog"].random()
    if entry:
        click.echo(str(entry))


@main.command()
@click.option(
    "--ask/--dont-ask",
    help="Prompt before deleting.",
    default=True,
)
@click.argument("pattern", type=PATTERN)
@click.pass_context
def remove(ctx: click.Context, pattern: Pattern[str], ask: bool) -> None:
    """Remove entries from the backlog."""
    entries = list(ctx.obj["backlog"].search(pattern))
    click.echo(str(backlog.Backlog(entries=entries)))
    if entries:
        if not ask or click.confirm(f"delete {len(entries)} entries?"):
            backlog.Backlog(
                entries=list(ctx.obj["backlog"].search(pattern, invert=True)),
            ).save(ctx.obj["path"])


@main.command()
@click.option(
    "--pattern",
    type=PATTERN,
    help="Specify a search pattern for entry titles.",
    default=".*",
)
@click.pass_context
def show(ctx: click.Context, pattern: Pattern[str]) -> None:
    """Show entries in the backlog."""
    entries = list(ctx.obj["backlog"].search(pattern))
    click.echo(f"total {len(entries)}")
    if entries:
        click.echo(str(backlog.Backlog(entries=entries)))
