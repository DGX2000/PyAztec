from distutils.core import setup

with open('README.md') as f:
    readme_md = f.read()

setup(name='pyaztec',
      version='0.1',
      description='Aztec Code Parser',
      long_description=readme_md,
      license='MIT License',
      author='Arne Voss',
      author_email='arnevoss@pm.me',
      url='https://github.com/DGX2000/PyAztec',
      packages=['pyaztec'],
      )
