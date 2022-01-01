"""Renders the documentation locally."""

from subprocess import run

process = run(['mkdocs', 'build', '--site-dir', 'HTML'])
