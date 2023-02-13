"""
反向代理重要用途负载均衡, 主要配置proxy+pass和upsteam命令
"""

""" ============================ 依次轮询
upstream backend {
    server 102.168.1.2:80;
    server 102.168.1.3:80;
    server 102.168.1.4:80;
}

server {
    listen 80;
    server_name www.glfadd.com;
    index index.html index.htm;
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host; 
    }
}
"""

""" ============================ 加权轮询
权高处理的请求多

upstream backend {
    server 102.168.1.2:80;
    server 102.168.1.3:80;
    server 102.168.1.4:80;
}

server {
    listen 80;
    server_name www.glfadd.com;
    index index.html index.htm;
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host; 
    }
}
"""

""" ============================ 对特定资源负载均衡
/video/     使用video负载均衡
/file/      使用file负载均衡
upstream video {
    server 102.168.1.2:80;
    server 102.168.1.3:80;
    server 102.168.1.4:80;
}

upstream file {
    server 102.168.1.5:80;
    server 102.168.1.6:80;
    server 102.168.1.7:80;
}

server {
    listen 80;
    server_name www.glfadd.com;
    index index.html index.htm;
    location /video/ {
        proxy_pass http://video;
        proxy_set_header Host $host; 
    }
    
    location /file/ {
        proxy_pass http://file;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
"""

""" ============================ 不同域名负载均衡
www.video.com 使用video
www.file.com 使用file

upstream video {
    server 102.168.1.2:80;
    server 102.168.1.3:80;
    server 102.168.1.4:80;
}

upstream file {
    server 102.168.1.5:80;
    server 102.168.1.6:80;
    server 102.168.1.7:80;
}

server {
    listen 80;
    server_name www.video.com;
    index index.html index.htm;
    location / {
        proxy_pass http://video;
        proxy_set_header Host $host; 
    }
}

server {
    listen 81;
    server_name www.file.com
    location / {
        proxy_pass http://file;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
"""

""" ============================ 带有URL重写的负载均衡
客户端请求URL http:///www.file.com/file/download/media/1.mp3, 虚拟服务器首先使用location的file将URL重, 再由location的 / 转发到服务器组实现负载均衡
upstream file {
    server 102.168.1.2:80;
    server 102.168.1.3:80;
    server 102.168.1.4:80;
}

server {
    listen 80;
    server_name www.video.com;
    index index.html index.htm;
    location /file/ {
        rewrite ^(/file/.*)/media/(.*)\.*$ $1/mp3/$2.mp3 last;
    }
    
    location / {
        proxy_pass http://file 
    }
}
"""
