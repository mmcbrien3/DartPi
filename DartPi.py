import pygame, numpy, math, random
import matplotlib.pyplot as plt
pi = math.pi
unitLength = 200
bgColor = 0x111111
circleColor = 0x1111ff
dartColor = 0xff1111
###################################
totalThrows = 100000

def run_simulation():
    pygame.init()
    pygame.font.init()
    piFont = pygame.font.SysFont('Courier', 10)
    screen = pygame.display.set_mode([unitLength * 2, unitLength * 2])
    pygame.display.set_caption("DartPi")

    throws = 0
    totalHits = 0
    draw_background(screen)
    estimates = numpy.zeros(totalThrows)
    while throws < totalThrows:
        throws += 1
        pos = get_random_position()
        draw_dart(pos, screen)
        hit = is_hit(pos)
        if hit:
            totalHits += 1
        draw_text(estimate_pi(totalHits, throws), piFont, screen)
        estimates[throws - 1] = estimate_pi(totalHits, throws)
        pygame.display.update()
        draw_background(screen)

    print(totalHits/totalThrows * 4)
    plt.plot(estimates)
    plt.plot([pi] * totalThrows)
    plt.xlabel("Number of Throws")
    plt.ylabel("Estimate of Pi")
    plt.show()

def get_random_position():
    x = random.randint(0, unitLength * 2)
    y = random.randint(0, unitLength * 2)
    return (x, y)

def estimate_pi(hits, throws):
    return (hits / throws) * 4

def draw_dart(position, screen):
    pygame.draw.circle(screen, dartColor, position, round(unitLength/100), 0)

def draw_text(estimate, piFont, screen):
    t = piFont.render("Pi: %s" % estimate, False, (255, 255, 255))
    screen.blit(t, (0,0))

def is_hit(position):
    dist_to_center = math.sqrt( (position[0] - unitLength) ** 2 + (position[1] - unitLength) ** 2)
    if dist_to_center < unitLength:
        return True
    return False

def draw_background(screen):
    screen.fill(bgColor)
    pygame.draw.circle(screen, circleColor, (unitLength, unitLength), unitLength, round(unitLength/100))

if __name__ == "__main__":
    run_simulation()