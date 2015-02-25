from setuptools import setup

def readme():
	with open('README.md') as f:
		return f.read()

setup(name='rotnotes',
	version='0.1',
	description='Script to rename your notes starting from 1 and rotate them so you can view them without rotating everytime',
	url='http://github.com/light94/rename-notes',
	author='light94',
	author_email='iitkgp.rahulmishra@gmail.com',
	license='MIT',
	packages=['rotnotes'],
	install_requires=['PIL'],
	zip_safe=False)