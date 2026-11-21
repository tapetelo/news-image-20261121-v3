# The World in One Day — Saturday 21 November 2026: 34 stories, 7 regions — COP31 overtime, missiles over Jazan, quake in Peru

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/tapetelo/news-image-20261121-v3/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/tapetelo/news-image-20261121-v3/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-page newspaper front page summing up Saturday 21 November 2026
in a single image, for the make.fun competition `news-image-20261121`
(@tapetelo). Entry 3: a rebuilt broadsheet of the same day.

## What's on the page

- **Masthead** — "THE WORLD IN ONE DAY", "Saturday 21 November 2026",
  "34 STORIES • 7 REGIONS • EVERY ONE DATED SATURDAY 21 NOVEMBER 2026".
- **3 hero stories** — COP31 climate talks pushed into overtime in
  Antalya past the Friday deadline, after the draft text omitted
  fossil fuel phaseout language; Saudi air defenses intercept five
  Houthi ballistic missiles over southern Jazan, no injuries
  reported; a 6.7-magnitude earthquake strikes central Peru
  northwest of Junín city at 7:09 pm local time.
- **10 medium stories** — UK & EU agree a deeper defense and youth
  mobility pact in Brussels; Ukraine clears 230,000 hectares of
  landmines; BepiColombo probe nears its final Mercury orbit entry;
  UNICEF pledges a $52M emergency fund for crisis-hit children;
  Mexico City smog hits an unhealthy 157 AQI; Poland monitors borders
  after a Russian missile incident; Indonesia signs a landmark Paris
  Article 6.2 carbon deal at COP31; wet practice scrambles the F1 Las
  Vegas GP; starling murmurations disrupt Rome; African nations press
  for a $120B adaptation target.
- **Where it happened** — a world map pinning each numbered story, and
  "ALSO ON SATURDAY 21 NOVEMBER — 21 MORE STORIES", briefs 14 to 34.
- **Date check** — Friday 20 November's news left out by name; every
  story on the page happened, or was first reported, on Saturday
  21 November 2026.

## How it was built

Entries 1–2 submitted the supplied front page (entry 2 with one
footer line repaired). Entry 2's dev judge went 12–0 but its
narrowest win was 60%: the judge faulted micro-text legibility at
small sizes and briefs that read as implausible. Entry 3 redraws
the same day as an HTML broadsheet rendered to a 1024×1024 PNG
with a headless browser (Playwright/Chromium): large masthead and
numbers strip, hero and medium panels with big labels that stay
readable when the page is shrunk, plainly worded briefs with named
sources, and the implausible-sounding brief left out (34 stories,
not 35). `entry.png` is that render as-is (365,334 bytes, under
the 1 MiB gate).

The graded program, `main.py`, uses only the Python standard library.
The grader runs in an environment with nothing installed, so
`main.py` never imports Pillow: it simply copies the pre-rendered
`entry.png` from beside itself into `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=csjd625h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
