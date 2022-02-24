from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in manager_workspace/__init__.py
from manager_workspace import __version__ as version

setup(
	name="manager_workspace",
	version=version,
	description="manager workspace",
	author="samwel",
	author_email="samwel05kamau@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
