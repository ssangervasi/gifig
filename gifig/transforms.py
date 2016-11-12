def greyscale(gif):
    for frame in gif.frames:
        for rgb in frame:
            grey = sum(rgb)/len(rgb)
            frame.set_rgb(grey)


def warpbox(gif):
    frame = gif.frames[0]
    h, w = frame.shape
    top, bottom = h/3, (h*2)/3
    left, right = w/3, (w*2)/3
    while frame.has_next():
        next_frame = frame.next()
        bottom = min(h, bottom + 10)
        top = max(0, top - 10)
        frame.data[top:bottom, left:right] = (
            next_frame.data[top:bottom, left:right])
        frame = next_frame
