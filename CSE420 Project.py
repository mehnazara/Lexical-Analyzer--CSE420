def internal(stop,temp_left_child,temp_counter):
    new_first = True
    while mathOP[stop] != ')':
        if mathOP[stop] == '|':
            if new_first == True:
                new_first = False
                finder = mathOP[stop-1]
                new_left_child = ''
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                new_left_child = x
                if stop+2 < len(mathOP) and mathOP[stop+2] == '*':
                    finder = mathOP[stop+1]
                    new_right_child = ''
                    for x in reference.keys():
                        if reference[x] == finder:
                            if done[x] == 'not':
                                done[x] = 'done'
                                break
                    new_right_child = x
                    again_left_child = new_right_child
                    nullable.append('*'+str(temp_counter+1))
                    firstpos['*'+str(temp_counter+1)] = firstpos[again_left_child] + []
                    lastpos['*'+str(temp_counter+1)] = lastpos[again_left_child] + []
                    firstpos[again_left_child].append('*'+str(temp_counter+1))
                    firstpos[again_left_child].append('left')
                    lastpos[again_left_child].append('*'+str(temp_counter+1))
                    lastpos[again_left_child].append('left')
                    new_right_child = '*'+str(temp_counter+1)
                    nullable.append('|'+str(temp_counter))
                    firstpos['|'+str(temp_counter)] = firstpos[new_left_child] + firstpos[new_right_child]
                    lastpos['|'+str(temp_counter)] = lastpos[new_left_child] + lastpos[new_right_child]
                    firstpos[new_left_child].append('|'+str(temp_counter))
                    firstpos[new_left_child].append('left')
                    lastpos[new_left_child].append('|'+str(temp_counter))
                    lastpos[new_left_child].append('left')
                    firstpos[new_right_child].append('|'+str(temp_counter))
                    firstpos[new_right_child].append('right')
                    lastpos[new_right_child].append('|'+str(temp_counter))
                    lastpos[new_right_child].append('right')
                    temp_left_child = '|'+str(temp_counter)
                    temp_counter += 2
                    stop += 2
                else:
                    finder = mathOP[stop+1]
                    new_right_child = ''
                    for x in reference.keys():
                        if reference[x] == finder:
                            if done[x] == 'not':
                                done[x] = 'done'
                                break
                    new_right_child = x
                    firstpos['|'+str(temp_counter)] = firstpos[new_left_child] + firstpos[new_right_child]
                    lastpos['|'+str(temp_counter)] = lastpos[new_left_child] + lastpos[new_right_child]
                    firstpos[new_left_child].append('|'+str(temp_counter))
                    firstpos[new_left_child].append('left')
                    lastpos[new_left_child].append('|'+str(temp_counter))
                    lastpos[new_left_child].append('left')
                    firstpos[new_right_child].append('|'+str(temp_counter))
                    firstpos[new_right_child].append('right')
                    lastpos[new_right_child].append('|'+str(temp_counter))
                    lastpos[new_right_child].append('right')
                    temp_left_child = '|'+str(temp_counter)
                    temp_counter += 1
            else: 
                if stop+2 < len(mathOP) and mathOP[stop+2] == '*':
                    finder = mathOP[stop+1]
                    new_right_child = ''
                    for x in reference.keys():
                        if reference[x] == finder:
                            if done[x] == 'not':
                                done[x] = 'done'
                                break
                    new_right_child = x
                    again_left_child = new_right_child
                    nullable.append('*'+str(temp_counter+1))
                    firstpos['*'+str(temp_counter+1)] = firstpos[again_left_child] + []
                    lastpos['*'+str(temp_counter+1)] = lastpos[again_left_child] + []
                    firstpos[again_left_child].append('*'+str(temp_counter+1))
                    firstpos[again_left_child].append('left')
                    lastpos[again_left_child].append('*'+str(temp_counter+1))
                    lastpos[again_left_child].append('left')
                    new_right_child = '*'+str(temp_counter+1)
                    nullable.append('|'+str(temp_counter))
                    firstpos['|'+str(temp_counter)] = firstpos[temp_left_child] + firstpos[new_right_child]
                    lastpos['|'+str(temp_counter)] = lastpos[temp_left_child] + lastpos[new_right_child]
                    firstpos[temp_left_child].append('|'+str(temp_counter))
                    firstpos[temp_left_child].append('left')
                    lastpos[temp_left_child].append('|'+str(temp_counter))
                    lastpos[temp_left_child].append('left')
                    firstpos[new_right_child].append('|'+str(temp_counter))
                    firstpos[new_right_child].append('right')
                    lastpos[new_right_child].append('|'+str(temp_counter))
                    lastpos[new_right_child].append('right')
                    temp_left_child = '|'+str(temp_counter)
                    temp_counter += 2
                    stop += 2
                else:
                    finder = mathOP[stop+1]
                    new_right_child = ''
                    for x in reference.keys():
                        if reference[x] == finder:
                            if done[x] == 'not':
                                done[x] = 'done'
                                break
                    new_right_child = x
                    if (temp_left_child in nullable) or (new_right_child in nullable):
                        nullable.append('|'+str(temp_counter))
                    firstpos['|'+str(temp_counter)] = firstpos[temp_left_child] + firstpos[new_right_child]
                    lastpos['|'+str(temp_counter)] = lastpos[temp_left_child] + lastpos[new_right_child]
                    firstpos[temp_left_child].append('|'+str(temp_counter))
                    firstpos[temp_left_child].append('left')
                    lastpos[temp_left_child].append('|'+str(temp_counter))
                    lastpos[temp_left_child].append('left')
                    firstpos[new_right_child].append('|'+str(temp_counter))
                    firstpos[new_right_child].append('right')
                    lastpos[new_right_child].append('|'+str(temp_counter))
                    lastpos[new_right_child].append('right')
                    temp_left_child = '|'+str(temp_counter)
                    temp_counter += 1
        elif mathOP[stop] == '.':
            if new_first == True:
                new_first = False
                finder = mathOP[stop-1]
                new_left_child = ''
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                new_left_child = x
                if stop+2 < len(mathOP) and mathOP[stop+2] == '*':
                    finder = mathOP[stop+1]
                    new_right_child = ''
                    for x in reference.keys():
                        if reference[x] == finder:
                            if done[x] == 'not':
                                done[x] = 'done'
                                break
                    new_right_child = x
                    again_left_child = new_right_child
                    nullable.append('*'+str(temp_counter+1))
                    firstpos['*'+str(temp_counter+1)] = firstpos[again_left_child] + []
                    lastpos['*'+str(temp_counter+1)] = lastpos[again_left_child] + []
                    firstpos[again_left_child].append('*'+str(temp_counter+1))
                    firstpos[again_left_child].append('left')
                    lastpos[again_left_child].append('*'+str(temp_counter+1))
                    lastpos[again_left_child].append('left')
                    new_right_child = '*'+str(temp_counter+1)
                    firstpos['.'+str(temp_counter)] = firstpos[new_left_child] + []
                    lastpos['.'+str(temp_counter)] = lastpos[new_left_child] + lastpos[new_right_child]
                    firstpos[new_left_child].append('.'+str(temp_counter))
                    firstpos[new_left_child].append('left')
                    lastpos[new_left_child].append('.'+str(temp_counter))
                    lastpos[new_left_child].append('left')
                    firstpos[new_right_child].append('.'+str(temp_counter))
                    firstpos[new_right_child].append('right')
                    lastpos[new_right_child].append('.'+str(temp_counter))
                    lastpos[new_right_child].append('right')
                    temp_left_child = '.'+str(temp_counter)
                    temp_counter += 2
                    stop += 2
                else:
                    finder = mathOP[stop+1]
                    new_right_child = ''
                    for x in reference.keys():
                        if reference[x] == finder:
                            if done[x] == 'not':
                                done[x] = 'done'
                                break
                    new_right_child = x
                    firstpos['.'+str(temp_counter)] = firstpos[new_left_child] + []
                    lastpos['.'+str(temp_counter)] = lastpos[new_right_child] + []
                    firstpos[new_left_child].append('.'+str(temp_counter))
                    firstpos[new_left_child].append('left')
                    lastpos[new_left_child].append('.'+str(temp_counter))
                    lastpos[new_left_child].append('left')
                    firstpos[new_right_child].append('.'+str(temp_counter))
                    firstpos[new_right_child].append('right')
                    lastpos[new_right_child].append('.'+str(temp_counter))
                    lastpos[new_right_child].append('right')
                    temp_left_child = '.'+str(temp_counter)
                    temp_counter += 1
            else: 
                if stop+2 < len(mathOP) and mathOP[stop+2] == '*':
                    finder = mathOP[stop+1]
                    new_right_child = ''
                    for x in reference.keys():
                        if reference[x] == finder:
                            if done[x] == 'not':
                                done[x] = 'done'
                                break
                    new_right_child = x
                    again_left_child = new_right_child
                    nullable.append('*'+str(temp_counter+1))
                    firstpos['*'+str(temp_counter+1)] = firstpos[again_left_child] + []
                    lastpos['*'+str(temp_counter+1)] = lastpos[again_left_child] + []
                    firstpos[again_left_child].append('*'+str(temp_counter+1))
                    firstpos[again_left_child].append('left')
                    lastpos[again_left_child].append('*'+str(temp_counter+1))
                    lastpos[again_left_child].append('left')
                    new_right_child = '*'+str(temp_counter+1)
                    if temp_left_child in nullable:
                        firstpos['.'+str(temp_counter)] = firstpos[temp_left_child] + firstpos[new_right_child]
                        nullable.append('.'+str(temp_counter))
                    else:
                        firstpos['.'+str(temp_counter)] = firstpos[temp_left_child] + []
                    lastpos['.'+str(temp_counter)] = lastpos[temp_left_child] + lastpos[new_right_child]
                    firstpos[temp_left_child].append('.'+str(temp_counter))
                    firstpos[temp_left_child].append('left')
                    lastpos[temp_left_child].append('.'+str(temp_counter))
                    lastpos[temp_left_child].append('left')
                    firstpos[new_right_child].append('.'+str(temp_counter))
                    firstpos[new_right_child].append('right')
                    lastpos[new_right_child].append('.'+str(temp_counter))
                    lastpos[new_right_child].append('right')
                    temp_left_child = '.'+str(temp_counter)
                    temp_counter += 2
                    stop += 2
                else:
                    finder = mathOP[stop+1]
                    new_right_child = ''
                    for x in reference.keys():
                        if reference[x] == finder:
                            if done[x] == 'not':
                                done[x] = 'done'
                                break
                    new_right_child = x
                    if temp_left_child in nullable:
                        firstpos['.'+str(temp_counter)] = firstpos[temp_left_child] + firstpos[new_right_child]
                    else:
                        firstpos['.'+str(temp_counter)] = firstpos[temp_left_child] + []
                    if new_right_child in nullable:
                        lastpos['.'+str(temp_counter)] = lastpos[temp_left_child] + lastpos[new_right_child]
                    else:
                        lastpos['.'+str(temp_counter)] = lastpos[new_right_child] + []
                    if (temp_left_child in nullable) and (new_right_child in nullable):
                        nullable.append('.'+str(temp_counter))
                    firstpos[temp_left_child].append('.'+str(temp_counter))
                    firstpos[temp_left_child].append('left')
                    lastpos[temp_left_child].append('.'+str(temp_counter))
                    lastpos[temp_left_child].append('left')
                    firstpos[new_right_child].append('.'+str(temp_counter))
                    firstpos[new_right_child].append('right')
                    lastpos[new_right_child].append('.'+str(temp_counter))
                    lastpos[new_right_child].append('right')
                    temp_left_child = '.'+str(temp_counter)
                    temp_counter += 1
        elif mathOP[stop] == '*':
            if new_first == True:
                new_first = False
                finder = mathOP[stop-1]
                new_left_child = ''
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                new_left_child = x
                nullable.append('*'+str(temp_counter))
                firstpos['*'+str(temp_counter)] = firstpos[new_left_child] + []
                lastpos['*'+str(temp_counter)] = lastpos[new_left_child] + []
                firstpos[new_left_child].append('*'+str(temp_counter))
                firstpos[new_left_child].append('left')
                lastpos[new_left_child].append('*'+str(temp_counter))
                lastpos[new_left_child].append('left')
                temp_left_child = '*'+str(temp_counter)
                temp_counter += 1
            else:
                nullable.append('*'+str(temp_counter))
                firstpos['*'+str(temp_counter)] = firstpos[temp_left_child] + []
                lastpos['*'+str(temp_counter)] = lastpos[temp_left_child] + []
                firstpos[temp_left_child].append('*'+str(temp_counter))
                firstpos[temp_left_child].append('left')
                lastpos[temp_left_child].append('*'+str(temp_counter))
                lastpos[temp_left_child].append('left')
                temp_left_child = '*'+str(temp_counter)
                temp_counter += 1
        stop += 1
    return stop,temp_left_child,temp_counter
