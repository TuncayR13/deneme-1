import microbit
import random

# Yılanın başlangıç konumu
x = 2
y = 2

# Yılanın yönü
direction = "sağ"

# Puan
score = 0

# Yılanın uzunluğu
snake_length = 1

# Yılanın konumu
snake_positions = [(x, y)]

# Yem konumu
food_x = random.randint(0, 4)
food_y = random.randint(0, 4)

while True:
    # Yılanın yönünü değiştir
    if microbit.button_a.was_pressed():
        if direction != "sağ":
            direction = "sol"
    elif microbit.button_b.was_pressed():
        if direction != "sol":
            direction = "sağ"

    # Yılanın konumunu değiştir
    if direction == "sağ":
        x = (x + 1) % 5
    elif direction == "sol":
        x = (x - 1) % 5

    # Yılanın yeni konumu
    new_position = (x, y)

    # Yılanın uzunluğunu artır
    snake_positions.append(new_position)

    # Yılanın uzunluğu sabit tut
    if len(snake_positions) > snake_length:
        snake_positions.pop(0)

    # Yılanın yemle teması
    if new_position == (food_x, food_y):
        score += 1
        snake_length += 1
        food_x = random.randint(0, 4)
        food_y = random.randint(0, 4)

    # Yılanın kendiyle teması
    if new_position in snake_positions[:-1]:
        break

    # Ekranı güncelle
    microbit.display.clear()
    for pos in snake_positions:
        microbit.display.set_pixel(pos[0], pos[1], 9)
    microbit.display.set_pixel(food_x, food_y, 5)
    microbit.sleep(500)

# Oyun bitti
microbit.display.scroll("Oyun bitti! Puan: " + str(score))

