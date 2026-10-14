import importlib
import subprocess
import sys


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

