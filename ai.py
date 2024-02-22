from sprite import Sprite

def UpdateAIMovement(AI: Sprite, ball: Sprite, moveSpeed):
    if ball.myPos.y > AI.myPos.y + AI.rect.height/2:
        AI.changePos(0, moveSpeed)
    elif ball.myPos.y < AI.myPos.y + AI.rect.height/2:
        AI.changePos(0, -moveSpeed)