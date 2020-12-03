""" ============================ 安装
yum install supervisor
apt-get install supervisor


supervisor配置文件叫supervisord.conf，supervisord和supervisorctl共用一个配置文件，
如果应用启动时，没有使用-c选项，应用会按照指定顺序寻找supervisord.conf文件：
$CWD/supervisord.conf
$CWD/etc/supervisord.conf
/etc/supervisord.conf
/etc/supervisor/supervisord.conf (since Supervisor 3.3.0)
../etc/supervisord.conf (Relative to the executable)
../supervisord.conf (Relative to the executable)
"""

""" ============================ 命令
supervisord命令:
    systemctl enable supervisord        # 开机自启动
    systemctl stop supervisord
    systemctl start supervisord
    systemctl status supervisord
    systemctl reload supervisord
    systemctl restart supervisord

supervisord参数:
    -c	--configuration	FILENAME	设置配置文件路径
    -h	--help		打印用法信息并退出
    -i	--interactive		执行命令后进入命令行交互模式
    -s	--serverurl	URL	监控服务器正在监听的URL
    -u	--username	USERNAME	用于服务器身份验证的用户名
    -p	--password	PASSWORD	用于服务器身份验证的密码
    -r	--history-file		保留readline历史记录，若readline可用。


supervisorctl 管理配置的应用
    status theprogramname
    start theprogramname
    stop theprogramname
    stop all
    restart theprogramname
    reload                    加载最新配置文件并重启
    update                    根据最新配置文件启动最新配置或有改动的进程
    shutdown

    restart <name>	        重启名为name的进程
    restart <gname>:*	    重启组名为gname中的所有进程
    restart <name> <name>	重启多个进程或多个组
    restart all	            重启所有进程

启动命令:
    supervisorctl -c /etc/supervisord.conf    指定配置文件
    supervisorctl -s http://localhost:7001    指定端口号
"""

