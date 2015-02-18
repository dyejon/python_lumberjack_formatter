import os

from setuptools import setup, find_packages, findall

def get_version():
	with open(os.path.join(thisdir, 'VERSION'), 'r') as fh:
		return fh.readline().strip()

def get_requires():
	requires = []
	with open(os.path.join(thisdir, 'requirements.txt'), 'r') as fh:
		for line in fh.readlines():
			requires += [ line.strip() ]
	return requires

SCRIPTS = findall('bin')

thisdir = os.path.dirname(os.path.realpath(__file__))

VERSION = get_version()

ALL_PACKAGES = find_packages()

ALL_INSTALL_REQUIRES = get_requires()

setup(
	name='lumberjack_formatter',
	version=VERSION,
	description='Python logging framework JSON formatter for use with the lumberjack transport (logstash-forwarder)',
	author='IBM',
	author_email='jdye@us.ibm.com',
	packages=ALL_PACKAGES,
	provides=ALL_PACKAGES,
	scripts=SCRIPTS,
	include_package_data=True,
	setup_requires=(
		'setuptools>=11.0,<13.0'
	),
	install_requires=ALL_INSTALL_REQUIRES,
)

