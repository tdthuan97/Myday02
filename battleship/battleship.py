def are_ships_destroyed(s, h):
    for i in range(len(s)):
        if s[i] != '.' and h[i] == '.':
            return False
    return True
