def on_left_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        assets.animation("""
            skeleton left
        """),
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    pass
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    pass
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        assets.animation("""
            skeleton right
        """),
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    global mySprite2
    info.start_countdown(5)
    info.change_score_by(1)
    mySprite2.destroy()
    mySprite2 = sprites.create(assets.image("""
        soul basic 2
    """), SpriteKind.food)
    animation.run_image_animation(mySprite2, assets.animation("""
        soul
    """), 100, True)
    mySprite2.set_position(randint(0, 155), randint(0, 115))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

mySprite2: Sprite = None
mySprite: Sprite = None
info.set_score(0)
mySprite = sprites.create(assets.image("""
    skeleton basic
"""), SpriteKind.player)
controller.move_sprite(mySprite, 80, 80)
mySprite.set_stay_in_screen(True)
scene.set_background_image(assets.image("""
    background
"""))
info.start_countdown(4)
mySprite2 = sprites.create(assets.image("""
    soul basic
"""), SpriteKind.food)

def on_forever():
    pass
forever(on_forever)
