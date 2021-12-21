import colorsys

def get_colors_list(n):
    colors = []
    for i in range(n):
        rgb = colorsys.hsv_to_rgb(i/n, 1, 1)
        hsl = "".join("%02X" % round(i * 255) for i in rgb)
        colors.append(hsl)
    return colors

if __name__ == "__main__":
    print(get_colors_list(16))