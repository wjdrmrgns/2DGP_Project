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
        self.spear = load_image('will spear.png')
        self.weapon_spear_1 = load_image('spear.png')
        self.shortsword = load_image('will shortsword.png')
        self.weapon_shortsword_1 = load_image('shortsword.png')


    def update(self):
        global move

        runpoint = 1
        if map_change == 1:
            runpoint = 1
        elif map_change == -1:
            runpoint = 2



        if move <= 4:
            self.frame = (self.frame + 1) % 8
        elif move <= 8:
            self.frame = (self.frame + 1) % 10
        elif move <= 12:
            self.frame = (self.frame + 1) % 24

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
        global attackcheck
        global move
        # global weapon_change

        # 공격시 프레임 초기화
        if attackcheck == 1:
            self.frame = 0
            attackcheck = 0

        # 공격 끝날 때 프레임 초기화
        framecontrol = 0
        if weapon_change == 0:
            framecontrol = 0
        elif weapon_change == 1:
            framecontrol = 5

        if self.frame == 23 - framecontrol:
            attackcheck = 0
            self.frame = 0
            if move == 9:
                move = 5
            elif move == 10:
                move = 6
            elif move == 11:
                move = 7
            elif move == 12:
                move = 8

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
            elif move == 9:
                if weapon_change == 0:
                    self.weapon_spear_1.clip_draw(self.frame * 130, 0, 130, 132, self.x - 2, self.y + 11)
                    self.spear.clip_draw(self.frame * 258, 0, 258, 260, self.x, self.y)
                elif weapon_change == 1:
                    self.shortsword.clip_draw(self.frame * 130, 0, 130, 132,self.x,self.y)
                    self.weapon_shortsword_1.clip_draw(self.frame * 130, 0, 130, 132, self.x, self.y)
            elif move == 10:
                if weapon_change == 0:
                    self.weapon_spear_1.clip_draw(self.frame * 130, 132, 130, 132, self.x + 5, self.y - 11)
                    self.spear.clip_draw(self.frame * 258, 260, 258,260, self.x, self.y)
                elif weapon_change == 1:
                    self.shortsword.clip_draw(self.frame * 130, 132, 130, 132,self.x,self.y)
                    self.weapon_shortsword_1.clip_draw(self.frame * 130, 132, 130, 132, self.x, self.y)
            elif move == 11:
                if weapon_change == 0:
                    self.weapon_spear_1.clip_draw(self.frame * 130, 264, 130, 132, self.x - 18, self.y)
                    self.spear.clip_draw(self.frame * 258, 520, 258, 260, self.x, self.y)
                elif weapon_change == 1:
                    self.shortsword.clip_draw(self.frame * 130, 264, 130, 132,self.x,self.y)
                    self.weapon_shortsword_1.clip_draw(self.frame * 130, 264, 130, 132, self.x, self.y)
            elif move == 12:
                if weapon_change == 0:
                    self.weapon_spear_1.clip_draw(self.frame * 130, 392, 130, 132, self.x + 18, self.y - 2)
                    self.spear.clip_draw(self.frame * 258, 780, 258, 260, self.x, self.y)
                elif weapon_change == 1:
                    self.shortsword.clip_draw(self.frame * 130, 396, 130, 132,self.x,self.y)
                    self.weapon_shortsword_1.clip_draw(self.frame * 130, 396, 130, 132, self.x, self.y)

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
    global attackcheck
    global weapon_change
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
            elif event.key == SDLK_a:
                if move == 1 or move == 5:
                    move = 9
                elif move == 2 or move == 6:
                    move = 10
                elif move == 3 or move == 7:
                    move = 11
                elif move == 4 or move == 8:
                    move = 12
                attackcheck = 1
            elif event.key == SDLK_f:
                weapon_change = (weapon_change + 1) % 3

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
map_change = -1
weapon_change = 0
attackcheck = 0
c_x, c_y = 400, 400
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
