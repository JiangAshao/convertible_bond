# convertible_bond
设置定时任务，每天抓取最新的可转债信息，并通过 sct.ftqq.com 推送到微信
现在是只提醒当天可以打的新债或者当天上市的新债

## 使用方法
安装依赖项：
```
pip3 install requests  或者 pip3 -r install requirements.txt
```

在 [sct.ftqq.com](https://sct.ftqq.com) 扫码登录并获得 SendKey。然后在[消息通道](https://sct.ftqq.com/forward)中配置好你想要的消息通道，并做好测试，确保该 SendKey 可以将消息送达。

接着将 `wx_send.py` 里你的 SendKey 填入其中，注意不要更改文件的格式。

最后在终端中运行：
```
python3 kzz.py
```

## 定时推送
- Linux/macOS：
  终端中运行 `crontab -e`，在文件末尾加上一行（注意换成实际的路径）
  ```
  30 9 * * * python3 /path/to/convertible_bond/kzz.py
  ```

- Windows:
  见[Win10设置定时运行任务](https://zhuanlan.zhihu.com/p/115187442)

## 参考说明
感谢[@the-eric-kwok](https://github.com/the-eric-kwok)
根据[Convertible_Bond_Monitor](https://github.com/the-eric-kwok/Convertible_Bond_Monitor.git)修改
如有侵权，请联系我删除

## 特别声明
* 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。
* 请勿将本仓库的任何内容用于商业或非法目的，否则后果自负。
* 任何以任何方式查看此项目的人或直接或间接使用该项目的任何脚本的使用者都应仔细阅读此声明。本人保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本的规则，则视为您已接受此免责声明。

## 关于打赏
如果对你有帮助可以点个赞哦，或者打赏作者一杯咖啡哟～
<img width="609" alt="支付宝" src="https://user-images.githubusercontent.com/11848358/143569245-7b1fe1bd-d170-4327-b729-459ae191fbc1.png">
<img width="609" alt="微信" src="https://user-images.githubusercontent.com/11848358/143569385-553ec9d1-0cad-44bf-8dcb-c444218832c0.png">
