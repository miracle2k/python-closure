import sys
import subprocess

try:
    # use importlib here instead
    import atexit
    import importlib.resources
    from contextlib import ExitStack

    def get_jar_filename():
        """Return the full path to the Closure Compiler Java archive."""
        return get_importlib_resources_jar()

except ImportError:
    from pkg_resources import resource_filename

    def get_jar_filename():
        """Return the full path to the Closure Compiler Java archive."""
        return get_pkg_resources_jar()


def get_importlib_resources_jar():
    file_manager = ExitStack()
    atexit.register(file_manager.close)
    ref = importlib.resources.files(__name__) / "closure.jar"
    return file_manager.enter_context(importlib.resources.as_file(ref))


def get_pkg_resources_jar():
    return resource_filename(__name__, "closure.jar")


def run(*args):
    cmd_args = ["java", "-jar", get_jar_filename()] + list(args)
    return subprocess.call(cmd_args)


def main():
    exit_code = run(*sys.argv[1:])
    sys.exit(exit_code)
