##### 配置

```
git的全局配置($HOME/.gitconfig )
git config --global user.name gonglongfei
git config --global user.email 2239660080@qq.com
ssh-keygen -t rsa -C 2239660080@qq.com

/Users/laddg/.ssh
cat id_rsa.pub
```

##### 命令

```bash
git branch				# 查看分支
git	branch xxx			# 创建分支
git branch -a
git branch -d xxx		# 删除分支
git checkout xxx		# 切换分支
git checkout -b xxx		# 创建并切换分支
git pull origin xxx
git push origin xxx:aaa	# xxx是本地分支 aaa是远程分支


git stash drop stash@{0}

# 删除本地分支
git branch -D temp_test
# 删除远程分支
git push origin --delete Chapater6   可以删除远程分支Chapater6   


合并到当前分支
git merge bugfix01


git submodule update --init --recursive
合并某分支到当前分支：git merge <name>


# 更新子分支
git remote add gitlab https://gitlab.xindebaby.com/backend/Web.git
git submodule init
git submodule update
```

##### git flow

- Production: 也就是我们经常使用的Master分支，这个分支最近发布到生产环境的代码，最近发布的Release， 这个分支只能从其他分支合并，不能在这个分支直接修改
- Develop: 这个分支是我们是我们的主开发分支，包含所有要发布到下一个Release的代码，这个主要合并与其他分支，比如Feature分支
- Feature: 这个分支主要是用来开发一个新的功能，一旦开发完成，我们合并回Develop分支进入下一个Release
- Release: 当你需要一个发布一个新Release的时候，我们基于Develop分支创建一个Release分支，完成Release后，我们合并到Master和Develop分支
- Hotfix: 当我们在Production发现新的Bug时候，我们需要创建一个Hotfix, 完成Hotfix后，我们合并回Master和Develop分支，所以Hotfix的改动会进入下一个Release

##### git tag

- 创建标签

  ```bash
  git tag -a v1.0-beta -m "v1.0 beta版本发布上线"
  # 此处对历史提交做tag处理
  git log --pretty=oneline --abbrev-commit
  # 对历史提交做tag处理
  git tag -a v0.9 -m "v0.9版本发布上线" <commit-id> 
  ```

- 查看标签

  ```bash
  # 查看tag列表
  git tag
  # 查看tag列表
  git tag --list
  # 同理查看tag列表
  git tag -l
  ```

- 推送本地标签到远程仓库

  ```bash
  # 推送到远程仓库
  git push origin v1.0-beta
  # 推送到远程仓库
  git push origin v1.0-beta:refs/tags/v1.0-beta 
  # 一次性推送全部尚未推送到远程的本地tags
  git push origin --tags 
  ```

- 删除tag并且更新到远程仓库命令为：

  ```bash
  # -d参数删除掉tag
  git tag -d v1.0-beta
  # 删除掉远程仓库的tag,名称为v1.0的tag
  git push origin :refs/tags/v1.0-beta 
  ```

  





















