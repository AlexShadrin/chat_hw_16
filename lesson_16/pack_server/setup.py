from setuptools import setup, find_packages

setup(name='server_chat_pyqt_January',
      version='0.2',
      description='Server packet',
      packages=find_packages(),
      author_email='mail@mail.ru',
      author='Ivanov I.I.',
      install_requeres=['PyQt5', 'sqlalchemy', 'pycruptodome', 'pycryptodomex']
      )