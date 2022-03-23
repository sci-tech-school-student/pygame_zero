import itertools


# We just put something on the screen
BLOCK_POSITIONS = [
    (750, 50),
    (750, 550),
    (50, 550),
    (50, 50),
]

block_positions = itertools.cycle(BLOCK_POSITIONS)
block = Actor('block', center=(50, 50))


def draw():
    screen.clear()
    block.draw()


def move_block():
    """Move the block to the next position over 1 second."""
    animate(
        block,
        duration=1,
        pos=next(block_positions),
        on_finished=move_block
    )


move_block()
