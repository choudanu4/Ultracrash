# Astrocrash 1
# Get asteroids moving on the screen


import random, math
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Wrapper(games.Sprite):
    """A sprite that wraps around the screen"""
    def update(self):
        """Wrap sprite around screen."""
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
    def die(self):
        """destroy self"""
        self.destroy()

class Collider(Wrapper):
    """A Wrapper that can collide with another object."""
    def update(self):
        """Check for overlapping sprites"""
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """Destroy self and leave explosion behind. """
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()
        
class Explosion(games.Animation):
    """Explosion animation. """
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)
        Explosion.sound.play()
        

class Asteroid(Wrapper):
    """ An asteroid which floats across the screen."""
    SPAWN = 2
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("asteroid_small.bmp"),
              MEDIUM : games.load_image("asteroid_med.bmp"),
              LARGE : games.load_image("asteroid_big.bmp") }
    SPEED = 2
    POINTS = 30
    total = 0

    def __init__(self, game, x, y, size):
        """Initialize asteroid sprite. """
        super(Asteroid, self).__init__(
            image = Asteroid.images[size],
            x = x, y = y,
            dx = random.choice([1,-1]) * Asteroid.SPEED * random.random()/size,
            dy = random.choice([1,-1]) * Asteroid.SPEED * random.random()/size)

        self.size = size
        Asteroid.total += 1
        self.game = game

    def die(self):
        """Destroy asteroid,then spawn debris"""
        Asteroid.total -= 1
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game,
                                        x = self.x,
                                        y = self.y,
                                        size = self.size -1)
                games.screen.add(new_asteroid)
        super(Asteroid, self).die()
        # if all asteroids are gone, advance to next level
        if Asteroid.total == 0:
            self.game.advance()
        
            

class Ship(Collider):
    """ A moving ship."""
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = 0.03
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3
    sound = games.load_sound("thrust.wav")
    ammo = 10

    def __init__(self, game, x, y):
        """initialize a ship"""
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0
        self.game = game
        

    
    def update(self):
        """Move ship based on keys pressed."""
        super(Ship, self).update()
        # if waiting until the ship can fire next, decrease wait
        if self.missile_wait > 0:
            self.missile_wait -= 1
        
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi / 180 # convert ship's angle to radians
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            if self.ammo == 0:
                Missile.none.play()
            else:
                new_missile = Missile(self.x, self.y, self.angle)
                games.screen.add(new_missile)
                self.missile_wait = Ship.MISSILE_DELAY

        if games.keyboard.is_pressed(games.K_TAB):

            if games.keyboard.is_pressed(games.K_a):
                Vocab.current_guess += "a"
            if games.keyboard.is_pressed(games.K_b):
                Vocab.current_guess += "b"
            if games.keyboard.is_pressed(games.K_c):
                Vocab.current_guess += "c"
            if games.keyboard.is_pressed(games.K_d):
                Vocab.current_guess += "d"
            if games.keyboard.is_pressed(games.K_e):
                Vocab.current_guess += "e"
            if games.keyboard.is_pressed(games.K_f):
                Vocab.current_guess += "f"
            if games.keyboard.is_pressed(games.K_g):
                Vocab.current_guess += "g"
            if games.keyboard.is_pressed(games.K_h):
                Vocab.current_guess += "h"
            if games.keyboard.is_pressed(games.K_i):
                Vocab.current_guess += "i"
            if games.keyboard.is_pressed(games.K_j):
                Vocab.current_guess += "j"
            if games.keyboard.is_pressed(games.K_k):
                Vocab.current_guess += "k"
            if games.keyboard.is_pressed(games.K_l):
                Vocab.current_guess += "l"
            if games.keyboard.is_pressed(games.K_m):
                Vocab.current_guess += "m"
            if games.keyboard.is_pressed(games.K_n):
                Vocab.current_guess += "n"
            if games.keyboard.is_pressed(games.K_o):
                Vocab.current_guess += "o"
            if games.keyboard.is_pressed(games.K_p):
                Vocab.current_guess += "p"
            if games.keyboard.is_pressed(games.K_q):
                Vocab.current_guess += "q"
            if games.keyboard.is_pressed(games.K_r):
                Vocab.current_guess += "r"
            if games.keyboard.is_pressed(games.K_s):
                Vocab.current_guess += "s"
            if games.keyboard.is_pressed(games.K_t):
                Vocab.current_guess += "t"
            if games.keyboard.is_pressed(games.K_u):
                Vocab.current_guess += "u"
            if games.keyboard.is_pressed(games.K_v):
                Vocab.current_guess += "v"
            if games.keyboard.is_pressed(games.K_w):
                Vocab.current_guess += "w"
            if games.keyboard.is_pressed(games.K_x):
                Vocab.current_guess += "x"
            if games.keyboard.is_pressed(games.K_y):
                Vocab.current_guess += "y"
            if games.keyboard.is_pressed(games.K_z):
                Vocab.current_guess += "z"
            if games.keyboard.is_pressed(games.K_a) and games.keyboard.is_pressed(games.K_LALT):
                Vocab.current_guess += "á"
            if games.keyboard.is_pressed(games.K_e) and games.keyboard.is_pressed(games.K_LALT):
                Vocab.current_guess += "é"
            if games.keyboard.is_pressed(games.K_i) and games.keyboard.is_pressed(games.K_LALT):
                Vocab.current_guess += "í"
            if games.keyboard.is_pressed(games.K_o) and games.keyboard.is_pressed(games.K_LALT):
                Vocab.current_guess += "ó"
            if games.keyboard.is_pressed(games.K_u) and games.keyboard.is_pressed(games.K_LALT):
                Vocab.current_guess += "ú"
            if games.keyboard.is_pressed(games.K_n) and games.keyboard.is_pressed(games.K_LALT):
                Vocab.current_guess += "ñ"
            if games.keyboard.is_pressed(games.K_BACKSPACE):
                Vocab.current_guess -= Vocab.current_guess[len.Vocab.current_guess]
            if games.keyboard.is_pressed(games.K_RETURN):
                Vocab.check()
            if games.keyboard.is_pressed(games.K_SPACE) and games.keyboard.is_pressed(games.K_LALT):
                Vocab.current_guess += " "
            
        

        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

        #cap velocity in each direction
        self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
        self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

        #updates current_guess with new keyboard input
        Vocab.check(Vocab)

    def die(self):
        """Destroy ship and end the game."""
        self.game.end()
        super(Ship, self).die()
        

