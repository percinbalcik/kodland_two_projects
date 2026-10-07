import random

WIDTH = 700
HEIGHT = 500

TITLE = "Fruit Collector"


# Oyuncuyu oluşturuyoruz
player = Actor("player")
player.pos = (350, 420)

# Meyveyi oluşturuyoruz
fruit = Actor("fruit")
fruit.pos = (
    random.randint(50, 650),
    random.randint(50, 350)
)

# Düşmanları tutacağımız liste
enemies = []

for i in range(2):
    enemy = Actor("enemy")

    enemy.pos = (
        random.randint(50, 650),
        random.randint(80, 300)
    )

    enemy.speed = random.choice([-3, -2, 2, 3])

    enemies.append(enemy)


score = 0
lives = 3
game_over = False
win = False


def draw():
    screen.clear()
    screen.fill((190, 230, 180))

    if game_over:
        screen.draw.text(
            "GAME OVER",
            center=(350, 210),
            fontsize=60,
            color="red"
        )

        screen.draw.text(
            "Score: " + str(score),
            center=(350, 280),
            fontsize=35,
            color="black"
        )

    elif win:
        screen.draw.text(
            "YOU WIN!",
            center=(350, 210),
            fontsize=60,
            color="green"
        )

        screen.draw.text(
            "You collected 10 fruits!",
            center=(350, 280),
            fontsize=30,
            color="black"
        )

    else:
        player.draw()
        fruit.draw()

        for enemy in enemies:
            enemy.draw()

        screen.draw.text(
            "Score: " + str(score),
            (20, 20),
            fontsize=30,
            color="black"
        )

        screen.draw.text(
            "Lives: " + str(lives),
            (590, 20),
            fontsize=30,
            color="black"
        )


def update():
    global score, lives
    global game_over, win

    if game_over or win:
        return

    move_player()
    move_enemies()

    # Oyuncu meyveye dokundu mu?
    if player.colliderect(fruit):
        score += 1

        fruit.pos = (
            random.randint(50, 650),
            random.randint(50, 350)
        )

    # Oyuncu düşmana dokundu mu?
    for enemy in enemies:

        if player.colliderect(enemy):
            lives -= 1

            # Oyuncuyu başlangıç konumuna döndür
            player.pos = (350, 420)

            # Düşmanın konumunu değiştir
            enemy.pos = (
                random.randint(50, 650),
                random.randint(80, 300)
            )

            break

    if score >= 10:
        win = True

    if lives <= 0:
        game_over = True


def move_player():

    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5

    if keyboard.up:
        player.y -= 5

    if keyboard.down:
        player.y += 5

    # Oyuncunun ekran dışına çıkmasını engelle
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    if player.top < 0:
        player.top = 0

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT


def move_enemies():

    for enemy in enemies:

        enemy.x += enemy.speed

        # Düşman sağ veya sol kenara çarparsa
        # hareket yönünü değiştiriyoruz
        if enemy.right >= WIDTH or enemy.left <= 0:
            enemy.speed *= -1