from setuptools import setup, find_packages
setup(
      name="kukibanshee",
      version = "0.3.6",
      description="http cookie,rfc6265",
      author="dapeli",
      url="https://github.com/ihgazni2/kukibanshee",
      author_email='terryinzaghi@163.com', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/kukibanshee",
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      py_modules=['kukibanshee'], 
      )


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist

