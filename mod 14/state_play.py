from puppy_state import PuppyState
import state_asleep

class StatePlay(PuppyState):
    def feed(self, puppy):
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        """When the puppy is playing, you can continue playing with it until it gets so tired that it falls
            asleep again (~2 or 3 times)"""
        puppy.inc_plays()
        if puppy._plays > 2:
            puppy.reset()
            puppy.change_state(state_asleep.StateAsleep())
            return "The puppy played so much it fell asleep!"
        else:
            return "You throw the ball again and the puppy exictedly chases it."