#---------------------------------------------------------------------------------------------------------------
file = open("C:\\Users\\LENOVO\\OneDrive\\Desktop\\420 project\\samplecode.txt")
lexemes = []
for line in file:
    lexemes.append(line)
file.close()
for i in range(len(lexemes)):
    lexemes[i] = lexemes[i].strip('\n')
    lexemes[i] = lexemes[i].strip(' ')
    new_lexeme = ''
    for j in lexemes[i]:
        if j != ' ':
            new_lexeme += j
    lexemes[i] = new_lexeme
print(lexemes)


#----------------------------------------------------------------------------------------------------------------------------------
mathOP = '(+|-|x|/|=|!).#'
done = {}
reference = {}
firstpos = {}
lastpos = {}
followpos = {}
nullable = []
count = 1
for i in mathOP:
    if i != '(' and i != ')' and i != '|' and i != '.' and i != '*':
        reference[str(count)] = i
        done[str(count)] = 'not' 
        followpos[str(count)] = []
        firstpos[str(count)] = [str(count)]
        lastpos[str(count)] = [str(count)]
        count += 1

accepted = str(count-1)
#----------------------------------------------------------------------------------------------------------------------------------

stop = 0
first = True
counter = 1
current_left_child = ''
j = 0
#------------------------------------------------------------------------------------------------------------

