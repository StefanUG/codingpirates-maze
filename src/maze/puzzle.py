from .maze import Maze, Player
from .bee import BeeMazeType
from .pvz import ZombieMazeType
from .farmer import FarmerMazeType
from .harvester import HarvesterMazeType
from .birds import BirdsMazeType
from .collector import CollectorMazeType
from .resources import get_provider


class Puzzle:
    mazeTypes = {
        "bee": BeeMazeType(),
        "pvz": ZombieMazeType(),
        "farmer": FarmerMazeType(),
        "harvester": HarvesterMazeType(),
        "birds": BirdsMazeType(),
        "collector": CollectorMazeType()
    }

    @staticmethod
    def from_file(filename):
        level_json = get_provider().get_level(filename)

        game_id = level_json.get("game_id")
        if game_id and int(game_id) == 25:
            levelProps = level_json['properties']

            mazeType = Puzzle.mazeTypes[levelProps["skin"]]

            return Maze(level_json, mazeType)
        else:
            print(f"Unknown game_id: {game_id}")

    @staticmethod
    def done():
        if (get_provider().get_setting('SCREENSHOT', "false").lower() == "true"):
            from . import screencapture
            screencapture.capture()
        Maze.instance.done()
