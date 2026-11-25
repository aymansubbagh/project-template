"""Print the versions of the core scientific stack. Run: python scripts/check_env.py"""

import importlib
import platform
import sys

PACKAGES = ["numpy", "pandas", "scipy", "matplotlib", "seaborn", "jupyterlab", "pytest", "Bio"]

print(f"Python {sys.version.split()[0]} on {platform.system()} {platform.machine()}")
missing = []
for name in PACKAGES:
    try:
        module = importlib.import_module(name)
        print(f"  ok   {name:<12} {getattr(module, '__version__', '?')}")
    except ImportError:
        missing.append(name)
        print(f"  --   {name:<12} not installed")

if missing:
    print(f"\nMissing: {', '.join(missing)}  (Bio = biopython, optional until Project 1)")
else:
    print("\nAll core packages found.")
