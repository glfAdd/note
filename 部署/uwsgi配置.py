[uwsgi]
master = true
processes = 2
chmod-socket = 666
pythonpath = /home/xindebaby_qa/Web/website
logformat = %(method) %(uri) %(status) %(addr) [%(ctime)]
pidfile = /home/xindebaby_qa/run/xindebaby.pid
socket = /home/xindebaby_qa/run/xindebaby.sock
module = app
callable = app
logdate = true
harakiri = 120
listen = 1024
enable-threads=true
ignore-sigpipe = true
ignore-write-errors = true
disable-write-exception = true