import sys
import subprocess
from pkg_resources import resource_filename


def get_jar_filename():
    """Return the full path to the Closure Compiler Java archive."""
    return resource_filename(__name__, "closure.jar")


def run(*args):
    cmd_args = ["java", "-jar", get_jar_filename()] + list(args)
    return subprocess.call(cmd_args)


def main():
    exit_code = run(*sys.argv[1:])
    sys.exit(exit_code)
