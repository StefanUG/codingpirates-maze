"""
Pluggable resource loading for maze levels/images.

CPython (desktop, `pip install codingpirates-maze`) resolves levels/images from the local
filesystem via `DefaultFilesystemProvider`. Skulpt (browser, no real filesystem) instead
fetches them from a version-pinned CDN via `SkulptBrowserProvider`. The active provider is
auto-detected via `platform.python_implementation()` so `from maze import Puzzle` just works
in both environments without any explicit wiring.

Only `DefaultFilesystemProvider` may import `os`/`importlib.resources`, and only locally
inside its methods -- those modules raise `NotImplementedError` on import under Skulpt, so
importing them at module level here (or in puzzle.py/maze.py) would crash `import maze`.
"""
import platform

IS_SKULPT = platform.python_implementation() == "Skulpt"

# Keep this aligned with the `version` in pyproject.toml and the matching GitHub release tag
# (see README) so the CDN URL below actually resolves to the release these assets ship with.
_PACKAGE_VERSION = "0.4.1"
_GITHUB_REPO = "StefanUG/codingpirates-maze"


def _default_asset_base_url() -> str:
    return f"https://cdn.jsdelivr.net/gh/{_GITHUB_REPO}@v{_PACKAGE_VERSION}/src/maze"


class ResourceProvider:
    """Strategy for loading level data and shape/image sources."""

    def get_level(self, name: str) -> dict:
        """Return the level data (as a plain dict) for a given level name."""
        raise NotImplementedError

    def get_shape_source(self, subfolder: str, name: str, ext: str = ".gif") -> str:
        """Return whatever `screen.register_shape` / `screen.bgpic` need: a local
        filesystem path (desktop) or an image URL (browser)."""
        raise NotImplementedError

    def get_setting(self, name: str, default=None):
        """Return a configuration setting by name, or the default if not found."""
        raise NotImplementedError


class DefaultFilesystemProvider(ResourceProvider):
    """Reproduces the pre-refactor filesystem-based resolution exactly."""

    def get_level(self, name: str) -> dict:
        import importlib.resources
        import json
        import os
        import sys

        filename = name if name.endswith(".json") else f"{name}.json"
        script_path = os.path.dirname(os.path.realpath(sys.argv[0]))

        resolved = None
        for candidate in (
            filename,
            os.path.join(script_path, filename),
            os.path.join(script_path, "levels", filename),
        ):
            if os.path.exists(candidate):
                resolved = candidate
                break

        if resolved is None:
            packaged = importlib.resources.files("maze.levels").joinpath(os.path.basename(filename))
            if packaged.is_file():
                resolved = packaged

        if resolved is None:
            raise TypeError("Unable to find file for level " + name)

        # `resolved` is either a plain path (str) or an importlib.resources Traversable
        opener = resolved.open if hasattr(resolved, "open") else lambda: open(resolved)
        with opener() as fp:
            return json.load(fp)

    def get_shape_source(self, subfolder: str, name: str, ext: str = ".gif") -> str:
        import importlib.resources

        with importlib.resources.path("maze.images." + subfolder, name + ext) as image_path:
            return str(image_path)

    def get_setting(self, name: str, default=None):
        """Return a configuration setting by name, or the default if not found."""
        import os
        return os.getenv(name, default)


class SkulptBrowserProvider(ResourceProvider):
    """Only ever instantiated when IS_SKULPT is True."""

    def __init__(self, asset_base_url: str):
        self.asset_base_url = asset_base_url

    def get_level(self, name: str) -> dict:
        import json
        import urllib.request

        filename = name if name.endswith(".json") else f"{name}.json"
        url = f"{self.asset_base_url}/levels/{filename}"
        return json.loads(urllib.request.urlopen(url).read())

    def get_shape_source(self, subfolder: str, name: str, ext: str = ".gif") -> str:
        # No fetch needed -- Skulpt's turtle loads images from a URL itself.
        return f"{self.asset_base_url}/images/{subfolder}/{name}{ext}"

    def get_setting(self, name: str, default=None):
        """os not available in Skulpt; simply return the default."""
        return default


_provider: ResourceProvider = (
    SkulptBrowserProvider(_default_asset_base_url()) if IS_SKULPT
    else DefaultFilesystemProvider()
)


def set_provider(provider: ResourceProvider) -> None:
    """Escape hatch for tests or to override the auto-picked default."""
    global _provider
    _provider = provider


def get_provider() -> ResourceProvider:
    return _provider
