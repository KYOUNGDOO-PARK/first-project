# from setuptools import setup

#setup(
#    name = 'vsearch',
#    version = '1.0',
#    description= 'The Head First Phython Search Tools',
#    author= 'HF Python 2e',
#    author_email= 'kyoungdoo.park@gmail.com',
#    url= 'headfirstlabs.com',
#    py_modules=['vsearch']
#)

def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('after :', arg)

print(double(25))

def change(arg: list):
    print('Before: ', arg)
    arg.append('more data')
    print('after :', arg)

print(change("aldkf"))
