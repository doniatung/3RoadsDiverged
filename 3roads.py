from flask import Flask

my_site = Flask(__name__)

@my_site.route('/')
def foo():
    return '<h1><font color="blue">Welcome!</font></h1>'

@my_site.route('/hi')
def moo():
    return '<h2><font color="green">Hi! My name is Donia!</font></h2>'

@my_site.route('/hello')
def goo():
    return '<h3> <font color="pink">Hello! I am excited to learn your name!</font></h3>'

if __name__ == '__main__':
   #my_site.debug = true
    my_site.run()
