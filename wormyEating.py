#Embedded file name: /home/tyiltiz/programm/wormproject/wormyEating.py
import worm
import types
wormA = worm.Worm(bowel=range(1, 4), name='Wormy')
wormB = worm.Worm(bowel=range(1, 4), name='Niboo')
wormC = worm.Worm(bowel=range(1, 4), name='Boonie')
army = worm.WormArmy(wormList=[wormA, wormB, wormC], lastArmy=[])
for i in range(1, 1 + army.wormNum):
    army.lastArmy = [[i] * army.wormLen for i in range(1, 1 + army.wormNum)]

bean = worm.Bean('NATURE', 0)
world = worm.World()
trace = [bean]
army.display(bean, True)
army.displayLast()
while not army.isLastArmy():
    chosenworm = raw_input('Choose a wormie apart from ' + bean.whosePoo + ':')
    is_legal_input = world.is_legal_input(chosenworm, army)
    if is_legal_input is not False:
        if isinstance(is_legal_input, types.IntType):
            if world.is_eatible(bean, is_legal_input, army) is not False:
                if world.is_eatible(bean, is_legal_input, army) is 1:
                    poo = army.wormList[is_legal_input - 1].eat(bean)
                    trace.append(poo)
                    bean = poo
                    army.display(bean)
                else:
                    print "I ain't eating my own poo!"
        elif isinstance(is_legal_input, types.StringType):
            print 'You wanted me to do ' + is_legal_input + ', but I have no idea how to do it'
else:
    print 'Congratulations! You made us full and happy!'
    is_display = world.ask_affirm()
    world.display_trace(trace, is_display)
