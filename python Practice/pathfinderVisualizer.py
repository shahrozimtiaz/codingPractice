import pygame
import random

class Node:
    def __init__(self,r,c,x,y,w=25,h=25,color=(0,128,255)):
        self.r = r
        self.c = c
        self.rect = pygame.Rect((x,y,w,h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.innerRect = (x+1,y+1,w-2,h-2)
        self.wall = False
        self.src = False
        self.sink = False
        self.f = None
        self.g = None
        self.h = None
        self.p = None

    def __str__(self):
        return '(r: {}, c: {})'.format(self.r,self.c)


class Button:
    def __init__(self,x,y,color,label):
        self.rect = None
        self.x = x
        self.y = y
        self.w = None
        self.h = None
        self.color = color
        self.label = label

    def add_button(self,win):
        font = pygame.font.Font('freesansbold.ttf', 15)
        text_surface = font.render(self.label, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        self.rect = text_rect
        self.w = text_rect.w
        self.h = text_rect.h
        text_rect.center = (self.x + self.w / 2, self.y + self.h / 2)
        pygame.draw.rect(win, self.color, text_rect)
        win.blit(text_surface, text_rect)

def create_grid(win,src,sink):
    win.fill((0, 0, 0))
    rectW = 25
    rectH = 25
    w, h = pygame.display.get_surface().get_size()
    y = -rectH
    gridH = (h - (2 * rectH)) // rectH
    gridW = w // rectW
    nodes = [[None]*gridW for r in range(gridH)]
    for r in range(gridH):
        y += rectH
        x = -rectW
        for c in range(gridW):
            x += rectW
            node = Node(r,c,x,y)
            nodes[r][c] = node
            pygame.draw.rect(win, node.color, node.rect)
            if r == src[0] and c == src[1]:
                node.src = True
                pygame.draw.rect(win, (0, 255, 0), pygame.Rect(node.innerRect))
            elif r == sink[0] and c == sink[1]:
                node.sink = True
                pygame.draw.rect(win, (255, 0, 0), pygame.Rect(node.innerRect))
            else:
                pygame.draw.rect(win, (0, 0, 0), pygame.Rect(node.innerRect))
    bx, by = 18, h-30
    button_buffer = 13
    button1 = Button(bx,by,(255,0,0),'Restart')
    button1.add_button(win)

    button = button1
    button2 = Button(button.x + button.w + button_buffer, by, (255, 0, 0), 'DFS')
    button2.add_button(win)

    button = button2
    button3 = Button(button.x + button.w + button_buffer, by, (255, 0, 0), 'BFS')
    button3.add_button(win)

    button = button3
    button4 = Button(button.x + button.w + button_buffer, by, (255, 0, 0), 'A*')
    button4.add_button(win)

    button=button4
    button5 = Button(button.x + button.w + button_buffer,by,(255,0,0),'Quit')
    button5.add_button(win)
    buttons = [button1,button2,button3,button4,button5]
    return nodes, buttons


def create_wall(event):
    for row in nodes:
        for node in row:
            if node.rect.collidepoint(event.pos):
                if (node.r != src[0] or node.c != src[1]) and (node.r != sink[0] or node.c != sink[1]):
                    node.wall=True
                    pygame.draw.rect(win, (255, 255, 255), pygame.Rect(node.innerRect))
                    break
                    
                      
def get_node(event):
    for row in nodes:
        for node in row:
            if node.rect.collidepoint(event.pos):
                return node
            

def set_up(src,sink):
    nodes, buttons = create_grid(win,src,sink)
    return nodes,buttons


def check_buttons(event):
    for button in buttons:
        if button.rect.collidepoint(event.pos):
            return button.label

def DFS(win,nodes,src):
    def _dfs(win,nodes,visted,r,c):
        done = False
        visted[r][c]=True
        if nodes[r][c].sink:
            pygame.draw.rect(win, (255, 0, 255), pygame.Rect(nodes[r][c].innerRect))
            pygame.display.update()
            return True
        if nodes[r][c].wall:
            return False
        if not nodes[r][c].src:
            pygame.draw.rect(win, (153, 255, 204), pygame.Rect(nodes[r][c].innerRect))
            pygame.display.update()
        dirs = list(range(8))
        random.shuffle(dirs)
        for dir in dirs:
            if done:
                return True
            elif dir == 0 and (r-1>=0 and c-1>=0) and not visted[r-1][c-1]: #nw
                done = _dfs(win,nodes,visted,r-1,c-1)
            elif dir == 1 and r-1>=0 and not visted[r-1][c]: #n
                done = _dfs(win, nodes, visted, r - 1, c)
            elif dir == 2 and (r-1>=0 and c+1<len(nodes[r])) and not visted[r-1][c+1]: #ne
                done = _dfs(win, nodes, visted, r - 1, c + 1)
            elif dir == 3 and c+1<len(nodes[r]) and not visted[r][c+1]: #e
                done = _dfs(win, nodes, visted, r, c + 1)
            elif dir == 4 and (r+1<len(nodes) and c+1<len(nodes[r])) and not visted[r+1][c+1]: #se
                done = _dfs(win, nodes, visted, r + 1, c + 1)
            elif dir == 5 and r+1<len(nodes) and not visted[r+1][c]: #s
                done = _dfs(win, nodes, visted, r + 1, c)
            elif dir == 6 and (r+1<len(nodes) and c-1>=0) and not visted[r+1][c-1]: #sw
                done = _dfs(win, nodes, visted, r + 1, c - 1)
            elif dir == 7 and c-1>=0 and not visted[r][c-1]: #w
                done = _dfs(win, nodes, visted, r, c - 1)
        return done
    visted=[[0]*len(nodes[0]) for r in range(len(nodes))]
    _dfs(win,nodes,visted,src[0],src[1])

def BFS(win,nodes,src):
    queue = []
    visited = [[0]*len(nodes[0]) for r in range(len(nodes))]
    queue.append(nodes[src[0]][src[1]])
    while queue:
        node = queue.pop(0)
        r, c = node.r, node.c
        if visited[r][c] or nodes[r][c].wall:
            continue
        visited[r][c] = True
        if nodes[r][c].sink:
            pygame.draw.rect(win, (255, 0, 255), pygame.Rect(nodes[r][c].innerRect))
            pygame.display.update()
            break
        if not nodes[r][c].src:
            pygame.draw.rect(win, (153, 255, 204), pygame.Rect(nodes[r][c].innerRect))
            pygame.display.update()
        dirs = list(range(8))
        random.shuffle(dirs)
        for dir in dirs:
            if dir == 0 and (r - 1 >= 0 and c - 1 >= 0) and not visited[r - 1][c - 1]:  # nw
                queue.append(nodes[r-1][c-1])
            elif dir == 1 and r - 1 >= 0 and not visited[r - 1][c]:  # n
                queue.append(nodes[r-1][c])
            elif dir == 2 and (r - 1 >= 0 and c + 1 < len(nodes[r])) and not visited[r - 1][c + 1]:  # ne
                queue.append(nodes[r-1][c+1])
            elif dir == 3 and c + 1 < len(nodes[r]) and not visited[r][c + 1]:  # e
                queue.append(nodes[r][c+1])
            elif dir == 4 and (r + 1 < len(nodes) and c + 1 < len(nodes[r])) and not visited[r + 1][c + 1]:  # se
                queue.append(nodes[r+1][c+1])
            elif dir == 5 and r + 1 < len(nodes) and not visited[r + 1][c]:  # s
                queue.append(nodes[r+1][c])
            elif dir == 6 and (r + 1 < len(nodes) and c - 1 >= 0) and not visited[r + 1][c - 1]:  # sw
                queue.append(nodes[r+1][c-1])
            elif dir == 7 and c - 1 >= 0 and not visited[r][c - 1]:  # w
                queue.append(nodes[r][c-1])

def A_STAR(win,nodes,src):
    queue = []
    closed = [[0]*len(nodes[0]) for r in range(len(nodes))]
    r = src[0]
    c = src[1]
    queue.append(nodes[r][c])
    queue[-1].f=0
    queue[-1].g=0
    queue[-1].h=0
    queue[-1].p=None
    final_node = None
    while queue:
        least_ind = 0
        for i in range(len(queue)):
            if queue[i].f<queue[least_ind].f:
                least_ind=i
        node = queue.pop(least_ind)
        r, c = node.r, node.c
        if closed[r][c] or node.wall:
            continue
        closed[r][c] = True
        if node.sink:
            pygame.draw.rect(win, (255, 0, 255), pygame.Rect(nodes[r][c].innerRect))
            pygame.display.update()
            final_node = node
            break
        if not node.src:
            pygame.draw.rect(win, (153, 255, 204), pygame.Rect(nodes[r][c].innerRect))
            pygame.display.update()
        successors = []
        if r - 1 >= 0 and c - 1 >= 0:  # nw
            successors.append(nodes[r - 1][c - 1])
        if r - 1 >= 0:  # n
            successors.append(nodes[r - 1][c])
        if r - 1 >= 0 and c + 1 < len(nodes[r]):  # ne
            successors.append(nodes[r - 1][c + 1])
        if c + 1 < len(nodes[r]):  # e
            successors.append(nodes[r][c + 1])
        if r + 1 < len(nodes) and c + 1 < len(nodes[r]):  # se
            successors.append(nodes[r + 1][c + 1])
        if r + 1 < len(nodes):  # s
            successors.append(nodes[r + 1][c])
        if r + 1 < len(nodes) and c - 1 >= 0:  # sw
            successors.append(nodes[r + 1][c - 1])
        if c - 1 >= 0:  # w
            successors.append(nodes[r][c - 1])

        for successor in successors:
            if closed[successor.r][successor.c]:
                continue
            successor.g = node.g+1
            successor.h = max(abs(successor.r - sink[0]),abs(successor.c - sink[1]))
            successor.f = successor.g + successor.h
            successor.p = node
            in_open_better_option = False
            for o in queue:
                if o.f < successor.f and (o.r==successor.r and o.c==successor.c):
                    in_open_better_option = True
            if in_open_better_option:
                continue
            queue.append(successor)
    if final_node:
        while final_node.p:
            final_node=final_node.p
            if final_node.p:
                pygame.draw.rect(win, (0, 200, 200), pygame.Rect(final_node.innerRect))

        pygame.display.update()



if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Pathfinder Visualizer')
    src, sink = (3, 3), (18, 33)
    nodes, buttons = set_up(src,sink)
    done = False
    dragging = False
    srcDragging = False
    sinkDragging = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = check_buttons(event)
                if button == 'Restart':
                    src, sink = (3, 3), (18, 33)
                    nodes, buttons = set_up(src,sink)
                elif button == 'DFS':
                    nodes, buttons = set_up(src,sink)
                    DFS(win,nodes,src)
                elif button == 'BFS':
                    nodes, buttons = set_up(src,sink)
                    BFS(win,nodes,src)
                elif button == 'A*':
                    nodes, buttons = set_up(src,sink)
                    A_STAR(win,nodes,src)
                elif button == 'Quit':
                    done = True
                elif nodes[src[0]][src[1]].rect.collidepoint(event.pos):
                    srcDragging=True
                elif nodes[sink[0]][sink[1]].rect.collidepoint(event.pos):
                    sinkDragging=True
                else:
                    dragging = True
                    create_wall(event)
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                srcDragging=False
                sinkDragging=False
            if srcDragging and event.type == pygame.MOUSEMOTION:
                node = get_node(event)
                if node:
                    src = (node.r, node.c)
                    nodes, buttons = set_up(src, sink)
            if sinkDragging and event.type == pygame.MOUSEMOTION:
                node = get_node(event)
                if node:
                    sink = (node.r,node.c)
                    nodes, buttons = set_up(src,sink)
            if dragging and event.type == pygame.MOUSEMOTION:
                create_wall(event)
        pygame.display.update()
        pygame.time.delay(20)
    pygame.quit()
