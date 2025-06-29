#给定两个方形区域,用bottomLeft 和 topRight表示,求出他们相交区域的长和宽
#注意,相交为线也返回 0,0
def get_intersection_size(bottomLeft1, topRight1, bottomLeft2, topRight2):
    # Step 1: Find the bottom left corner of the intersection
    x1, y1 = bottomLeft1
    x2, y2 = bottomLeft2
    bottom_left_x = max(x1, x2)
    bottom_left_y = max(y1, y2)

    # Step 2: Find the top right corner of the intersection
    x3, y3 = topRight1
    x4, y4 = topRight2
    top_right_x = min(x3, x4)
    top_right_y = min(y3, y4)

    # Step 3: Check if there is an intersection
    if bottom_left_x >= top_right_x or bottom_left_y >= top_right_y:
        return 0, 0  # No intersection

    # Step 4: Calculate the width and height of the intersection
    width = top_right_x - bottom_left_x
    height = top_right_y - bottom_left_y
    return width, height

#变体:  返回相交的区域,依然用bottomLeft 和 topRight表示,   无重合返回 None(包括线重合)
def get_intersection(bottomLeft1, topRight1, bottomLeft2, topRight2):
    # Step 1: Extract coordinates
    x1, y1 = bottomLeft1
    x2, y2 = topRight1
    x3, y3 = bottomLeft2
    x4, y4 = topRight2

    # Step 2: Find the intersection corners
    intersection_x1 = max(x1, x3)
    intersection_y1 = max(y1, y3)
    intersection_x2 = min(x2, x4)
    intersection_y2 = min(y2, y4)

    # Step 3: Check if there is an intersection
    if intersection_x1 < intersection_x2 and intersection_y1 < intersection_y2:
        # There is an intersection, return the bottomLeft and topRight of the intersection
        intersection_bottomLeft = (intersection_x1, intersection_y1)
        intersection_topRight = (intersection_x2, intersection_y2)
        return intersection_bottomLeft, intersection_topRight
    else:
        # No intersection
        return None