import pathlib
from setuptools import setup, find_packages
# the directory containing this file
HERE = pathlib.Path(__file__).parent
# readme file
README = (HERE / "README.md").read_text()

setup(name="lemon-tools",
      version="1.0.0",
      # if you want a cleaner versioning use the things below
      # setup_requires=['setuptools_scm'],
      # intall_requires=['setuptools_scm'],
      # use_scm_version={'write_to': 'lemon-tools/version.txt'},
      description="Module buider with CI included",
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/japandotorg/lemon-tools",
      author="Lemon Rose", author_email="yash.kul69@gmail.com",
      packages=find_packages(),
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=[''],
      zip_safe=False
      )