while j < len(mathOP):
    if mathOP[j] == '|':      
        if first == True:
            first = False
            finder = mathOP[j-1]
            left_child = ''
            for x in reference.keys():
                if reference[x] == finder:
                    if done[x] == 'not':
                        done[x] = 'done'
                        break
            left_child = x
            if j+2 < len(mathOP) and mathOP[j+2] == '*':
                right_child = ''
                finder = mathOP[j+1]
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                right_child = x
                again_left_child = right_child
                nullable.append('*'+str(counter+1))
                firstpos['*'+str(counter+1)] = firstpos[again_left_child] + []
                lastpos['*'+str(counter+1)] = lastpos[again_left_child] + []
                firstpos[again_left_child].append('*'+str(counter+1))
                firstpos[again_left_child].append('left')
                lastpos[again_left_child].append('*'+str(counter+1))
                lastpos[again_left_child].append('left')
                right_child = '*'+str(counter+1)
                nullable.append('|'+str(counter))
                firstpos['|'+str(counter)] = firstpos[left_child] + firstpos[right_child]
                lastpos['|'+str(counter)] = lastpos[left_child] + lastpos[right_child]
                firstpos[left_child].append('|'+str(counter))
                firstpos[left_child].append('left')
                lastpos[left_child].append('|'+str(counter))
                lastpos[left_child].append('left')
                firstpos[right_child].append('|'+str(counter))
                firstpos[right_child].append('right')
                lastpos[right_child].append('|'+str(counter))
                lastpos[right_child].append('right')
                current_left_child = '|'+str(counter)
                counter += 2
                j += 2
            elif mathOP[j+1] == '(':
                stop = j+2
                temp_left_child = ''
                temp_counter = counter + 1
                stop,temp_left_child,temp_counter = internal(stop,temp_left_child,temp_counter)
                if mathOP[stop+1] == '*':
                    nullable.append('*'+str(temp_counter))
                    firstpos['*'+str(temp_counter)] = firstpos[temp_left_child] + []
                    lastpos['*'+str(temp_counter)] = lastpos[temp_left_child] + []
                    firstpos[temp_left_child].append('*'+str(temp_counter))
                    firstpos[temp_left_child].append('left')
                    lastpos[temp_left_child].append('*'+str(temp_counter))
                    lastpos[temp_left_child].append('left')
                    temp_left_child = '*'+str(temp_counter)
                    temp_counter += 1 
                    stop += 1
                    if temp_left_child in nullable:
                        nullable.append('|'+str(counter))
                    firstpos['|'+str(counter)] = firstpos[left_child] + firstpos[temp_left_child]
                    lastpos['|'+str(counter)] = lastpos[left_child] + lastpos[temp_left_child]
                    firstpos[left_child].append('|'+str(counter))
                    firstpos[left_child].append('left')
                    lastpos[left_child].append('|'+str(counter))
                    lastpos[left_child].append('left')
                    firstpos[temp_left_child].append('|'+str(counter))
                    firstpos[temp_left_child].append('right')
                    lastpos[temp_left_child].append('|'+str(counter))
                    lastpos[temp_left_child].append('right')
                    current_left_child = '|'+str(counter)
                    counter = temp_counter 
                    j = stop
                else:
                    if temp_left_child in nullable:
                        nullable.append('|'+str(counter))
                    firstpos['|'+str(counter)] = firstpos[left_child] + firstpos[temp_left_child]
                    lastpos['|'+str(counter)] = lastpos[left_child] + lastpos[temp_left_child]
                    firstpos[left_child].append('|'+str(counter))
                    firstpos[left_child].append('left')
                    lastpos[left_child].append('|'+str(counter))
                    lastpos[left_child].append('left')
                    firstpos[temp_left_child].append('|'+str(counter))
                    firstpos[temp_left_child].append('right')
                    lastpos[temp_left_child].append('|'+str(counter))
                    lastpos[temp_left_child].append('right')
                    current_left_child = '|'+str(counter)
                    counter = temp_counter 
                    j = stop
            else:
                right_child = ''
                finder = mathOP[j+1]
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                right_child = x
                firstpos['|'+str(counter)] = firstpos[left_child] + firstpos[right_child]
                lastpos['|'+str(counter)] = lastpos[left_child] + lastpos[right_child]
                firstpos[left_child].append('|'+str(counter))
                firstpos[left_child].append('left')
                lastpos[left_child].append('|'+str(counter))
                lastpos[left_child].append('left')
                firstpos[right_child].append('|'+str(counter))
                firstpos[right_child].append('right')
                lastpos[right_child].append('|'+str(counter))
                lastpos[right_child].append('right')
                current_left_child = '|'+str(counter)
                counter += 1 
                


        else:
            if j+2 < len(mathOP) and mathOP[j+2] == '*':
                right_child = ''
                finder = mathOP[j+1]
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                right_child = x
                again_left_child = right_child
                nullable.append('*'+str(counter+1))
                firstpos['*'+str(counter+1)] = firstpos[again_left_child] + []
                lastpos['*'+str(counter+1)] = lastpos[again_left_child] + []
                firstpos[again_left_child].append('*'+str(counter+1))
                firstpos[again_left_child].append('left')
                lastpos[again_left_child].append('*'+str(counter+1))
                lastpos[again_left_child].append('left')
                right_child = '*'+str(counter+1)
                nullable.append('|'+str(counter))
                firstpos['|'+str(counter)] = firstpos[current_left_child] + firstpos[right_child]
                lastpos['|'+str(counter)] = lastpos[current_left_child] + lastpos[right_child]
                firstpos[current_left_child].append('|'+str(counter))
                firstpos[current_left_child].append('left')
                lastpos[current_left_child].append('|'+str(counter))
                lastpos[current_left_child].append('left')
                firstpos[right_child].append('|'+str(counter))
                firstpos[right_child].append('right')
                lastpos[right_child].append('|'+str(counter))
                lastpos[right_child].append('right')
                current_left_child = '|'+str(counter)
                counter += 2
                j += 2
                

            elif mathOP[j+1] == '(':
                stop = j+2
                temp_left_child = ''
                temp_counter = counter + 1
                stop,temp_left_child,temp_counter = internal(stop,temp_left_child,temp_counter)
                if mathOP[stop+1] == '*':
                    nullable.append('*'+str(temp_counter))
                    firstpos['*'+str(temp_counter)] = firstpos[temp_left_child] + []
                    lastpos['*'+str(temp_counter)] = lastpos[temp_left_child] + []
                    firstpos[temp_left_child].append('*'+str(temp_counter))
                    firstpos[temp_left_child].append('left')
                    lastpos[temp_left_child].append('*'+str(temp_counter))
                    lastpos[temp_left_child].append('left')
                    temp_left_child = '*'+str(temp_counter)
                    temp_counter += 1 
                    stop += 1
                    if (current_left_child in nullable) or (temp_left_child in nullable):
                        nullable.append('|'+str(counter))
                    firstpos['|'+str(counter)] = firstpos[current_left_child] + firstpos[temp_left_child]
                    lastpos['|'+str(counter)] = lastpos[current_left_child] + lastpos[temp_left_child]
                    firstpos[current_left_child].append('|'+str(counter))
                    firstpos[current_left_child].append('left')
                    lastpos[current_left_child].append('|'+str(counter))
                    lastpos[current_left_child].append('left')
                    firstpos[temp_left_child].append('|'+str(counter))
                    firstpos[temp_left_child].append('right')
                    lastpos[temp_left_child].append('|'+str(counter))
                    lastpos[temp_left_child].append('right')
                    current_left_child = '|'+str(counter)
                    counter = temp_counter 
                    j = stop
                else:
                    if (current_left_child in nullable) or (temp_left_child in nullable):
                        nullable.append('|'+str(counter))
                    firstpos['|'+str(counter)] = firstpos[current_left_child] + firstpos[temp_left_child]
                    lastpos['|'+str(counter)] = lastpos[current_left_child] + lastpos[temp_left_child]
                    firstpos[current_left_child].append('|'+str(counter))
                    firstpos[current_left_child].append('left')
                    lastpos[current_left_child].append('|'+str(counter))
                    lastpos[current_left_child].append('left')
                    firstpos[temp_left_child].append('|'+str(counter))
                    firstpos[temp_left_child].append('right')
                    lastpos[temp_left_child].append('|'+str(counter))
                    lastpos[temp_left_child].append('right')
                    current_left_child = '|'+str(counter)
                    counter = temp_counter 
                    j = stop
            else:
                right_child = ''
                finder = mathOP[j+1]
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                right_child = x
                if (current_left_child in nullable) or (right_child in nullable):
                    nullable.append('|'+str(counter))
                firstpos['|'+str(counter)] = firstpos[current_left_child] + firstpos[right_child]
                lastpos['|'+str(counter)] = lastpos[current_left_child] + lastpos[right_child]
                firstpos[current_left_child].append('|'+str(counter))
                firstpos[current_left_child].append('left')
                lastpos[current_left_child].append('|'+str(counter))
                lastpos[current_left_child].append('left')
                firstpos[right_child].append('|'+str(counter))
                firstpos[right_child].append('right')
                lastpos[right_child].append('|'+str(counter))
                lastpos[right_child].append('right')
                current_left_child = '|'+str(counter)
                counter += 1 
    elif mathOP[j] == '.':
        if first == True:
            first = False
            left_child = ''
            finder = mathOP[j-1]
            for x in reference.keys():
                if reference[x] == finder:
                    if done[x] == 'not':
                        done[x] = 'done'
                        break
            left_child = x
            if j+2 < len(mathOP) and mathOP[j+2] == '*':
                right_child = ''
                finder = mathOP[j+1]
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                right_child = x
                again_left_child = right_child
                nullable.append('*'+str(counter+1))
                firstpos['*'+str(counter+1)] = firstpos[again_left_child] + []
                lastpos['*'+str(counter+1)] = lastpos[again_left_child] + []
                firstpos[again_left_child].append('*'+str(counter+1))
                firstpos[again_left_child].append('left')
                lastpos[again_left_child].append('*'+str(counter+1))
                lastpos[again_left_child].append('left')
                right_child = '*'+str(counter+1)
                firstpos['.'+str(counter)] = firstpos[left_child] + []
                lastpos['.'+str(counter)] = lastpos[left_child] + lastpos[right_child]
                firstpos[left_child].append('.'+str(counter))
                firstpos[left_child].append('left')
                lastpos[left_child].append('.'+str(counter))
                lastpos[left_child].append('left')
                firstpos[right_child].append('.'+str(counter))
                firstpos[right_child].append('right')
                lastpos[right_child].append('.'+str(counter))
                lastpos[right_child].append('right')
                current_left_child = '.'+str(counter)
                counter += 2
                j += 2

            elif mathOP[j+1] == '(':
                stop = j+2
                temp_left_child = ''
                temp_counter = counter + 1
                stop,temp_left_child,temp_counter = internal(stop,temp_left_child,temp_counter)
                if mathOP[stop+1] == '*':
                    nullable.append('*'+str(temp_counter))
                    firstpos['*'+str(temp_counter)] = firstpos[temp_left_child] + []
                    lastpos['*'+str(temp_counter)] = lastpos[temp_left_child] + []
                    firstpos[temp_left_child].append('*'+str(temp_counter))
                    firstpos[temp_left_child].append('left')
                    lastpos[temp_left_child].append('*'+str(temp_counter))
                    lastpos[temp_left_child].append('left')
                    temp_left_child = '*'+str(temp_counter)
                    temp_counter += 1 
                    stop += 1
                    firstpos['.'+str(counter)] = firstpos[left_child] + []
                    if temp_left_child in nullable:
                        lastpos['.'+str(counter)] = lastpos[left_child] + lastpos[temp_left_child]
                    else:
                        lastpos['.'+str(counter)] = lastpos[temp_left_child] + []
                    firstpos[left_child].append('.'+str(counter))
                    firstpos[left_child].append('left')
                    lastpos[left_child].append('.'+str(counter))
                    lastpos[left_child].append('left')
                    firstpos[temp_left_child].append('.'+str(counter))
                    firstpos[temp_left_child].append('right')
                    lastpos[temp_left_child].append('.'+str(counter))
                    lastpos[temp_left_child].append('right')
                    current_left_child = '.'+str(counter)
                    counter = temp_counter 
                    j = stop
                else:
                    firstpos['.'+str(counter)] = firstpos[left_child] + []
                    if temp_left_child in nullable:
                        lastpos['.'+str(counter)] = lastpos[left_child] + lastpos[temp_left_child]
                    else:
                        lastpos['.'+str(counter)] = lastpos[temp_left_child] + []
                    firstpos[left_child].append('.'+str(counter))
                    firstpos[left_child].append('left')
                    lastpos[left_child].append('.'+str(counter))
                    lastpos[left_child].append('left')
                    firstpos[temp_left_child].append('.'+str(counter))
                    firstpos[temp_left_child].append('right')
                    lastpos[temp_left_child].append('.'+str(counter))
                    lastpos[temp_left_child].append('right')
                    current_left_child = '.'+str(counter)
                    counter = temp_counter 
                    j = stop
            else:
                right_child = ''
                finder = mathOP[j+1]
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                right_child = x
                firstpos['.'+str(counter)] = firstpos[left_child] + []
                lastpos['.'+str(counter)] = lastpos[right_child] + []
                firstpos[left_child].append('.'+str(counter))
                firstpos[left_child].append('left')
                lastpos[left_child].append('.'+str(counter))
                lastpos[left_child].append('left')
                firstpos[right_child].append('.'+str(counter))
                firstpos[right_child].append('right')
                lastpos[right_child].append('.'+str(counter))
                lastpos[right_child].append('right')
                current_left_child = '.'+str(counter)
                counter += 1 
            
        else: 
            if j+2 < len(mathOP) and mathOP[j+2] == '*':
                right_child = ''
                finder = mathOP[j+1]
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                right_child = x
                again_left_child = right_child
                nullable.append('*'+str(counter+1))
                firstpos['*'+str(counter+1)] = firstpos[again_left_child] + []
                lastpos['*'+str(counter+1)] = lastpos[again_left_child] + []
                firstpos[again_left_child].append('*'+str(counter+1))
                firstpos[again_left_child].append('left')
                lastpos[again_left_child].append('*'+str(counter+1))
                lastpos[again_left_child].append('left')
                right_child = '*'+str(counter+1)
                if current_left_child in nullable:
                    firstpos['.'+str(counter)] = firstpos[current_left_child] + firstpos[right_child]
                    nullable.append('.'+str(counter))
                else:
                    firstpos['.'+str(counter)] = firstpos[current_left_child] + []
                lastpos['.'+str(counter)] = lastpos[current_left_child] + lastpos[right_child]
                firstpos[current_left_child].append('.'+str(counter))
                firstpos[current_left_child].append('left')
                lastpos[current_left_child].append('.'+str(counter))
                lastpos[current_left_child].append('left')
                firstpos[right_child].append('.'+str(counter))
                firstpos[right_child].append('right')
                lastpos[right_child].append('.'+str(counter))
                lastpos[right_child].append('right')
                temp_left_child = '.'+str(counter)
                counter += 2
                j += 2
            
            elif mathOP[j+1] == '(':
                stop = j+2
                temp_left_child = ''
                temp_counter = counter + 1
                stop,temp_left_child,temp_counter = internal(stop,temp_left_child,temp_counter)
                if mathOP[stop+1] == '*':
                    nullable.append('*'+str(temp_counter))
                    firstpos['*'+str(temp_counter)] = firstpos[temp_left_child] + []
                    lastpos['*'+str(temp_counter)] = lastpos[temp_left_child] + []
                    firstpos[temp_left_child].append('*'+str(temp_counter))
                    firstpos[temp_left_child].append('left')
                    lastpos[temp_left_child].append('*'+str(temp_counter))
                    lastpos[temp_left_child].append('left')
                    temp_left_child = '*'+str(temp_counter)
                    temp_counter += 1 
                    stop += 1
                    if current_left_child in nullable:
                        firstpos['.'+str(counter)] = firstpos[current_left_child] + firstpos[temp_left_child]
                    else:
                        firstpos['.'+str(counter)] = firstpos[current_left_child] + []
                    if temp_left_child in nullable:
                        lastpos['.'+str(counter)] = lastpos[current_left_child] + lastpos[temp_left_child]
                    else:
                        lastpos['.'+str(counter)] = lastpos[temp_left_child] + []
                    if (current_left_child in nullable) and (temp_left_child in nullable):
                        nullable.append('.'+str(counter))
                    firstpos[current_left_child].append('.'+str(counter))
                    firstpos[current_left_child].append('left')
                    lastpos[current_left_child].append('.'+str(counter))
                    lastpos[current_left_child].append('left')
                    firstpos[temp_left_child].append('.'+str(counter))
                    firstpos[temp_left_child].append('right')
                    lastpos[temp_left_child].append('.'+str(counter))
                    lastpos[temp_left_child].append('right')
                    current_left_child = '.'+str(counter)
                    counter = temp_counter 
                    j = stop
                else:
                    if current_left_child in nullable:
                        firstpos['.'+str(counter)] = firstpos[current_left_child] + firstpos[temp_left_child]
                    else:
                        firstpos['.'+str(counter)] = firstpos[current_left_child] + []
                    if temp_left_child in nullable:
                        lastpos['.'+str(counter)] = lastpos[current_left_child] + lastpos[temp_left_child]
                    else:
                        lastpos['.'+str(counter)] = lastpos[temp_left_child] + []
                    if (current_left_child in nullable) and (temp_left_child in nullable):
                        nullable.append('.'+str(counter))
                    firstpos[current_left_child].append('.'+str(counter))
                    firstpos[current_left_child].append('left')
                    lastpos[current_left_child].append('.'+str(counter))
                    lastpos[current_left_child].append('left')
                    firstpos[temp_left_child].append('.'+str(counter))
                    firstpos[temp_left_child].append('right')
                    lastpos[temp_left_child].append('.'+str(counter))
                    lastpos[temp_left_child].append('right')
                    current_left_child = '.'+str(counter)
                    counter = temp_counter 
                    j = stop    
            else:
                right_child = ''
                finder = mathOP[j+1]
                for x in reference.keys():
                    if reference[x] == finder:
                        if done[x] == 'not':
                            done[x] = 'done'
                            break
                right_child = x
                if current_left_child in nullable:
                    firstpos['.'+str(counter)] = firstpos[current_left_child] + firstpos[right_child]
                else:
                    firstpos['.'+str(counter)] = firstpos[current_left_child] + []
                if right_child in nullable:
                    lastpos['.'+str(counter)] = lastpos[current_left_child] + lastpos[right_child]
                else:
                    lastpos['.'+str(counter)] = lastpos[right_child] + []
                if (current_left_child in nullable) and (right_child in nullable):
                    nullable.append('.'+str(counter))
                firstpos[current_left_child].append('.'+str(counter))
                firstpos[current_left_child].append('left')
                lastpos[current_left_child].append('.'+str(counter))
                lastpos[current_left_child].append('left')
                firstpos[right_child].append('.'+str(counter))
                firstpos[right_child].append('right')
                lastpos[right_child].append('.'+str(counter))
                lastpos[right_child].append('right')
                current_left_child = '.'+str(counter)
                counter += 1
    elif mathOP[j] == '*':
        if first == True:
            first = False
            left_child = ''
            finder = mathOP[j-1]
            for x in reference.keys():
                if reference[x] == finder:
                    if done[x] == 'not':
                        done[x] = 'done'
                        break
            left_child = x
            nullable.append('*'+str(counter))
            firstpos['*'+str(counter)] = firstpos[left_child] + []
            lastpos['*'+str(counter)] = lastpos[left_child] + []
            firstpos[left_child].append('*'+str(counter))
            firstpos[left_child].append('left')
            lastpos[left_child].append('*'+str(counter))
            lastpos[left_child].append('left')
            current_left_child = '*'+str(counter)
            counter += 1
        else:
            nullable.append('*'+str(counter))
            firstpos['*'+str(counter)] = firstpos[current_left_child] + []
            lastpos['*'+str(counter)] = lastpos[current_left_child] + []
            firstpos[current_left_child].append('*'+str(counter))
            firstpos[current_left_child].append('left')
            lastpos[current_left_child].append('*'+str(counter))
            lastpos[current_left_child].append('left')
            current_left_child = '*'+str(counter)
            counter += 1



    j += 1