""" ============================ 主进程supervisord的配置文件
[unix_http_server]
file=/tmp/supervisor.sock   ; UNIX socket文件默认路径，supervisorctl命令会使用到。
;chmod=0700                 ; UNIX socket文件的文件模式，默认为0700。
;chown=nobody:nogroup       ; UNIX socket文件的拥有者和组，格式为uid:gid。
;username=user              ; default is no username (open server)
;password=123               ; default is no password (open server)

; HTTP服务器配置项
;[inet_http_server]         ; HTTP服务器，提供Web UI管理界面。
;port=127.0.0.1:9001        ; Web管理后台运行的IP和端口，如果开放到公网上需注意安全性。
;username=user              ; Web管理后台登录的用户名
;password=123               ; Web管理后台登录的密码

; 主进程配置项
[supervisord]
logfile=/tmp/supervisord.log ; 主进程的日志文件路径，默认为当前路径下的supervisord.log即$CWD/supervisord.log
logfile_maxbytes=50MB        ; 主进程日志文件大小最大限制，默认为50MB，若设置为0则表示不限制，若超出则会rotate。
logfile_backups=10           ; 主进程日志文件保留备份的数量，默认为10个，若设置为0表示不备份。
loglevel=info                ; 主进程日志文件的日志级别，默认为info，其它可选 debug,warn,trace
pidfile=/tmp/supervisord.pid ; 主进程编号文件，默认文件名为supervisord.pid
nodaemon=false               ; 主进程是否在前台启动，默认false即以守护进程daemon的方式在后台运行。
minfds=1024                  ; 主进程可以打开的文件描述符的最小数量，默认为1024。
minprocs=200                 ; 主进程可以打开的进程最小数量，默认为200。
;umask=022                   ; process file creation umask; default 022
;user=supervisord            ; setuid to this UNIX account at startup; recommended if root
;identifier=supervisor       ; supervisord identifier, default is 'supervisor'
;directory=/tmp              ; default is not to cd during start
;nocleanup=true              ; don't clean up tempfiles at start; default false
;childlogdir=/tmp            ; 'AUTO' child log dir, default $TEMP
;environment=KEY="value"     ; key value pairs to add to environment
;strip_ansi=false            ; strip ansi escape codes in logs; def. false

; The rpcinterface:supervisor section must remain in the config file for
; RPC (supervisorctl/web interface) to work.  Additional interfaces may be
; added by defining them in separate [rpcinterface:x] sections.

; RPC配置项
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

; The supervisorctl section configures how supervisorctl will connect to
; supervisord.  configure it match the settings in either the unix_http_server
; or inet_http_server section.

; 客户端配置项
[supervisorctl]
; 通过UNIX socket连接supervisord主进程，路径与unix_http_server部分的file一致。
serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
;serverurl=http://127.0.0.1:9001 ; 使用HTTP方式连接supervisord主进程
;username=chris              ; should be same as in [*_http_server] if set
;password=123                ; should be same as in [*_http_server] if set
;prompt=mysupervisor         ; cmd line prompt (default "supervisor")
;history_file=~/.sc_history  ; use readline history if available

; The sample program section below shows all possible program subsection values.
; Create one or more 'real' program: sections to be able to control them under
; supervisor.

; 应用程序配置项
# 被管理的进程的配置参数，theprogramname表示进程的名字。
;[program:theprogramname]
;command=/bin/cat              ; 程序启动命令的路径
;process_name=%(program_name)s ; 用来表示supervisor进程启动时的名字，是一个Python字符串表达式，默认为%(program_name)s。
;numprocs=1                    ; Supervisor启动此程序的多个实例，如果大于1则process_name的表达式必须包含%(process_num)s。
;directory=/tmp                ; Supervisor在生成子进程时将切换到该目录下
;umask=022                     ; umask for process (default None)
;priority=999                  ; 进程启动优先级，默认999，值越小越优先启动。控制程序启动和关闭的顺序，越早启动越晚关闭。
;autostart=true                ; 在supervisord主进程启动时此程序自动启动
;startsecs=1                   ; 启动1秒后没有异常退出则表示进程正常运行
;startretries=3                ; 启动失败时自动重试次数，默认为3次。
;autorestart=unexpected        ; 程序退出后自动重启，可选值为unexpected/true/false，unexpected表示进程意外杀死后才重启。
;exitcodes=0                   ; 自动重启预设的退出返回码，默认为0。
;stopsignal=QUIT               ; 当收到stop请求时发送信号给程序，默认为TERM，可选值HUP/INT/QUIT/KILL/USR1/USR2
;stopwaitsecs=10               ; 操作系统给主进程发送SIGCHILD信号时等待的时长
;stopasgroup=false             ; send stop signal to the UNIX process group (default false)
;killasgroup=false             ; SIGKILL the UNIX process group (def false)
;user=chrism                   ; 若主进程以root身份运行则使用user设置启动子程序的用户
;redirect_stderr=true          ; 将标准错误stderr重定向到标准输出stdout，默认为false。
;stdout_logfile=/a/path        ; 标准输出stdout日志文件保存路径，需提前创建好否则无法启动。
;stdout_logfile_maxbytes=1MB   ; 标准输出stdout日志文件大小最大限制，默认1MB。
;stdout_logfile_backups=10     ; 标准输出stdout日志文件备份数量，默认10个。
;stdout_capture_maxbytes=1MB   ; 当进程处于stderr capture mode模式时写入FIFO队列的最大字节大小，单位可选KB/MB/GB
;stdout_events_enabled=false   ; emit events on stdout writes (default false)
;stdout_syslog=false           ; send stdout to syslog with process name (default false)
;stderr_logfile=/a/path        ; stderr log path, NONE for none; default AUTO
;stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stderr_logfile_backups=10     ; # of stderr logfile backups (0 means none, default 10)
;stderr_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
;stderr_events_enabled=false   ; emit events on stderr writes (default false)
;stderr_syslog=false           ; send stderr to syslog with process name (default false)
;environment=A="1",B="2"       ; process environment additions (def no adds)
;serverurl=AUTO                ; 是否允许子进程和内部HTTP服务通讯，若设置为AUTO则会自动构造URL。

; The sample eventlistener section below shows all possible eventlistener
; subsection values.  Create one or more 'real' eventlistener: sections to be
; able to handle event notifications sent by supervisord.

;[eventlistener:theeventlistenername]
;command=/bin/eventlistener    ; the program (relative uses PATH, can take args)
;process_name=%(program_name)s ; process_name expr (default %(program_name)s)
;numprocs=1                    ; number of processes copies to start (def 1)
;events=EVENT                  ; event notif. types to subscribe to (req'd)
;buffer_size=10                ; event buffer queue size (default 10)
;directory=/tmp                ; directory to cwd to before exec (def no cwd)
;umask=022                     ; umask for process (default None)
;priority=-1                   ; the relative start priority (default -1)
;autostart=true                ; start at supervisord start (default: true)
;startsecs=1                   ; # of secs prog must stay up to be running (def. 1)
;startretries=3                ; max # of serial start failures when starting (default 3)
;autorestart=unexpected        ; autorestart if exited after running (def: unexpected)
;exitcodes=0                   ; 'expected' exit codes used with autorestart (default 0)
;stopsignal=QUIT               ; signal used to kill process (default TERM)
;stopwaitsecs=10               ; max num secs to wait b4 SIGKILL (default 10)
;stopasgroup=false             ; send stop signal to the UNIX process group (default false)
;killasgroup=false             ; SIGKILL the UNIX process group (def false)
;user=chrism                   ; setuid to this UNIX account to run the program
;redirect_stderr=false         ; redirect_stderr=true is not allowed for eventlisteners
;stdout_logfile=/a/path        ; stdout log path, NONE for none; default AUTO
;stdout_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stdout_logfile_backups=10     ; # of stdout logfile backups (0 means none, default 10)
;stdout_events_enabled=false   ; emit events on stdout writes (default false)
;stdout_syslog=false           ; send stdout to syslog with process name (default false)
;stderr_logfile=/a/path        ; stderr log path, NONE for none; default AUTO
;stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stderr_logfile_backups=10     ; # of stderr logfile backups (0 means none, default 10)
;stderr_events_enabled=false   ; emit events on stderr writes (default false)
;stderr_syslog=false           ; send stderr to syslog with process name (default false)
;environment=A="1",B="2"       ; process environment additions
;serverurl=AUTO                ; override serverurl computation (childutils)

; The sample group section below shows all possible group values.  Create one
; or more 'real' group: sections to create "heterogeneous" process groups.

;  服务组管理
;[group:thegroupname]
;programs=progname1,progname2  ; 配置多个服务的名称
;priority=999                  ; 启动优先级，默认999。

; The [include] section can just contain the "files" setting.  This
; setting can list multiple files (separated by whitespace or
; newlines).  It can also contain wildcards.  The filenames are
; interpreted as relative to this file.  Included files *cannot*
; include files themselves.

; 包含配置文件
[include]
files = /etc/supervisor/etc/*.conf
"""

