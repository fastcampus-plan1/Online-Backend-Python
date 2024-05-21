import math


def calculate_rectangle_area(width,height):
    """사각형의 면적을 계산합니다."""
    return width * height


def calculate_elipse_area(width, height ):
    """타원의 면적을 계산합니다."""
    return math.pi* (width    /2) *(height/ 2)


def get_shape_area(shape_type, width, height = None):
    """도형의 종류와 매개변수에 따라 면적을 계산합니다.
    Returns:
        float: 계산된 면적, 또는 None (지원되지 않는 도형의 경우)
    """
    if shape_type== "rectangle":
        return calculate_rectangle_area(width, height)
    elif shape_type == 'circle' or shape_type == "elipse":
        if height is None:
            return calculate_elipse_area(width,width)
        return calculate_elipse_area(width,height)
    else:
        print(f"지원되지 않는 도형입니다: {shape_type}")
        return None
