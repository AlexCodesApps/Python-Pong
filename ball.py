from sprite import Sprite

def UpdatePhysics(ball: Sprite, window_width, window_height, speed, yspeed, paddle: Sprite, paddle2: Sprite):
    over = False
    if ball.myPos.x < 80:
        speed = abs(speed)
        if not (paddle.myPos.y < ball.myPos.y < paddle.myPos.y + paddle.rect.height):
            over = True
    elif ball.myPos.x > window_width - 110:
        speed = - abs(speed)
        if not (paddle.myPos.y < ball.myPos.y < paddle.myPos.y + paddle.rect.height):
            over = True
    if ball.myPos.y < ball.rect.height:
        yspeed = abs(yspeed)
    elif ball.myPos.y > window_height - ball.rect.height:
        yspeed = - abs(yspeed)
    ball.changePos(speed, yspeed)
    return speed, yspeed, over