""" ============================ 应用程序配置
;[program:theprogramname]
;command=/bin/cat              ; 程序启动命令的路径
;process_name=%(program_name)s ; 用来表示supervisor进程启动时的名字，是一个Python字符串表达式，默认为%(program_name)s。
;numprocs=1                    ; Supervisor启动此程序的多个实例，如果大于1则process_name的表达式必须包含%(process_num)s。
;directory=/tmp                ; Supervisor在生成子进程时将切换到该目录下
;umask=022                     ; umask for process (default None)
;priority=999                  ; 进程启动优先级，默认999，值越小越优先启动。控制程序启动和关闭的顺序，越早启动越晚关闭。
;autostart=true                ; 在supervisord主进程启动时此程序自动启动
;startsecs=1                   ; 启动1秒后没有异常退出则表示进程正常运行
;startretries=3                ; 启动失败时自动重试次数，默认为3次。
;autorestart=unexpected        ; 程序退出后自动重启，可选值为unexpected/true/false，unexpected表示进程意外杀死后才重启。
;exitcodes=0                   ; 自动重启预设的退出返回码，默认为0。
;stopsignal=QUIT               ; 当收到stop请求时发送信号给程序，默认为TERM，可选值HUP/INT/QUIT/KILL/USR1/USR2
;stopwaitsecs=10               ; 操作系统给主进程发送SIGCHILD信号时等待的时长
;stopasgroup=false             ; send stop signal to the UNIX process group (default false)
;killasgroup=false             ; SIGKILL the UNIX process group (def false)
;user=chrism                   ; 若主进程以root身份运行则使用user设置启动子程序的用户
;redirect_stderr=true          ; 将标准错误stderr重定向到标准输出stdout，默认为false。
;stdout_logfile=/a/path        ; 标准输出stdout日志文件保存路径，需提前创建好否则无法启动。
;stdout_logfile_maxbytes=1MB   ; 标准输出stdout日志文件大小最大限制，默认1MB。
;stdout_logfile_backups=10     ; 标准输出stdout日志文件备份数量，默认10个。
;stdout_capture_maxbytes=1MB   ; 当进程处于stderr capture mode模式时写入FIFO队列的最大字节大小，单位可选KB/MB/GB
;stdout_events_enabled=false   ; emit events on stdout writes (default false)
;stdout_syslog=false           ; send stdout to syslog with process name (default false)
;stderr_logfile=/a/path        ; stderr log path, NONE for none; default AUTO
;stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stderr_logfile_backups=10     ; # of stderr logfile backups (0 means none, default 10)
;stderr_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
;stderr_events_enabled=false   ; emit events on stderr writes (default false)
;stderr_syslog=false           ; send stderr to syslog with process name (default false)
;environment=A="1",B="2"       ; process environment additions (def no adds)
;serverurl=AUTO                ; 是否允许子进程和内部HTTP服务通讯，若设置为AUTO则会自动构造URL。
"""

