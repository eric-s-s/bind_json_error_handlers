from setuptools import setup, find_packages


with open("README.rst", "r") as fh:
    long_description = fh.read()

VERSION = '1.1.2'

setup(name='bind_json_error_handlers',
      version=VERSION,
      description='make app return json errors',
      long_description=long_description,
      keywords='',
      url='https://github.com/eric-s-s/bind_json_error_handlers',
      author='Eric Shaw',
      author_email='shaweric01@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      packages=find_packages(exclude=['tests']),
      install_requires=['flask', 'requests'],
      include_package_data=True,
      zip_safe=False)
