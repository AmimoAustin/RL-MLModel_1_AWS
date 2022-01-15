# 1st runners up  ***debugging
class Reward:

    def __init__(self,):
        self.steering_angles = []

    def reward_function(self, params):
        steering_angle = params["steering_angle"] reward_steering = 1.0

        if len(self.steering_angles) == 0:
            self.steering_angles.append(steering_angle)
        elif self.steering_angles[-1] != steering_angle:
            self.steering_angles.append(steering_angle) reward_steering = 0.1

        if params["all_wheels_on_track"] and params["steps"] > 0:
            reward = params["progress"] / params["steps"] * 100 + params["speed"] ** 2
        else:
            reward = 0.01

        return reward + reward_steering * 10 reward_object = Reward()

        def reward_function(params):
            return reward_object.reward_function(params)