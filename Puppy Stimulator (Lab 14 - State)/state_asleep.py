from puppy_state import PuppyState
import state_eat

class StateAsleep(PuppyState):
    def feed(self, puppy):
        """When the puppy is asleep, the only way to wake it up is to feed it. It will come running when
            it hears its food bowl being filled"""
        puppy.change_state(state_eat.StateEat())
        puppy.reset()
        return "The puppy wakes up and comes running to eat."
    
    def play(self, puppy):
        """You should not be able to play with puppy when it is asleep (it should continue sleeping) and
            you should not be able to feed the puppy when it is playing (it should ignore the food)"""
        return "The puppy is asleep. It doesn't want to play right now."
    