class Missile(Collider):
    """ A missile launched by the player's ship."""
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    none = games.load_sound("no_missiles.wav")
    
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40
    

    def __init__(self, ship_x, ship_y, ship_angle):
        """Initialize the missile sprite."""           
        Ship.ammo -= 1
        Missile.sound.play()
        # convert to radians
        angle = ship_angle *math.pi / 180

        # calculate missile's starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y
        # calculate missile's velocity components
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        # create the missile
        super(Missile, self).__init__(image = Missile.image,
                                      x = x, y =y,
                                      dx = dx, dy = dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super(Missile, self).update()
        """Move the missile"""
        # if lifetime is up, destroy the missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

class Vocab(object):
    """Object that deals with vocab files"""
    current_guess = ""
    lines = []
    lines_len = 0
    word_choice = ""
    phrase = "Decode " + word_choice + " for Missiles: " + current_guess
    language = 0 # set to even for first language = question
                 # set to odd for first language = answer
    
    def __init__(self):
        try:
            vocab_file = open("vocab.txt.", "r")
        except IOError:
            print("No file called 'vocab.txt'. Please add 'vocab.txt'")
        
        self.lines = vocab_file.readlines()
        self.lines_len = len(self.lines)
        self.new_word()

    def new_word(self):
        word_line = (random.randrange(0, self.lines_len))/2 + self.language
        word_line = int(word_line)
        self.word_choice = self.lines[word_line]
        self.phrase = "Decode " + self.word_choice + " for Missiles: " + self.current_guess
        screen_guess = games.Text(value = self.phrase,
                                  size = 30,
                                  color = color.black,
                                  x = 30,
                                  y = games.screen.height-10)
        screen_guess.left = 5
        games.screen.add(screen_guess)

    def check(self):
        if self.current_guess == self.word_choice:
            Ship.ammo += 10
            self.new_word(Vocab)
        else:
            self.phrase = "Decode " + self.word_choice + " for Missiles: " + self.current_guess

class Game(object):
    """The game itself. """
    def __init__(self):
        """Initialize Game object. """
        # set level
        self.level = 0
        #load sound for level advance
        self.sound = games.load_sound("level.wav")
        #create score
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width -10,
                                is_collideable = False)
        games.screen.add(self.score)
        #create the player's ship
        self.ship = Ship(game = self,
                         x = games.screen.width/2,
                         y = games.screen.height/2)
        games.screen.add(self.ship)

    def play(self):
        """Play the game."""
        #begin theme music
        games.music.load("theme.mid")
        games.music.play(-1)
        #load and set background
        nebula_image = games.load_image("nebula.jpg")
        games.screen.background = nebula_image
        #advance to level 1
        self.advance()
        # start play
        games.screen.mainloop()

    def advance(self):
        """Advance to the next game level"""
        self.level += 1
        #create buffer zone around ship forbidding asteroid spawn points
        BUFFER = 150
        # create asteroids
        for i in range(self.level):
            # calculate an x and y at least BUFFER distance from the ship
            # choose minimum distance along x-axis and y-axis
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            # choose a distance along x-axis and y-axis based on minimum distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            # calculate location based on distance
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance
            # wrap around the screen if necessary
            x %= games.screen.width
            y %= games.screen.height
            # create the asteroid
            new_asteroid = Asteroid(game = self,
                                    x = x, y = y,
                                    size = Asteroid.LARGE)
            games.screen.add(new_asteroid)
        # display level number
        level_message = games.Message(value = "Level " + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.height/2,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)
        

        #play new level sound (except at first level
        if self.level > 1:
            self.sound.play()

    def end(self):
        """End the game"""
        # show game 'Game Over' for 5 seconds
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5*games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)        
            

def main():
    study = Vocab()
    astrocrash = Game()
    astrocrash.play()
    
#kick it off!
main()



              
