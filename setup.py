import setuptools
setuptools.setup(
  name="esmac_diags_demo",
  version = "1.0.0a",
  license="BSD",
  packages=find_packages(
    where='src'
  ),
  package_dir={"": "src"},
  install_requires=[
    "numpy",
    "pytest",
    "matplotlib",
    "netCDF4",
    "pip"]

)
