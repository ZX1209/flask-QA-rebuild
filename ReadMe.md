这是基于原先的 flask-QA 的 重置做版本.

基本的框架还是 python3 flask
静态页面就好了.
首先,关于数据库,我想使用高层次的ORM嗯.希望不会由太大问题
现在还是先用着 sqlite3 吧.本地的数据.

# todo
- [ ] 配置好本机的环境(虚拟环境)
```bash
python -m venv venv

venv\Scripts\activate

deactivate

```

- [x] 配置好git仓库
```bash
githubApi --username --password createRepo --repoName='something'

# add remote node
git remote add origin {remote_url}
git push -u origin master
git push --set-upstream origin master # 设置默认 push 目标
```
- [x] peewee?
foreign learned

- [ ] restfull api 构建

- [ ] 带着 flask-template
- [ ] 常用页面.
- [ ] 测试?




