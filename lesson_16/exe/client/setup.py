from setuptools import setup, find_packages

setup(name='client_chat_pyqt_January',
      version='0.1',
      description='Client packet',
      packages=find_packages(),
      author_email='mail@mail.ru',
      author='Ivanov I.I.',
      install_requeres=['PyQt5', 'sqlalchemy', 'pycruptodome', 'pycryptodomex']
      )
