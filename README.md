# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/Djebrix/excuse-almost-works/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/Djebrix/excuse-almost-works/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

Entry for [The Excuse That Almost Works](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5) — the one line a gamer texts the boss to skip work on GTA 6 launch week.

## The line

> Boss, boiler burst, flat's flooded, plumber's here till noon, he brought his PS5, says the Wi-Fi's the real leak.

A boiler flood is the kind of boring, believable emergency a tired manager has heard before — until the plumber shows up with a PS5. The excuse collapses on exactly one detail.

## Run

```sh
python3 main.py
```

Writes the line to `$ENTRY_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```

Stdlib only, no network, deterministic: two runs produce byte-identical output.
