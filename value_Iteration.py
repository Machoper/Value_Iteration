gamma = 1
epsilon = 0.001
MAX_ITERS = 1000
wind = 3

u = [[0 for x in range(7)] for x in range(7)]

# Actions
stay = u"\u2022"
W = u"\u2190"
N = u"\u2191"
E = u"\u2192"
S = u"\u2193"
NW = u"\u2196"
NE = u"\u2197"
SE = u"\u2198"
SW = u"\u2199"
Actions = [stay, W, N, E, S, NW, NE, SE, SW]
direction = [[stay for x in range(7)] for x in range(7)]


# Reward function
def r(state):
    if state[0] == 3 and state[1] == 6:
        return 0
    else:
        return -1


# Wind function
def w(state):
    if wind == 1:
        return state
    if wind == 2:
        if 2 < state[1] < 6:
            state = (state[0] - 1, state[1])
        if state[0] < 0:
            state = (0, state[1])
        if state[0] > 6:
            state = (6, state[1])
        return state
    if wind == 3:
        if 2 < state[1] < 6:
            state = (state[0] - 2, state[1])
        if state[0] < 0:
            state = (0, state[1])
        if state[0] > 6:
            state = (6, state[1])
        return state


# Transition function
def t(s, a):
    s = w(s)
    if a == W:
        if s[1] > 0:
            s = (s[0], s[1]-1)
    elif a == N:
        if s[0] > 0:
            s = (s[0]-1, s[1])
    elif a == E:
        if s[1] < 6:
            s = (s[0], s[1]+1)
    elif a == S:
        if s[0] < 6:
            s = (s[0]+1, s[1])
    elif a == NE:
        if s[0] == 0 and s[1] == 6:
            return s
        elif s[0] == 0:
            s = (s[0], s[1]+1)
        elif s[1] == 6:
            s = (s[0]-1, s[1])
        else:
            s = (s[0]-1, s[1]+1)
    elif a == NW:
        if s[0] == 0 and s[1] == 0:
            return s
        elif s[0] == 0:
            s = (s[0], s[1]-1)
        elif s[1] == 0:
            s = (s[0]-1, s[1])
        else:
            s = (s[0]-1, s[1]-1)
    elif a == SE:
        if s[0] == 6 and s[1] == 6:
            return s
        elif s[0] == 6:
            s = (s[0], s[1]+1)
        elif s[1] == 6:
            s = (s[0]+1, s[1])
        else:
            s = (s[0]+1, s[1]+1)
    elif a == SW:
        if s[0] == 6 and s[1] == 0:
            return s
        elif s[0] == 6:
            s = (s[0], s[1]-1)
        elif s[1] == 0:
            s = (s[0]+1, s[1])
        else:
            s = (s[0]+1, s[1]-1)
    return s


# Value Iteration
u_prime = [[0 for x in range(7)] for x in range(7)]
iterations = 0
while iterations <= MAX_ITERS:
    iterations += 1
    delta = 0
    u = u_prime
    for i in range(7):
        for j in range(7):
            s = (i, j)
            MAX_V = -9999
            MAX_A = stay
            for a in Actions:
                s_prime = t(s, a)
                value = u[s_prime[0]][s_prime[1]]
                if value > MAX_V:
                    MAX_V = value
                    MAX_A = a
            u[i][j] = r(s) + gamma * MAX_V
            direction[i][j] = MAX_A
            if abs(u[i][j] - u[i][j]) > delta:
                delta = abs(u[i][j] - u[i][j])
    if delta >= epsilon:
        break


# Output value function and policy map
for i in range(7):
    print(u[i])
print('\n')
output = ''
for j in range(7):
    for k in range(7):
        output += direction[j][k] + ' '
        if len(output) == 14:
            print(output)
            output = ''
