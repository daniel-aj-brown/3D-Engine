import pygame as pg
from Object import *
from Camera import *
from Projection import *

class threeDEngine:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 800, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH //2, self.HEIGHT//2
        self.FPS = 0
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.dt = 0

        self.objects = []
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)

        self.cube = Object(self, [1, 0, 0])
        self.world_axis = Axis(self)
        self.world_axis.scale(2.5)

        self.angle = 0

    def input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        self.camera.control(self.dt)

    def update(self):
        self.cube.rotate_y(self.dt * 0.001)
        self.cube.rotate_x(self.dt * 0.0005)


    def draw(self):
        self.screen.fill(LIGHTBLUE)
        for object in self.objects:
            object.draw()

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.dt = self.clock.tick(self.FPS)

if __name__ == "__main__":
    app = threeDEngine()
    app.run()
