def on_overlap_tile(sprite, location):
    game.set_game_over_effect(False, effects.melt)
    game.set_game_over_message(False, "Coins: " + str(coin1))
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
        """),
    on_overlap_tile)

def on_a_pressed():
    if Kiwi.vy == 0:
        Kiwi.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite2, location2):
    global coin1
    coin1 += 1
    tiles.set_tile_at(location2, assets.tile("""
        transparency16
        """))
    coinText.set_text("Coins: " + str(coin1))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myCoinTile
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    global coin1
    coin1 += 100
    coinText.set_text("Coins: " + str(coin1))
    game.set_game_over_effect(True, effects.bubbles)
    game.set_game_over_message(True, "Coins: " + str(coin1))
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
        """),
    on_overlap_tile3)

coin1 = 0
coinText: TextSprite = None
Kiwi: Sprite = None
scene.set_background_color(9)
Kiwi = sprites.create(assets.image("""
    Kiwi
    """), SpriteKind.player)
controller.move_sprite(Kiwi, 100, 0)
Kiwi.ay = 170
scene.camera_follow_sprite(Kiwi)
tiles.set_current_tilemap(tilemap("""
    level1
    """))
coinText = textsprite.create("Coins: 0")
coinText.set_position(30, 10)
coinText.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)