#---------------------------------------------------------------------------------------------------------------------

for i, j in firstpos.items():
    if i[0] == '.':
        right_child_firstpos = []
        for x, y in firstpos.items():
            if len(y) > 2:
                if y[-2] == i:
                    if y[-1] == 'right':
                        right_child_firstpos += y[:len(y)-2:]
        left_child_lastpos = []
        for m, n in lastpos.items():
            if len(n) > 2:
                if n[-2] == i:
                    if n[-1] == 'left':
                        left_child_lastpos += n[:len(n)-2:]
        for k in left_child_lastpos:
            followpos[k] += right_child_firstpos
    elif i[0] == '*':
        arr1 = j #left
        arr2 = lastpos[i] #right
        for j in range(0,len(arr2)-2):
            followpos[arr2[j]] += arr1[:-2:]

#print(firstpos)
#print(lastpos)
#-------------------------------------------------------------------------------------------------------------------
i = '' #starting state of dfa
for j in firstpos.keys():
    i = j
start = ''
for state in firstpos[i]:
    start += state



#-------------------------------------------------------------------------------------------------------------------
current_node = start
states = []
states.append(current_node)
state_dict = {}
state_dict['s'+str(0)] = current_node
state_link = {}
pointer = 0
state_pointer = 1
current_state = False
while pointer < len(states):
    found = []
    for_dict = {}
    for i in states[pointer]:     #i number
        if followpos[i] != []:
            adder = ''
            for k in followpos[i]:
                adder += k
            temp = reference[i]  #temp character  
            if temp not in found:
                found.append(temp)
                for_dict[temp] = adder
            else:
                if adder not in for_dict[temp]:
                    for_dict[temp] += adder
    for j in found:
        new = for_dict[j]
        if new not in states:
            states.append(new)
            state_dict['s'+str(state_pointer)] = new 
            state_link['s'+str(pointer)+j] = 's'+str(state_pointer)
            state_pointer += 1
        else:
            no =  ''
            for x,y in state_dict.items():
                if state_dict[x] == for_dict[j]:
                    no = x
            state_link['s'+str(pointer)+j] = no
                
    pointer += 1
#print(states)
#print(state_link)
#print(state_dict)
#-------------------------------------------------------------------------------------------------------------
final = []


for item in lexemes:
    move = 's0'
    parse = ''
    first = 1
    j = 0
    while j < len(item)+1:
        if j == len(item):
            if accepted in state_dict[move]:
                final.append(parse)
                j += 1
            else:
                j += 1
        else:
            if (move+item[j]) in state_link.keys():
                move = state_link[move+item[j]]
                first = 0
                parse += item[j]
                j += 1
            else:
                if first == 1:
                    if accepted in state_dict[move]:
                        final.append(item[j])
                        move = 's0'
                        j += 1
                    else:
                        move = 's0'
                        j += 1
                else:
                    if accepted in state_dict[move]:
                        final.append(parse)
                        parse = ''
                        first = 1
                        move = 's0'
                    else:
                        parse = ''
                        first = 1
                        move = 's0'
print(final)
