# judge

AtCoderのテストケースを自動チェックするPythonプログラム

## 導入方法

``` shell
$ pip install git+https://github.com/zukash/judge.git@develop
```

developブランチの最新をpip installします。

## 使い方

### テストケースのダウンロード

``` shell
$ judge fetch https://atcoder.jp/contests/abc184/tasks/abc184_a
```

初期設定では、 `./.problems` にテストケースがダウンロードされます。

### テストケースとの比較

``` shell
$ judge diff
```

1. ダウンロード済みのテストケース一覧がfzfで表示されます。問題を選択してください。
2. ソースコード一覧がfzfで表示されます。ソースコードを選択してください。
3. 実行結果が表示されます。

### ログイン

``` shell
$ judge login <USERNAME>
```

続けてパスワードを入力すると、ログイン状態になります。
これによって、コンテスト中にもテストケースをダウンロードできるようになります。

### テストケース一覧表示

``` shell
$ judge problems
```

ダウンロード済みのテストケースが一覧表示されます。

### テストケース削除

``` shell
$ judge rm
```

1. ダウンロード済みのテストケースが一覧表示されます。
2. 選択したテストケースを削除することができます。（TABで複数選択可能）

### 設定

``` shell
$ judge config <NAME> <VALUE>
```

様々な定数を設定することができます。

例えば、

``` shell
$ judge config PROBLEM_DIR ~/.config/judge/.problems
```

とすると、テストケースを保管しておくフォルダが `~/.config/judge/.problems` に変更されます。

#### 変数一覧

* PROBLEM_DIR: テストケースを保管しておくフォルダへのパス（初期設定：./.problems）
* SOLVER_EXTENSIONS: ソースコードとして認識するファイルの拡張子（初期設定：py, out）
