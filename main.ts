scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    game.setGameOverEffect(false, effects.melt)
    game.setGameOverMessage(false, "Coins: " + ("" + coin1))
    game.gameOver(false)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Kiwi.vy == 0) {
        Kiwi.vy = -150
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile3`, function (sprite3, location3) {
    coin1 += 100
    coinText.setText("Coins: " + ("" + coin1))
    game.setGameOverEffect(true, effects.bubbles)
    game.setGameOverMessage(true, "Coins: " + ("" + coin1))
    game.gameOver(true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myCoinTile`, function (sprite2, location2) {
    coin1 += 1
    tiles.setTileAt(location2, assets.tile`transparency16`)
    coinText.setText("Coins: " + ("" + coin1))
})
let coin1 = 0
let coinText: TextSprite = null
let Kiwi: Sprite = null
scene.setBackgroundColor(9)
Kiwi = sprites.create(assets.image`Kiwi`, SpriteKind.Player)
controller.moveSprite(Kiwi, 100, 0)
Kiwi.ay = 170
scene.cameraFollowSprite(Kiwi)
tiles.setCurrentTilemap(tilemap`level1`)
coinText = textsprite.create("Coins: 0")
coinText.setPosition(30, 10)
coinText.setFlag(SpriteFlag.RelativeToCamera, true)
