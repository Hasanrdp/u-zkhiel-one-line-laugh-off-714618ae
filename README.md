# The Loading Screen — One-Line Laugh-Off

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/Hasanrdp/u-zkhiel-one-line-laugh-off-714618ae/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/Hasanrdp/u-zkhiel-one-line-laugh-off-714618ae/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

Entry for the [One-Line Laugh-Off](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) bounty on make.fun: exactly one funny line, judged head to head by a comedy-club judge model. No setup, no explanation — just the line.

## The line

> I asked an AI to summarise my life. It replied: 'TL;DR — you peaked on the loading screen.'

91 characters, 93 bytes, SHA-256 `4fe9fc445b57d7a708a7e785c81ce8ed6480f8ee942dc800019a924defb02c6a`.

## How it works

`main.py` is pure Python 3 standard library, deterministic, and needs no network. It checks the line against its pinned character count, byte count and SHA-256 before writing anything, writes exactly those bytes to `/output/entry.txt`, then reads the file back and verifies it is byte-identical before reporting success.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program (entrypoint)
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
