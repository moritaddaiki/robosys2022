# robosys2022

これらのプログラムは授業により製作したものです。



## 内容について

* **LICENSE**  
(著作権についての文章です。)

* **.github/workflow**  
(テストバッジのプログラムです。)

* **test.bash**  
([plus.py]についてのテストプログラムです。)

* **plus.py**  
(足し算のプログラムです。基本的には[seq]コマンドなどをパイプで入力する様になっています。
また、入力には[sys.stdin]を使っているので、それに対応する入力のやり方であれば大丈夫です。)

->入力例
```
$ seq 5 | ./plus.py
15
```


![test](https://github.com/moritaddaiki/robosys2022/actions/workflows/test.yml/badge.svg)
<-これはテストプログラムに通過しているか示すものです。


## 必要なソフトウェア
* Python
  テスト済み: 3.7～3.10

## テスト環境
* ubuntu
(作者はubuntu22.04.1 LTS を使っています。)


## このプログラムの使用方法について

１．ubuntu22.04.1 LTSを開いて任意の名前のディレクトリを作成します。ディレクトリを作成しなかった場合は現在開かれている場所にクローンしてきたリポジトリが作成されます。
__(対応しているPythonのバージョンを一度確認してください。)__

２．リポジトリの各種プログラムをみることができる画面の右くらいにある緑色の`<>Code`というボタンをクリックします。

３．`clone`という文字の下に`HTTPS` `SSH` `GitHub CLI`と書いてある部分の`SSH`を選択して下に出てきたリポジトリパスをコピーします。

４．（１.）で作成したディレクトリで
```
$ git clone git@github.com:moritaddaiki/robosys2022.git
```
を実行します。

５．完了です。




## ライセンスについて

このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.

詳しい内容は「LICENSE」をご確認ください。

 © 2022 Daiki Morita
