controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    animation.runImageAnimation(
    mySprite,
    assets.animation`skeleton left`,
    200,
    true
    )
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
	
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
	
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    animation.runImageAnimation(
    mySprite,
    assets.animation`skeleton right`,
    200,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.startCountdown(5)
    info.changeScoreBy(1)
    mySprite2.destroy()
    mySprite2 = sprites.create(assets.image`soul basic 2`, SpriteKind.Food)
    animation.runImageAnimation(
    mySprite2,
    assets.animation`soul`,
    100,
    true
    )
    mySprite2.setPosition(randint(5, 155), randint(5, 115))
})
let mySprite2: Sprite = null
let mySprite: Sprite = null
info.setScore(0)
mySprite = sprites.create(assets.image`skeleton basic`, SpriteKind.Player)
controller.moveSprite(mySprite, 80, 80)
mySprite.setStayInScreen(true)
scene.setBackgroundImage(assets.image`background`)
info.startCountdown(4)
mySprite2 = sprites.create(assets.image`soul basic`, SpriteKind.Food)
forever(function () {
	
})
