from pathlib import Path
from typing import List

import typer


def _append_echo(file: Path, text: str) -> None:
    warning_message = (
        f"{text} appended to {file}."
    )
    styled_warning = typer.style(warning_message, typer.colors.YELLOW, bold=True)
    typer.echo(styled_warning)


def _create_file_echo(file: Path) -> None:
    message = f"Warning: created the {file}."
    styled_message = typer.style(message, fg=typer.colors.YELLOW, bold=True)
    typer.echo(styled_message)


def _create_dir_echo(directory: Path) -> None:
    message = f"Warning: created the {directory} directory."
    styled_message = typer.style(message, fg=typer.colors.YELLOW, bold=True)
    typer.echo(styled_message)


def _create_vmsshconfig_echo(
    hostnames: List[str],
) -> None:
    """
    Echos the newly created config files
    """

    typer.echo("")
    message = "✨ Creating ~/.ssh/config.d/ files"
    typer.echo(message)
    for hostname in hostnames:
        hostname_output = typer.style(hostname, fg=typer.colors.YELLOW, bold=True)
        hostname_message = "✅ " + hostname_output
        typer.echo(hostname_message)
    message_end = "SSH config updated! 🚀 ✨!"
    typer.echo(message_end)
    typer.echo("")

    message = "Thank you for using vm-ssh-config."

    thank_you_message = typer.style(message, typer.colors.BRIGHT_BLACK)
    typer.echo(thank_you_message)
    typer.echo("")