# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER

def Teleport():
    agent.teleport_to_player()
player.on_chat("come", Teleport)


def Forward(steps):
    agent.move(FORWARD, steps)
player.on_chat("forward", Forward)

def Back(steps):
    agent.move(BACK, steps)
player.on_chat("back", Back)

def Left(steps):
    agent.move(LEFT, steps)
player.on_chat("left", Left)

def Right(steps):
    agent.move(RIGHT, steps)
player.on_chat("right", Right)

def Up(steps):
    agent.move(UP, steps)
player.on_chat("up", Up)

def Down(steps):
    agent.move(DOWN, steps)
player.on_chat("down", Down)

def TurnLeft():
    agent.turn(LEFT)
player.on_chat("tl", TurnLeft)

def TurnRight():
    agent.turn(RIGHT)
player.on_chat("tr", TurnRight)


def course():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    for i in range(2):
        agent.move(UP, 1)
        agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 3)
    for i in range(2):
        agent.move(DOWN, 1)
        agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
player.on_chat("course", course)


def chat():
    for i in range(5):
        agent.move(FORWARD, i)
player.on_chat("say", chat)


def tree(num1):
    for i in range(num1):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, num1)
    agent.collect_all()
player.on_chat("chop", tree)

def stone(num2):
    for i in range(num2):
        agent.destroy(DOWN)
        agent.move(FORWARD, 1)
player.on_chat("break", stone)

def bulldozer(num, num3):
    for i in range(num3):
        for j in range(num):
            agent.destroy(DOWN)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.destroy(FORWARD)
            agent.collect_all()
            agent.move(FORWARD, 1)
        agent.move(BACK, num)
        agent.move(DOWN, 1)

player.on_chat("destroy", bulldozer)

# def wall(num5, num6):
#     for i in range(num5):
#         agent.move(UP, 1)
#         for i in range(num6):
#             # agent.place(DOWN, 1)
#             agent.move(FORWARD, 1)
# player.on_chat("wall", wall)

# def house_wall(width, height):
#     for i in range(width):
#         agent.move(UP, 1)
#         for j in range(height):
#             agent.place(DOWN)
#             agent.move(FORWARD, 1)
#         agent.move(BACK, width)

# player.on_chat("hw", house_wall)

def build_wall(height, width):
    for j in range(width):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP, 1)
        agent.move(DOWN, height)
        agent.move(RIGHT, 1)
player.on_chat("bw", build_wall)

def pillar(height):
    for i in range(height):
        agent.place(FORWARD)
        agent.move(UP, 1)
player.on_chat("pillar", pillar)

def roof(height, width):
    for i in range(width):
        for j in range(height):
            agent.place(DOWN)
            agent.move(UP, 1)
        agent.move(RIGHT, 1)
        agent.move(DOWN, height)
player.on_chat("roof", roof)

def layer(width):
    for i in range(width):
        agent.place(DOWN)
        agent.move(RIGHT, 1)
player.on_chat("build", layer)

def dig_down():
    while agent.detect(AgentDetection.BLOCK, DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        agent.collect_all()
player.on_chat("dig", dig_down)

def bridge(length, width):
    for j in range(width):
        for i in range(length):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
    agent.move(BACK, length)
    agent.move(RIGHT, 1)
player.on_chat("bridge", bridge)