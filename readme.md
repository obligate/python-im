# git
## gitee 初始化
+ config
```
#  需要在本地的~/.ssh/config 添加配置信息
# 1. gitee config
Host gitee.com
Hostname gitee.com
User git
IdentityFile	~/.ssh/tb_git_peter
# 2. github config
Host github.com
Hostname github.com
User git
IdentityFile	~/.ssh/tb_git_peter
```
+ init
```
cd python-im
git init 
git add .
git commit -m "init"
git remote add gitee git@gitee.com:peterhly/python-im.git
git remote add github git@github.com:peter/python-im.git
git push -u gitee   master
git push -u github  master
git remote -v
```
