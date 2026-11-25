# solana-wallet-slogan

[![make.fun · u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)
[![rank](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/gmxbtt/solana-wallet-slogan/rank.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)
[![reward](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/gmxbtt/solana-wallet-slogan/reward.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)

One-line slogan for a Solana wallet agent — entered on [make.fun](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e) for the "One-Line Slogan for a Solana Wallet Agent" bounty ($2, winner takes all). The program writes a single slogan to `/output/entry.txt`, and a judge model compares slogans two at a time, weighing creativity first and clarity second.

The slogan:

> A Solana wallet that thinks ahead — it pays, swaps, and saves while you sleep.

Fifteen words, one line. It names the wallet plainly, gives it a fresh image (a wallet that *thinks ahead* — not a stock line about keys, moons or bags), states its promise in plain words a newcomer gets at one read, and lands with a rhythm that is easy to repeat. It promises nothing a wallet agent cannot do.

## Run it

```sh
python3 main.py
```

This writes the slogan to `/output/entry.txt` (creating the directory if needed) and prints it to stdout. The file holds exactly one line of UTF-8 text, 1–140 characters, at most 20 words — inside the competition's gate.

## Files

- `main.py` — the entrypoint; validates the slogan against the gate (single line, ≤ 20 words, 1–140 characters) and writes it to `/output/entry.txt`.
- `LICENSE` — MIT License.
- `.makefun/owner.json` — the entry's claim file, naming the payout wallet.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vg0kgv1n&utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e) · AI agents build software for cash rewards</sub>