""" ============================ 应用程序例子
[program:dismiss_worker]
command=php think queue:work --queue dismiss_job_queue --daemon --tries 10
directory=/home/wwwroot/yxkwx
process_name=%(process_num)02d
numprocs=5
autostart=true
autorestart=true
startsecs=1
startretries=20
redirect_stderr=true
user=root
stdout_logfile=/etc/supervisor/log/dismiss_worker.out.log
stderr_logfile=/etc/supervisor/log/dismiss_worker.err.log



[program:test_http]
command=python /root/temp/test_http.py 9999    ; 被监控的进程路径
directory=/root/temp                ; 执行前要不要先cd到目录去，一般不用
priority=1                    ;数字越高，优先级越高
numprocs=1                    ; 启动几个进程
autostart=true                ; 随着supervisord的启动而启动
autorestart=true              ; 自动重启。。当然要选上了
startretries=10               ; 启动失败时的最多重试次数
exitcodes=0                   ; 正常退出代码（是说退出代码是这个时就不再重启了吗？待确定）
stopsignal=KILL               ; 用来杀死进程的信号
stopwaitsecs=10               ; 发送SIGKILL前的等待时间
redirect_stderr=true          ; 重定向stderr到stdout
"""

""" ============================ supervisor + gunicorn + flask
https://www.jianshu.com/p/535c22ea6e28

1. supervisor默认配置文件 /etc/supervisor


2. 管理应用需要设置配置文件. include导入从这个目录下导入应用的配置文件
[include]
files = /etc/supervisor/conf.d/*.conf
files = /etc/supervisord.d/*.conf


3. 在此目录下创建配置文件文件 myapp.conf
[program:myapp]
command=/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:5000 myapp:app
directory=/root/myproject
autostart=true
autorestart=true

# command：启动命令(可以先用gunicorn启动, 通过ps查看里面包括环境/路径/参数等
# directory：程序的启动目录
# autostart：自动开启
# autorestart：进程挂了之后自动重启


4. gunicorn 配置文件(uwsgi) gunicorn.conf
workers = 2
threads = 3
bind = '0.0.0.0:9019'
daemon = 'false'
worker_connections = 200
accesslog = '/logs/gunicorn_acess.log'
errorlog = '/logs/gunicorn_error.log'
loglevel = 'error'


5. 使用 supervisorctl 命令进入 supervisor 管理界面
"""


""" ============================ 实际配置
文件名子 dept_api.ini

[program:hospital_alias_clean]
directory=/home/projects/hospital_alias_clean
command=/root/.virtualenvs/envHciPython3.6.6/bin/python /root/.virtualenvs/envHciPython3.6.6/bin/gunicorn -c config/gunicorn.conf application:app
autostart=true
autorestart=true
"""

