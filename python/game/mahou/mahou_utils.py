import os, pygame, math
#Lerp between two rgb 3-tuples
# 0 <= t <= 1 
def color_lerp(color1, color2, t):
    r1 = color1[0]
    g1 = color1[1]
    b1 = color1[2]

    r2 = color2[0]
    g2 = color2[1]
    b2 = color2[2]

    return (r1 + (r2 - r1) * t, g1 + (g2 - g1) * t, b1 + (b2 - b1) * t)

def load_image(name):
   fullname = os.path.join('data/', name)
   image = pygame.image.load(fullname)
   image = image.convert()
   return image, image.get_rect()

#Rotate an image around its center point.
# Angle in degress
def rotate_center(image, rect, angle):
    image_r = pygame.transform.rotate(image, angle)
    rect_r = image_r.get_rect(center=rect.center)
    return image_r, rect_r

#Determing the counterclockwise angle of rotation required for an entity at point1
# to face point2.
#Assume entity is initially facing downwards
#Returns angle in radians
def determine_angle(point1, point2):
        x_diff = point2[0] - point1[0]
        y_diff = point2[1] - point1[1]

        theta_rot = 0
        if x_diff == 0:
            if y_diff >= 0:
                theta_rot = 0
            else:
                theta_rot = math.pi
        elif y_diff == 0:
            if x_diff >= 0:
                theta_rot = math.pi / 2
            else:
                theta_rot = 3 / 2 * math.pi
        elif x_diff > 0 and y_diff > 0:
            theta_radians = math.atan(x_diff/y_diff)
            theta_rot = theta_radians
        elif x_diff > 0 and y_diff < 0:
            theta_radians = math.atan(abs(y_diff)/x_diff)
            theta_rot = theta_radians + math.pi / 2
        elif x_diff < 0 and y_diff < 0:
            theta_radians = math.atan(x_diff/y_diff)
            theta_rot = theta_radians + math.pi
        elif x_diff < 0 and y_diff > 0:
            theta_radians = math.atan(y_diff/abs(x_diff))
            theta_rot = theta_radians + 3 / 2 * math.pi

        return theta_rot

#Rectangle collision detection
#Note: just for practice. In real code use pygame.sprite.collide_rect(left,right)
def is_collision(sprite1, sprite2):
    rect1 = sprite1.rect
    rect2 = sprite2.rect

    if (rect1.x < rect2.x + rect2.w and \
        rect1.x + rect1.w > rect2.x and \
        rect1.y < rect2.y + rect2.h and \
        rect1.y + rect1.h > rect2.y):
        return True
    else:
        return False     
