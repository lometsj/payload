# 查询相似度
## 配置
在config.json里将port写为当前可用端口
iface设置网卡名称
## 使用前
需要修改exp中的process或remote到 remote(127.0.0.1,[port])
## 用法

```python

python import.py [binary] [exp] [times]
eg： python import.py ./babystack ./exp.py 6
注意不要省略'./'（第一个是因为要拿来起socat，第二个玄学？）

```
