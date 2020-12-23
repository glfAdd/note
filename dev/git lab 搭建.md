- Gitlab CE社区版是免费的，EE企业版是收费的
- 下载地址

```
https://docs.gitlab.com/omnibus/manual_install.html
```

- 安装 sshd

```bash
# sudo yum install -y curl policycoreutils-python openssh-server
# sudo systemctl enable sshd
# sudo systemctl start sshd
```

- 源安装

```bash
# curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
# yum install -y gitlab-ce
```

- 使用速度更快的国内源

```bash
# vim /etc/yum.repos.d/gitlab-ce.repo

[gitlab-ce]
name=gitlab-ce
baseurl=http://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7
repo_gpgcheck=0
gpgcheck=0
enabled=1
gpgkey=https://packages.gitlab.com/gpg.key

# yum makecache
# yum install gitlab-ce
```

- 命令

```bash
# gitlab-ctl stop
# gitlab-ctl start
# gitlab-ctl restart
# gitlab-ctl status
禁止开机自启动
# sudo systemctl disable gitlab-runsvdir.service
开机自启动
# sudo systemctl enable gitlab-runsvdir.service
```

- 占用内存过大

```
gitlab默认开启进程数与CPU内核数相同, 修改gitlab.rb文件, 建议worker=CPU核数+1

# vim /etc/gitlab/gitlab.rb
unicorn['worker_processes'] = 8
重新加载配置
```

