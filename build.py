"""Builds the documentation locally."""

from subprocess import run
from pathlib import Path

here = Path(__file__).parent
run(['mkdocs', 'build', '--site-dir', 'HTML'], cwd=here)
