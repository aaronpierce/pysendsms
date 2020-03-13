from setuptools import setup

readme = open('README.md').read()

setup(name                              =       'pysendsms',
      version                           =       '0.1.4',
      description                       =       'Send SMS via Gmail SMTP servers.',
      long_description                  =        readme,
      long_description_content_type     =       'text/markdown',
      classifiers                       =       [
                                                'Development Status :: 3 - Alpha',
                                                'License :: OSI Approved :: MIT License',
                                                'Intended Audience :: Developers',
                                                'Programming Language :: Python',
                                                'Programming Language :: Python :: 3',
                                                'Topic :: Communications :: Email',
                                                'Topic :: Software Development :: Libraries :: Python Modules',
                                                ],
      keywords                          =       'sms python gmail mail mms text message',
      url                               =       'http://github.com/aaronpierce/pysendsms',
      author                            =       'Aaron Pierce',
      author_email                      =       'aaronpierce15@gmail.com',
      license                           =       'MIT',
      packages                          =       ['pysendsms'],
      include_package_data              =       True,
      python_requires                   =       '>=3')