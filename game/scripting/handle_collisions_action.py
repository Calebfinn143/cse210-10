from pickle import TRUE
import constants
from game.casting.actor import Actor
from game.casting.cycler_one import cycler_one
from game.casting.score_player_one import ScorePlayerOne
from game.casting.score_player_two import ScorePlayerTwo
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score_player_one = cast.get_first_actor("scores")
        score_player_two = cast.get_second_actor("scores")
        cycler_one = cast.get_first_actor("cycler")
        cycler_two = cast.get_second_actor("cycler")
        head_one = cycler_one.get_segments()[0]
        head_two = cycler_two.get_segments()[0]
        segments = cycler_one.get_segments()[1:] + cycler_two.get_segments()[1:]
        
        for segment in segments:
            if head_one.get_position().equals(segment.get_position()):
                self._is_game_over = True
                constants.GAME_OVER = TRUE
                score_player_two.add_points(1)

            if head_two.get_position().equals(segment.get_position()):
                self._is_game_over = True
                constants.GAME_OVER = TRUE
                score_player_one.add_points(1)
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycler_one = cast.get_first_actor("cycler")
            cycler_two = cast.get_second_actor("cycler")
            segments = cycler_one.get_segments() + cycler_two.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)