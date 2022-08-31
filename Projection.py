import math
import numpy as np

class Projection:
    def __init__(self, render):
        NEAR = render.camera.near_plane
        FAR = render.camera.far_plane
        RIGHT = math.tan(render.camera.h_fov/2)
        LEFT = -RIGHT
        TOP = math.tan(render.camera.v_fov/2)
        BOTTOM = -TOP

        n00 = 2/(RIGHT - LEFT)
        n11 = 2/(TOP - BOTTOM)
        n22 = (FAR + NEAR)/(FAR - NEAR)
        n32 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projection_matrix = np.array([
            [n00,0,0,0],
            [0,n11,0,0],
            [0,0,n22,1],
            [0,0,n32,0]
        ])

        HW, HH =render.H_WIDTH, render.H_HEIGHT
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])