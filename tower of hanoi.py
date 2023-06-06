import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Tower of Hanoi")
screen.tracer(0)

tower_positions = {'A': (-200, -100), 'B': (0, -100), 'C': (200, -100)}

def draw_disk(size, position):
    turtle.penup()
    turtle.goto(position[0] - size * 10, position[1])
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(size * 20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(size * 20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

def draw_peg(peg, disks):
    position = tower_positions[peg]
    for i, size in enumerate(disks, start=1):
        draw_disk(size, (position[0], position[1] + i * 20))

def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        tower_of_hanoi(n-1, source, auxiliary, target)

        screen.clear()
        draw_peg('A', [])
        draw_peg('B', [])
        draw_peg('C', [])

        disk_to_move = disks[source].pop()
        disks[target].append(disk_to_move)
        
        draw_peg(source, disks[source])
        draw_peg(target, disks[target])
        draw_peg(auxiliary, disks[auxiliary])
        screen.update()

        tower_of_hanoi(n-1, auxiliary, target, source)


n = 4
disks = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
tower_of_hanoi(n, 'A', 'C', 'B')
turtle.done()
