telecom_major_colors = ['White', 'Red', 'Black', 'Yellow', 'Violet']
telecom_minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]


def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'


def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(telecom_minor_colors)
    if major_index >= len(telecom_major_colors):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(telecom_minor_colors)
    if minor_index >= len(telecom_minor_colors):
        raise Exception('Minor index out of range')
    return telecom_major_colors[major_index], telecom_minor_colors[minor_index]


def get_pair_number_from_color(major_color, minor_color):
    try:
        major_index = telecom_major_colors.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    try:
        minor_index = telecom_minor_colors.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    return major_index * len(telecom_minor_colors) + minor_index + 1
