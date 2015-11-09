s = 'ebuskriqzsgomsmuzrm'

pos = 0
end = 0
start = 0
print 'Length: ' + str(len(s))

def end_of_string(pos):
    if pos + 1 < (len(s) - 1):
        while s[pos] <= s[pos + 1]:
            if pos + 1 < (len(s) - 1):
                pos += 1
            else:
                pos += 1
                break
        return pos
    else:
        return pos


for pos in range(len(s)):
    last = end_of_string(pos)
    if (last - pos) > (end - start):
        start = pos
        end = last
    print 'Pos: ' + str(pos) + ' | Last: ' + str(last)

print 'Start: ' + str(start) + ', End: ' + str(end)
print s[start:end+1]