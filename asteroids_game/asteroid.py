from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle (screen, (255,255,255), self.position,self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split (self):
        if self.radius != ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20,30)
            vector_1 = self.velocity.rotate(random_angle)*1.2
            vector_2 = self.velocity.rotate(-random_angle)*1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = vector_1
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = vector_2
            
        
        
        self.kill()

