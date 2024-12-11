from puppy_state import PuppyState
import state_play
import state_asleep

class StateEat(PuppyState):
    def feed(self, puppy):
        puppy.inc_feeds()
        # it will fall back asleep (after ~2 or 3 times)
        if puppy._feeds > 2:
            puppy.reset()
            puppy.change_state(state_asleep.StateAsleep())
            return "The puppy ate so much it fell asleep!"
        
        else:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
    
    def play(self, puppy):
        puppy.reset()
        puppy.change_state(state_play.StatePlay())
        return "The puppy looks up from its food and chases the ball you threw."
    