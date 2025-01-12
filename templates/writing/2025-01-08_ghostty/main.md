自分がブラウザの次に一番使うのがターミナルだ。せっかくなら好みの見た目と使い心地にしたい。そう思い、人生で初めてターミナルをカスタマイズしてみた。

![01-neofetch.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3911823/f71e0334-09f8-698e-704e-6f452fb0cc14.png)

構成：
- マシン：M1 Pro
- OS：macOS 15.1.1 (24B91)
- パッケージマネージャ：Homebrew 4.4.13
- シェル：zsh 5.9
- ターミナル：Ghostty 1.0.0 stable
- フォント：BlexMono Nerd Font
- Theme：ohmyzsh

事前知識：
- Homebrewの使い方
- シェル、ターミナルとは何か

## ターミナルエミュレータ

macOSのデフォルトのターミナルだとカスタマイズがしづらいので、ターミナルエミュレータを使う。まだ開発がサイドプロジェクトとして始まって[3年ほど](https://mitchellh.com/writing/ghostty-devlog-001)だが、1.0.0が最近リリースされたのでGhosttyを選んだ。ちなみに開発者のMitchell HashimotoはTerraformなどを手掛けるHashicorpの創業者だ。

GhosttyのインストールはHomebrewで普通にできる。

```zsh
brew install --cask ghostty
```

## フォント

[Nerd Font](https://www.nerdfonts.com/)というシリーズのフォントがあり、これらにはアイコンが含まれているため、後ほど紹介するOh My Zshや、LazyVimで綺麗にアイコン達が表示されるようになる。

BlexMono Nerd Fontは一覧を眺めてパッと見気に入ったものを選んだ。

macOSでのNerd Fontのインストールはとても簡単で、Homebrewのコマンドひとつで済む。

```zsh
brew install --cask font-blex-mono-nerd-font
```

## Ghosttyの設定

現在Ghosttyの設定をmacOSでするには`CMD + ,`で出てくるTextEditで書くのが一番便利。そこに一つ一つの設定を書き込んでいく感じだ。

自分の設定はこうなっている。

```
background-blur-radius = 20
background-opacity = 0.9
font-family = BlexMono Nerd Font Mono
font-size = 16
mouse-hide-while-typing = true
theme = Ryuuko
window-decoration = true
```

このRyuukoというカラーテーマは初めて見たが、とても気に入った。ターミナルから直接カラーテーマのプレビューを表示できるのもGhosttyの良いところだ。

`ghostty +list-themes`でプレビューできる。

![02-list-themes.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3911823/b487c87f-c445-638e-093f-33b8b183149d.png)

設定が終わり、Ghosttyを再起動したら変更されているはずだ。

## Theme

Oh My Zshではプラグインなどでシェルの使用感をカスタマイズできるらしいが、今の自分には必要ないと感じている。これはほとんど画像の赤枠にあるところのために使っている。

![03-ohmyzsh.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3911823/a6253c7f-4c1f-058b-864d-67517c3045d0.png)

Oh My Zshをインストールすると既存の`.zshrc`が上書きされるが、インストール前のものは`.zshrc.pre-oh-my-zsh`に保存されている。

## まとめ

まだ開発途中のGhosttyを基にしたカスタマイズだが、十分早いし、今の所トラブルはない。

今までエディタは主にVimで、たまにVSCodeを使っていた。けど好みのターミナルにできたのだから、次はNeovimに挑戦しようと思っている。

![04-neovim.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3911823/ecf59b1a-244a-046f-ce29-a784a1d96972.png)

