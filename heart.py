# pyright: reportMissingImports=false
import math
import random
from pathlib import Path

import pygame  # type: ignore


WIDTH, HEIGHT = 900, 700
FPS = 60
SCALE = 15
BACKGROUND = (0, 0, 0)
WORDS = ["I Love You", "Love You", "LOVE YOU", "love you"]
BLUE_COLORS = [(25, 105, 210), (30, 144, 255), (0, 170, 255), (80, 190, 255)]


class TextParticle:
    def __init__(self, x: float, y: float, word: str, font: pygame.font.Font):
        self.x = round(x)
        self.y = round(y)
        self.word = word
        self.font = font
        self.color = random.choice(BLUE_COLORS)
        self.phase = random.uniform(0, math.tau)
        self.alpha = random.randint(150, 255)


def heart_point(t: float) -> tuple[float, float]:
    """Return a point on the outline of a mathematical heart."""
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, -y


def make_particles(font: pygame.font.Font) -> list[TextParticle]:
    particles = []
    # Place words around the outline; skip nearby points to keep the shape readable.
    min_distance = 27
    for i in range(260):
        t = math.tau * i / 260
        x, y = heart_point(t)
        sx = WIDTH / 2 + x * SCALE
        sy = HEIGHT / 2 + y * SCALE
        if any(math.hypot(sx - p.x, sy - p.y) < min_distance for p in particles):
            continue
        particles.append(TextParticle(sx, sy, random.choice(WORDS), font))
    return particles


def draw_glowing_text(screen: pygame.Surface, particle: TextParticle, tick: int) -> None:
    pulse = 0.72 + 0.28 * (0.5 + 0.5 * math.sin(tick * 0.045 + particle.phase))
    alpha = int(particle.alpha * pulse)
    text = particle.font.render(particle.word, True, particle.color)
    text.set_alpha(alpha)
    rect = text.get_rect(center=(particle.x, particle.y))

    glow = pygame.transform.smoothscale(
        text, (max(1, int(text.get_width() * 1.8)), max(1, int(text.get_height() * 1.8)))
    )
    glow.set_alpha(alpha // 4)
    screen.blit(glow, glow.get_rect(center=rect.center))
    screen.blit(text, rect)


def main() -> None:
    pygame.init()
    try:
        pygame.mixer.init()
        music_path = Path(__file__).with_name("love_you.mp3")
        if music_path.exists():
            pygame.mixer.music.load(str(music_path))
            pygame.mixer.music.play(-1)
    except pygame.error as error:
        print(f"Ses başlatılamadı: {error}")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Love You - Heart")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 15, bold=True)
    particles = make_particles(font)
    running = True
    tick = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        screen.fill(BACKGROUND)
        for particle in particles:
            draw_glowing_text(screen, particle, tick)
        pygame.display.flip()
        clock.tick(FPS)
        tick += 1

    pygame.quit()


if __name__ == "__main__":
    main()
