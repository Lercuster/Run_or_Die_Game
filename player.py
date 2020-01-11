import pygame
import numpy as np


class Player():
    """ """

    def __init__(self, settings, screen):
        self.screen = screen
        self.speed = settings.player_speed
        self.moving = False
        #self.settings = settings
        self.color = settings.player_color
        self.radius = settings.player_radius
        self.start_pos_center = settings.game_field_width // 2
        self.center = self.start_pos_center
        self.start_pos_bottom = settings.screen_height - 3.5 * settings.player_radius
        self.bottom = self.start_pos_bottom
        self.direction_vector = np.array([0, 1])
        self.steering_vector = np.array([0, 0])
        # movement boundaries #
        self.bound_left = settings.grid_block_size + self.radius
        self.bound_up = settings.grid_block_size + self.radius
        self.bound_right = settings.game_field_width - settings.grid_block_size - self.radius
        self.bound_bottom = settings.screen_height - settings.grid_block_size - self.radius

    def update(self):
        """ move player """
        if self.moving:
            self.direction_vector = self.direction_vector + self.steering_vector
            self.normalize_direction_vector()
            self.center -= self.direction_vector[0]
            self.bottom -= self.direction_vector[1]
            if self.bottom <= self.bound_up or self.bottom >= self.bound_bottom:
                self.moving = False
                self.reset_to_initial_pos()
            if self.center >= self.bound_right or self.center <= self.bound_left:
                self.moving = False
                self.reset_to_initial_pos()

    def reset_to_initial_pos(self):
        self.center = self.start_pos_center
        self.bottom = self.start_pos_bottom
        self.direction_vector = np.array([0, 1])
        self.steering_vector = np.array([0, 0])

    def get_orto_vector(self, dir):
        if dir == 'r':
            return np.array([-self.direction_vector[1], self.direction_vector[0]])
        elif dir == 'l':
            return np.array([self.direction_vector[1], -self.direction_vector[0]])

    def normalize_direction_vector(self):
        self.direction_vector = self.direction_vector / np.linalg.norm(self.direction_vector)

    def blitme(self):
        """ draw player """
        pygame.draw.circle(self.screen, self.color, (int(self.center), int(self.bottom)), self.radius)