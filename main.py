#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes one line — the excuse a gamer texts the boss to skip work
on GTA 6 launch week — to $ENTRY_OUTPUT_DIR/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

LINE = "Boss, boiler burst, flat's flooded, plumber's here till noon, he brought his PS5, says the Wi-Fi's the real leak."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
