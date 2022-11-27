# robosys202x

これらのプログラムは授業により製作したものです。



## 内容について

・LICENCE、README.md　は著作権関係

・test.bash、.github/workflows　はプログラムのテストプログラムです。

・plus.pyとplus-stdin.py　は基本的に機能としては同じ様なプログラムです。[seq]コマンドをパイプを使って使うことが前提になってます。
（sys.stdin）を入力に使っていますのでそれに対応する入力であれば大丈夫だと思います。

・register.py  は[./register.py 50 10 20]のように実行コマンドを打った後に入力したい数字を入力してください。段階的に足されていきます。また、入力の最後に合計がでる様になっています。


![test](https://github.com/moritaddaiki/robosys202x/actions/workflows/test.yml/badge.svg)
<-これはテストプログラムに通過しているか示すものです。


## 必要なソフトウェア
* Python
  テスト済み: 3.7から3.10

## テスト環境
* ubuntu
(作者はubuntu22.04.1 LTS を使っています。)


## このプログラムの使用方法について

１．ubuntu22.04.1 LTSを開いて[(任意の名前).py]のファイルを作成します。

２．次にgithub上のプログラムを自身の手で書き込んでください。（ここでCtrl+C等の手段で写した場合、「IndentationError: expected an indented block 」のエラーが発生してひと手間面倒くさくなるため手書きをお勧めします。）

３．ファイルを保存して閉じた後、「chmod +x (任意の名前).py」とコマンドを実行してファイルを書き込み可能な状態にします。

５．実行します。

## ライセンスについて

このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.

詳しい内容は「LICENCE」をご確認ください。
 © 2022 Daiki Morita
