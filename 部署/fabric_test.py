from fabric.api import run, env, runs_once, task, lcd, local, cd

env.hosts = ['10.211.55.5']
env.passwords = {'root@10.211.55.5:22': 'weiyi'}
env.user = "root"
# env.password = "weiyi"


@runs_once
@task
def local_update():
    with lcd("/Users/glfadd/Desktop/object/tools"):
        local("git add .")
        local("git commit -m 'fabric'")
        local("git pull origin master")
        local("git push origin master")


@task
def remote_update():
    with cd("/root/code/tools"):
        run("git checkout master")
        run("git pull origin master")


@task
def main():
    local_update()
    remote_update()
