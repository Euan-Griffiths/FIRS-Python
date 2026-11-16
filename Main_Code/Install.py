import importlib
import subprocess
import sys
import sysconfig
from pathlib import Path


_venv_instructions_shown = False


def is_externally_managed_python():
    if sys.prefix != sys.base_prefix:
        return False
    marker = Path(sysconfig.get_path("stdlib")) / "EXTERNALLY-MANAGED"
    return marker.is_file()


def show_venv_instructions():
    global _venv_instructions_shown
    if _venv_instructions_shown:
        return

    _venv_instructions_shown = True
    print(
        "This Ubuntu Python environment is externally managed, so pip cannot "
        "install packages into it.\n"
        "From the project directory, create and use a virtual environment:\n"
        "  sudo apt install python3-venv python3-tk\n"
        "  python3 -m venv .venv\n"
        "  source .venv/bin/activate\n"
        "  python -m pip install astropy matplotlib numpy Pillow\n"
        "Then run the application with the environment active:\n"
        "  python Main_Code/run.py"
    )


def check_and_install(import_names, package_name=None):
    try:
        for import_name in import_names:
            importlib.import_module(import_name)
        return True
    except ImportError:
        if package_name is None:
            print(
                "tkinter is missing. Install a Python distribution or OS package "
                "that includes tkinter."
            )
            return False

        if is_externally_managed_python():
            show_venv_instructions()
            return False

        print(f"{package_name} is missing; installing it now.")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package_name]
            )
            for import_name in import_names:
                importlib.import_module(import_name)
            return True
        except (ImportError, OSError, subprocess.CalledProcessError) as error:
            print(f"Could not install {package_name}: {error}")
            return False


astropyinstall = check_and_install(
    ("astropy.io", "astropy.visualization"), "astropy"
)
matplotlibinstall = check_and_install(("matplotlib",), "matplotlib")
numpyinstall = check_and_install(("numpy",), "numpy")
tkinterinstall = check_and_install(("tkinter",))
PILinstall = check_and_install(("PIL",), "Pillow")

if all(
    (astropyinstall, matplotlibinstall, numpyinstall, tkinterinstall, PILinstall)
):
    print("Program Completed Successfully")
else:
    print("Some dependencies are missing; see the messages above.")