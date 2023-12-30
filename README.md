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
3種類のじゃんけん動きをトピック/janken_pubを通じてランダムに送信し続けるパブリッシャノード

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
二つのノードを起動すると以下のように表示されます。

```bash
端末1$ ros2 run mypkg janken_publisher
端末2$ ros2 run mypkg janken_publisher
Waiting....
Enter your move (rock, paper, scissors):
```
`Enter your move (rock, paper, scissors):`が表示されたら`rock, paper, scissors`のどれかを入力してください。間違えて入力された場合再び相手から手が受信され入力できるようになります。

```bash
Waiting....
Enter your move (rock, paper, scissors):rock
You win!
```
終了するときは`Ctrl+C`を押してください

## 必須ソフト
python

## テスト環境
* ubuntu 20.04
* ROS2foxy

## ライセンス
* このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます．
* このパッケージのコードの一部は, 下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを, 本人の許可を得て自身の著作としたものです．
   * [ryuichiueda/my_slides/robosys_2022/lesson8](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson9](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson10](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson11](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/)
* © 2023 Sho Yoshida
