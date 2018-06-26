from ai import AI

if __name__ == '__main__':
    wang = []
    f = open(r'D:/ai_result.txt', 'w')
    for i in open(r'D:/ai.txt'):
        a = i.strip().split(' ')
        hand = list(a[6:8])
        if len(a) > 9:
            l = list(a[8:])
        if len(a) == 8:
            l = list()
        ai_move = AI(int(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5]), hand, l).parse()
        if ai_move[-1] != int(a[0]):
            f.writelines(i + ' ' + str(ai_move))
            wang.append(i.strip())
    f.close()
    print wang
