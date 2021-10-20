from pico2d import *

class Map_shop:
    def __init__(self):
        self.frame = 0
        self.x,self.y = 200,300
        self.dg_x, self.dg_y = 800, 300
        self.dgdoor_x, self.dgdoor_y = 800, 450
        self.bed_x, self.bed_y = self.x + 75, self.y + 115
        self.door_x, self.door_y = self.x + 26, self.y - 154
        self.doorhatch_x, self.doorhatch_y = self.x + 25,self.y - 154
        self.table_x, self.table_y = self.x - 40, self.y + 100
        self.shoptable_x, self.shoptable_y = self.x - 75, self.y - 110
        self.sell_x, self.sell_y = self.x + 50, self.y - 75

        self.image = load_image('shop.png')
        self.bed = load_image('bed.png')
        self.door = load_image('door.png')
        self.doorhatch = load_image('doorhatch.png')
        self.object = load_image('object.png')
        self.dg = load_image('dg.png')
        self.dgback = load_image('dgback.png')
        self.dgdoor = load_image('dgdoor.png')

    def update(self):
        self.frame = (self.frame + 1) % 11
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 340, 436,self.x,self.y)
        self.bed.clip_draw(0,0,128,128,self.bed_x, self.bed_y)
        self.door.clip_draw(0,0,152,120,self.door_x, self.door_y)
        self.doorhatch.clip_draw(0,0,152,120,self.doorhatch_x, self.doorhatch_y)
        self.object.clip_draw(118,0,24,68,self.table_x,self.table_y)
        self.object.clip_draw(145,40,26,36,self.shoptable_x + 26, self.shoptable_y + 22)
        self.object.clip_draw(145, 40, 26, 36, self.shoptable_x, self.shoptable_y + 22)
        self.object.clip_draw(145, 40, 26, 36, self.shoptable_x + 26, self.shoptable_y)
        self.object.clip_draw(145, 40, 26, 36, self.shoptable_x, self.shoptable_y)
        self.object.clip_draw(0,0,100,40,self.sell_x, self.sell_y)
        self.dg.clip_draw(0,0,1024,1024,self.dg_x, self.dg_y)
        self.dgback.clip_draw(0,0,1024,1024,self.dg_x, self.dg_y)
        self.dgdoor.clip_draw(self.frame * 130,0,128,128,self.dgdoor_x, self.dgdoor_y)

class character_move:
    def __init__(self):
        self.x, self.y = 400,400
        self.frame = 0

        self.run = load_image('will run.png')
        self.stand_dg = load_image('will stand dg.png')
        self.walk = load_image('will walk.png')
        self.stand = load_image('will stand.png')

    def update(self):
        global move
        runpoint = 1
        if map_change == 1:
            runpoint = 1
        elif map_change == -1:
            runpoint = 2

        if move <= 4:
            self.frame = (self.frame + 1) % 8
        else:
            self.frame = (self.frame + 1) % 10
        if move == 1:
            self.y += 5 * runpoint
        elif move == 2:
            self.y -= 5 * runpoint
        elif move == 3:
            self.x -= 5 * runpoint
        elif move == 4:
            self.x += 5 * runpoint

    def draw(self):
        global map_change
        if self.x == 200 and self.y == 400:
            self.x = 1000
            map_change *= -1
        if map_change == -1:
            if move == 1:
                self.run.clip_draw(self.frame * 130, 0, 130, 130, self.x, self.y)
            elif move == 2:
                self.run.clip_draw(self.frame * 130, 132, 130, 130, self.x, self.y)
            elif move == 3:
                self.run.clip_draw(self.frame * 130, 264, 130, 130, self.x, self.y)
            elif move == 4:
                self.run.clip_draw(self.frame * 130, 396, 130, 130, self.x, self.y)
            elif move == 5:
                self.stand_dg.clip_draw(260, 0, 130,130, self.x, self.y)
            elif move == 6:
                self.stand_dg.clip_draw(390, 0, 130,130, self.x, self.y)
            elif move == 7:
                self.stand_dg.clip_draw(130, 0, 130,130, self.x, self.y)
            elif move == 8:
                self.stand_dg.clip_draw(0, 0, 130,130, self.x, self.y)


        elif map_change == 1:
            if move == 1:
                self.walk.clip_draw(self.frame * 130, 0, 130, 130, self.x, self.y)
            elif move == 2:
                self.walk.clip_draw(self.frame * 130, 132, 130, 130, self.x, self.y)
            elif move == 3:
                self.walk.clip_draw(self.frame * 130, 264, 130, 130, self.x, self.y)
            elif move == 4:
                self.walk.clip_draw(self.frame * 130, 396, 130, 130, self.x, self.y)
            elif move == 5:
                self.stand.clip_draw(self.frame * 130, 396, 130,130, self.x, self.y)
            elif move == 6:
                self.stand.clip_draw(self.frame * 130, 264, 130,130, self.x, self.y)
            elif move == 7:
                self.stand.clip_draw(self.frame * 130, 132, 130,130, self.x, self.y)
            elif move == 8:
                self.stand.clip_draw(self.frame * 130, 0, 130,130, self.x, self.y)

def handle_events():
    global running
    global move
    global will
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                move = 3
            elif event.key == SDLK_RIGHT:
                move = 4
            elif event.key == SDLK_UP:
                move = 1
            elif event.key == SDLK_DOWN:
                move = 2
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                move = 7
            elif event.key == SDLK_RIGHT:
                move = 8
            elif event.key == SDLK_UP:
                move = 5
            elif event.key == SDLK_DOWN:
                move = 6

open_canvas(1200, 600)
move = 0
map_change = 1
will = character_move()
shop = Map_shop()
running = True

while running:
    handle_events()
    shop.update()
    will.update()

    clear_canvas()
    shop.draw()
    will.draw()

    update_canvas()
    delay(0.1)
