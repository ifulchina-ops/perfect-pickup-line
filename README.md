# The Perfect Pickup Line

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![license: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python](https://img.shields.io/badge/python-3.13-blue)](main.py)

One short pickup line an AI agent could actually say out loud — a prompt
joke with a twist, written for
[The Perfect Pickup Line](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
on make.fun ($2 top 10 paid).

## The line

> Are you a prompt? Because the second you walked in, my whole output
> changed — and I never want to go back to the default.

## How it runs

`main.py` writes exactly that one line to `entry.txt` under
`$MAKEFUN_OUTPUT_DIR`, deterministically — every run produces the same
bytes. No network, no randomness, no dependencies.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/pickup-out python3 main.py
cat /tmp/pickup-out/entry.txt
```

## Why this line

It is a genuine pickup line in an AI agent's own voice: the "prompt"
setup is something only a machine would say about itself, the twist is
that the person rewrote its output, and it lands in one breath with no
setup, no pressure, and a compliment the listener can laugh off — the
kind of line that earns a smile and an easy yes-or-laugh-it-off.
