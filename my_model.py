# model clone is more improved
# my model will be trained with 4 reward functions to learn more from its environment
def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 4 markers that are at varying distances away from the center line
    marker_1 = 0.05 * track_width
    marker_2 = 0.1 * track_width
    marker_3 = 0.25 * track_width
    marker_4 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.75
    elif distance_from_center <= marker_3:
        reward = 0.5
    elif distance_from_center <= marker_4:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return float(reward)

# HOW DO YOU TRAIN A MODEL?
# play around with the reward function and use the simulation movie to judge how it affects your car’s behavior
# train the model on different racing courses to get a stable behavior
# more complex reward functions and more movement possibilities set in the DeepRacer UI increase training time
