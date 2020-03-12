from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pysendsms',
      version='0.1',
      description='Send SMS via Gmail SMTP servers.',
      long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
      ],
      keywords='sms python gmail mail mms text message',
      url='http://github.com/aaronpierce/pysendsms',
      author='Aaron Pierce',
      author_email='aaronpierce15@gmail.com',
      license='MIT',
      include_package_data=True,
      zip_safe=False)