def colors_not_in_list(color_list_1, color_list_2):
    return color_list_1 - color_list_2

print(colors_not_in_list(set(["White", "Black", "Red"]), set(["Red", "Green"])))
