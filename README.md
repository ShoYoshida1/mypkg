# mypkg
[![test](https://github.com/ShoYoshida1/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ShoYoshida1/mypkg/actions/workflows/test.yml)

Ros2の課題及び練習リポジトリ

## リポジトリ内のファイル詳細

### talker.py
数字をカウントしてトピック/countupを通じて送信するパブリッシャノード

### listener.py
/countupからメッセージをもらって表示するサブスクライバノード

### talk_listen.launch.py
talkerとlistenerの二つのノードを同時に起動するもの

### janken_publisher.py
3種類のじゃんけん動きをトピック/janken_pubを通じてランダムに送信するパブリッシャノード

### janken_subscriber.py
/janken_pubからじゃんけんの手を受け取って記録し標準入力に使用者が手を入力したものと勝敗判定を行うノード

## 実行方法(talker-listener)

```bash
端末1$ ros2 run mypkg talker
端末2$ ros2 run mypkg listener
[INFO] [1703836466.532205845] [listener]: Listen: 0
[INFO] [1703836467.039620010] [listener]: Listen: 1
[INFO] [1703836467.537382352] [listener]: Listen: 2
[INFO] [1703836468.036067184] [listener]: Listen: 3
[INFO] [1703836468.533279278] [listener]: Listen: 4
[INFO] [1703836469.031189114] [listener]: Listen: 5
[INFO] [1703836469.528300177] [listener]: Listen: 6
[INFO] [1703836470.025618536] [listener]: Listen: 7
```
実行すると以上のように出力される. 終了するときは`Ctrl+C`を押してください

または
```bash
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/shoinyoshida/.ros/log/2023-12-29-16-58-38-404317-MeisterC-29289
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [29291]
[INFO] [listener-2]: process started with pid [29293]
[listener-2] [INFO] [1703836719.211164940] [listener]: Listen: 0
[listener-2] [INFO] [1703836719.703729567] [listener]: Listen: 1
[listener-2] [INFO] [1703836720.203602809] [listener]: Listen: 2
[listener-2] [INFO] [1703836720.704242384] [listener]: Listen: 3
[listener-2] [INFO] [1703836721.204415568] [listener]: Listen: 4
[listener-2] [INFO] [1703836721.703649442] [listener]: Listen: 5
[listener-2] [INFO] [1703836722.204310074] [listener]: Listen: 6
```
 終了するときは`Ctrl+C`を押してください

## 実行方法(janken_pubrisher-janken_subscriber)
じゃんけんゲーム


