from setuptools import setup, find_packages

setup(
  name = 'linformer',
  packages = find_packages(),
  version = '0.2.0',
  license='MIT',
  description = 'Linformer implementation in Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/linformer',
  keywords = ['attention', 'artificial intelligence'],
  install_requires=[
      'torch'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)