# maze

This is the Python Turtle-graphics maze framework and the code.org level importer behind the
[Coding Pirates Python puzzles](https://github.com/StefanUG/code-org-python) student repository.

It is published to PyPI as `codingpirates-maze`, but imported in code as `maze`:

```
pip install codingpirates-maze
```

```python
from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while1_2024")
farmer: Farmer = maze.player
```

Level files are bundled with the package under `src/maze/levels/`, so `Puzzle.from_file(name)`
works the same way whether `maze` is installed from PyPI or from a local/editable checkout.

# Repository layout

- `src/maze/` — the published package: the Turtle-based maze framework, game skins (bee, farmer,
  harvester, birds, collector, plants-vs-zombies) and the bundled level `.json` files.
- `src/importer/` — a dev-only tool (not needed by students) that imports lesson/level content from
  a locally checked out clone of [code.org's `code-dot-org`](https://github.com/code-dot-org/code-dot-org)
  repository and generates:
  - the student-facing puzzle `.py` files (written into the student repo),
  - the private `test_*.py` solution files and matching level `.json` files (written into this repo).
- `course*-*/` — mirrors the student repo's course/lesson folder structure, but only holds the
  private `test_*.py` solution files (used by `test_all.py` for regression testing). It
  intentionally excludes the student-facing puzzle files and has no `levels/` subfolder — the level
  `.json` files instead live in `src/maze/levels/`.

Only lessons that code.org has released under a Creative Commons license are imported and re-shared
here, using alternative artwork since code.org holds exclusive rights to their own artwork.

# Local development

1. `poetry install --with importer` (the `importer` group pulls in Jinja2, only needed to run the
   importer; the published `codingpirates-maze` package has no runtime dependencies).
2. Run the regression tests: `python test_all.py` (recurses into every `course*-*/**/test_*.py`).
3. Run the importer, e.g.:
   ```
   python -m importer.create_course -s ../code-dot-org -t ../code-org-python -m . coursed-2024
   ```
   This writes puzzle `.py` files into the student repo (`-t`), and level `.json` + `test_*.py`
   files into this repo (`-m`).

# Publishing to PyPI

Releases are published via GitHub Actions using PyPI Trusted Publishing — see
`.github/workflows/publish.yml`. Push a `v*` tag / create a GitHub Release to trigger a publish.

# Artwork Attribution

Code.org has exclusive rights to their artwork and graphics, so alternative artwork was used
instead. The graphics and artwork is found on https://opengameart.org/. Specific mentions should go
to the following for the bits used.

## Bee

* Honeycomb from [Admurin's Insect Items](https://opengameart.org/content/admurins-insect-items)
* Grass background from [LPC Tile Atlas](https://opengameart.org/content/lpc-tile-atlas)
* Flowers from [Plants and Flowers - Pixel Art](https://opengameart.org/content/plants-and-flowers-pixel-art)

## Plants vs. Zombies

* Ground tiles from [Whispers of Avalon: Grassland Tileset](https://opengameart.org/content/whispers-of-avalon-grassland-tileset)
* Evil Flower obstacle from: [Bevouliin Free sprite sheets - Plant Monster](https://opengameart.org/content/bevouliin-free-sprite-sheets-plant-monster)
* Sunflower from [Plants and Flowers - Pixel Art](https://opengameart.org/content/plants-and-flowers-pixel-art)

## Farmer and Harvester

* Crops from [LPC Crops](https://opengameart.org/content/lpc-crops)
* Background from [LPC Farming tilesets, magic animations and UI elements](https://opengameart.org/content/lpc-farming-tilesets-magic-animations-and-ui-elements)

## Birds

* Grass background, same as Bee
* "Pig" monster from [Fat Green Monster Sprites](https://opengameart.org/content/fat-green-monster-sprites)
* Walls from [Platformer Tiles](https://opengameart.org/content/platformer-tiles) and [Shape Characters](https://opengameart.org/content/shape-characters)
* TNT from [Wooden Boxes Crates](https://opengameart.org/content/wooden-boxes-crates)

## Collector

* Walls, Floor and Gem from [Dungeon Crawl 32x32 tiles](https://opengameart.org/content/dungeon-crawl-32x32-tiles)
