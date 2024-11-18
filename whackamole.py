import pygame
import random

def main():
	try:
		pygame.init()
		# You can draw the mole with this snippet:
		# screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
		mole_image = pygame.image.load("mole.png")
		screen = pygame.display.set_mode((640, 512))
		clock = pygame.time.Clock()
		mole_rect = mole_image.get_rect(topleft=(0,0))
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					if mole_rect.collidepoint(event.pos):
						mole_rect.topleft = (random.randrange(0, 640, 32), random.randrange(0, 512, 32))
			screen.fill("light green")
			screen.blit(mole_image, mole_rect.topleft)
			for i in range(0, 640, 32):
				x = i
				pygame.draw.line(screen, "black", (x, 0), (x, 512))
			for i in range(0, 512, 32):
				y = i
				pygame.draw.line(screen, "black", (0, y), (640, y))
			pygame.display.flip()
			clock.tick(60)
	finally:
		pygame.quit()


if __name__ == "__main__":
	main()