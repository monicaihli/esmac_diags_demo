import setuptools
setuptools.setup(
  name="esmac_diags_demo",
  version = 1.0.alpha.demo,
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
