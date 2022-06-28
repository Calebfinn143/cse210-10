import constants
from game.casting.actor import Actor
from game.shared.point import Point


class cycler_two(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # Move head
        self._segments[0].move_next()

        # Create trail
        head = self._segments[0]
        segment = Actor()
        position = head.get_position().add(head.get_velocity().reverse())
        text = "#"
        if constants.GAME_OVER == False:
            color = constants.GREEN
        else:
            color = constants.WHITE

        segment.set_position(position)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)

    def get_head(self):
        return self._segments[0]

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = 600
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)