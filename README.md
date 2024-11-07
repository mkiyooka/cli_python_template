# README

``` sh
git clone https://x.y.com/cli_template_python.git
cd cli_template_python
. .venv/bin/activate
python -m src.calc --help

```

## direnvを利用して`. .venv/bin/activate`を省略する

``` sh:.bashrc
curl -sfL https://direnv.net/install.sh | bash 
echo '"$(direnv hook bash)"' >> ~/.bashrc

#git clone https://x.y.com/cli_template_python.git
#cd cli_template_python
echo '. .venv/bin/activate' >> .envrc
```

## uvの設定

このプロジェクトを利用する前に以下の方法でuvをインストールしてください。

``` sh
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.cargo/env"
```

uvコマンドの自動補完を設定するためには以下のコマンドを実行してください。

``` sh
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc

echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```

```
calc1: argparse
calc2: jsonargparse
calc3: typer
```