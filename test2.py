from invoke import Responder
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.utils import abort
from fabric.colors import *
from fabric import Connection

env.hosts = ['47.93.122.31']
env.port = 22
env.user = 'root'
env.password = '123qwe.com'

