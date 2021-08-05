import pygame, random
import os
import time
from pygame import time as T

WIDTH = 1285
HEIGHT = 674
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ALIEN VERSUS BALLOON")
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(os.path.join("assets", "NAVE.png"))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centery = HEIGHT// 2
		self.rect.right = WIDTH
		self.speed_x = 0
		self.shield = 100

	def update(self):
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_UP]:
			self.speed_y = -5
		if keystate[pygame.K_DOWN]:
			self.speed_y = 5
		self.rect.y += self.speed_y
		if self.rect.bottom >= HEIGHT:
			self.rect.bottom = HEIGHT
		if self.rect.top <= 0:
			self.rect.top = 0

	def shoot(self):
		bullet = Bullet(self.rect.centerx - 75 , self.rect.bottom - 50)
		all_sprites.add(bullet)
		bullets.add(bullet)
		laser_sound.play()

class Globos(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(Globos_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - 450)
		self.rect.y = self.rect.bottom + 425
		self.speedy = random.randrange(1, 3)

	def update(self):
		self.rect.y -= self.speedy
		if self.rect.bottom < 0:
			self.rect.top =HEIGHT

class Globos2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(os.path.join("assets", "Globoazul.png"))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - 450)
		self.rect.y = self.rect.bottom + 425
		self.speedy = random.randrange(7, 9)

	def update(self):
		self.rect.y -= self.speedy
		if self.rect.bottom < 0:
			self.rect.top =HEIGHT

class Globos3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(os.path.join("assets", "GloboRojo.png"))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - 450)
		self.rect.y = self.rect.bottom + 425
		self.speedy = random.randrange(6, 7)

	def update(self):
		self.rect.y -= self.speedy
		if self.rect.bottom < 0:
			self.rect.top =HEIGHT

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/laser1.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10
	
	def update(self):
		self.rect.x += self.speedy
		if self.rect.bottom < 0:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center 
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 60 # VELOCIDAD DE LA EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

class Explosion2(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center 
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 20 # VELOCIDAD DE LA EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center


def show_go_screen():
	screen.blit(background, [0,0])
	draw_text(screen, "ALIEN VERSUS BALLOON", 65, WIDTH // 2, HEIGHT // 4)
	draw_text(screen, "Preciona ESPACIO para continuar", 20, WIDTH // 2, HEIGHT * 3/4)
	pygame.display.flip()
	waiting = True
	while waiting:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
    					waiting = False
			


Globos_images = []
Globos_list = ["GloboAmarillo.png", "GloboMorado.png","GloboNaranja.png","GloboVerde.png"]
for img in Globos_list:
	Globos_images.append(pygame.image.load(os.path.join("assets", img)))


####----------------EXPLOSTION IMAGENES --------------
explosion_anim = []
for i in range(9):
	file = "assets/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70,70))
	explosion_anim.append(img_scale)

# Cargar imagen de fondo
background = pygame.image.load("assets/LAND.png").convert()

# Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/laser5.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("assets/music.ogg")
pygame.mixer.music.set_volume(0.2)


pygame.mixer.music.play(loops=-1)

def pausa():
    
	screen.blit(background, [0,0])
	draw_text(screen, "Pausa", 65, WIDTH // 2, HEIGHT // 4)
	draw_text(screen, "Presiona P para seguir jugando", 27, WIDTH // 2, HEIGHT // 2)
	draw_text(screen, "Presiona Q para salir del juego", 27, WIDTH // 2, 400)
	pygame.display.flip()

	pausa = True

	while pausa:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p: #Quitar la Pausa
					pausa = False
				elif event.key == pygame.K_q: #Salir del juego
					pygame.quit()
					quit()

	pygame.display.update()



#Presentacion Timer

Fuente = pygame.font.SysFont("Arial",30)

#### ----------GAME OVER
game_over = False
Menu = True
running = True
Win = False
aux = 10

while running:
	
	if Menu:
    	
		game_over = False
		Win = False
		show_go_screen()
		Menu = False
		all_sprites = pygame.sprite.Group()
		Globos_list = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		Globos_Azules = pygame.sprite.Group()
		Globos_Rojos = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)
		for i in range(10):
			globos = Globos()
			all_sprites.add(globos)
			Globos_list.add(globos)
		
		for i in range(1):
			globos2 = Globos2()
			all_sprites.add(globos2)
			Globos_Azules.add(globos2)
		
		for i in range(1):
			globos3 = Globos3()
			all_sprites.add(globos3)
			Globos_Rojos.add(globos3)
				
				
		score = 10
	
	if Menu == False:
		Tiempo = T.get_ticks()//1000

	if game_over:
    	
		screen.blit(background, [0,0])
		draw_text(screen, "GAME OVER", 65, WIDTH // 2, HEIGHT // 4)
		draw_text(screen, "Presiona la tecla X para continuar", 27, WIDTH // 2, HEIGHT // 2)
		pygame.display.flip()
		Tiempo = 0
		over = True
		while over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_x:		
						over = False
						Menu = True
		pygame.display.update()

	
	if Win:
		screen.blit(background, [0,0])
		draw_text(screen, "YOU WIN", 65, WIDTH // 2, HEIGHT // 4)
		draw_text(screen, "Presiona la tecla X para continuar", 27, WIDTH // 2, HEIGHT // 2)
		pygame.display.flip()
		Win2 = True
		while Win2:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_x:		
						Win2 = False
						Menu = True
		pygame.display.update()

	
	if Tiempo == aux:
		aux += 10
		score -= 5

	if score >= 500:
		Win = True

	if score <= 0:
		game_over = True

	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_ESCAPE]:
		pausa()
	

	if player.rect.bottom >= HEIGHT:
		explosion2 = Explosion2(player.rect.center)
		all_sprites.add(explosion2)
		explosion_sound.play()		
		game_over = True
	if player.rect.top <= 0:
		explosion2 = Explosion2(player.rect.center)
		all_sprites.add(explosion2)
		explosion_sound.play()
		game_over = True

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()


	all_sprites.update()

	#colisiones - Globoso - laser
	hits = pygame.sprite.groupcollide(Globos_list, bullets, True, True)
	for hit in hits:
		score += 1
		explosion_sound.play()
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)
		globos = Globos()
		all_sprites.add(globos)
		Globos_list.add(globos)
	
	hits = pygame.sprite.groupcollide(Globos_Azules, bullets, True, True)
	for hit in hits:
		score += 10
		explosion_sound.play()
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)
		globos2 = Globos2()
		all_sprites.add(globos2)
		Globos_Azules.add(globos2)

	hits = pygame.sprite.groupcollide(Globos_Rojos, bullets, True, True)
	for hit in hits:
		score -= 3
		explosion_sound.play()
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)
		globos3 = Globos3()
		all_sprites.add(globos3)
		Globos_Rojos.add(globos3)


	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	draw_text(screen,"Time: " +str(Tiempo), 35, WIDTH - 300, 10)

	#Marcador
	draw_text(screen,"Helio: "+str(score), 35, 100, 10)

	pygame.display.flip()
pygame.quit()
