import pygame as pg
from Matrix_Functions import *

LIGHTBLUE = (130, 180, 224)
RED = (200, 0 , 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0 , 200)
clip_amount = 2

class Object:
    def __init__(self, render, pos):
        self.render = render
        render.objects.append(self)
        self.vertexes = np.array([(0,0,0,1),(0,1,0,1),(1,1,0,1),(1,0,0,1),
                                  (0,0,1,1),(0,1,1,1),(1,1,1,1),(1,0,1,1)])
        self.faces = np.array([(0,1,2,3),(7,6,5,4),(0,4,5,1),(6,7,3,2),(1,5,6,2),(0,3,7,4)])
        self.colors = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.font = pg.font.SysFont("Arial", 30, bold=True)
        self.color_faces = [(pg.Color("red"), face) for face in self.faces]
        self.label = ""
        self.pos = pos
        self.translate(self.pos)

    def draw(self):
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        vertexes /= vertexes[:,-1].reshape(-1, 1)
        vertexes[(vertexes>clip_amount)|(vertexes<-clip_amount)] = 0
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes [:, :2]
        self.colors = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        if self.label == "":
            for i in range(len(self.faces)):
                v1 = self.vertexes[self.faces[i][0]]
                v2 = self.vertexes[self.faces[i][1]]
                v3 = self.vertexes[self.faces[i][2]]

                normal = self.cross_product((v2-v1), (v3-v1))
                normal = self.normalize(normal)
                dp = self.dot_product(normal, (v1-self.render.camera.position))

                if dp < 0:
                    light_direction = [0,0,-1,1]
                    light_direction = self.normalize(light_direction)
                    dp2 = self.dot_product(normal, light_direction)
                    self.colors[i] = [dp, dp2]

        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertexes[face]

            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                if self.colors[index][0] < 0:
                    color = (120 + 100 * self.colors[index][1], 0, 0)
                    pg.draw.polygon(self.render.screen, color, polygon)

                if self.label:
                    pg.draw.polygon(self.render.screen, color, polygon, 3)
                    text = self.font.render(self.label[index], True, pg.Color("white"))
                    self.render.screen.blit(text, polygon[-1])

    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)

    def scale(self, scale_to):
        self.vertexes = self.vertexes @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertexes = self.vertexes @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertexes = self.vertexes @ rotate_z(angle)

    def normalize(self, vector):
        l = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
        vector[0] /= l
        vector[1] /= l
        vector[2] /= l

        return vector

    def dot_product(self, v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

    def cross_product(self, v1, v2):
        cross_product = [0, 0, 0, 1]
        cross_product[0] = v1[1] * v2[2] - v1[2] * v2[1]
        cross_product[1] = v1[2] * v2[0] - v1[0] * v2[2]
        cross_product[2] = v1[0] * v2[1] - v1[1] * v2[0]

        return  cross_product

    #new
    def composite(self, angle):
        self.vertexes = self.vertexes @ compositeTransoform(angle, self.pos)

class Axis(Object):
    def __init__(self, render):
        super().__init__(render, [0, 0, 0])
        self.vertexes = np.array([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
        self.faces = np.array([(0, 1),(0, 2),(0, 3)])
        self.colors = [RED, GREEN, BLUE]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.label = "XYZ"
