#Embedded file name: /home/tyiltiz/programm/wormproject/worm.py
"""Worm Game

This is a game created by Hormetjan Yiltiz, from Kashgar, Sinkiang, China.
The game was originally played using four different types of coins.
And was implemented using GNU/Octave in November, 2011, Peking.
Here we have a Python code for it, eventually.

Please help design a funny GUI for this game. Resque the worms from the dark
terminal!

hyiltiz@gmail.com

"""
import types


class Worm(object):

    def __init__(self, bowel=[], name='wormy'):
        """Worms love eating, and their digestion is so good! Look at their
        bowel! And each have their name too! Such as Niboo.
        This is the most fundemantal object.

        """
        self.bowel = bowel
        self.name = name
        print 'Here we have the lovely wormy ' + self.name + '.'

    def eat(self, bean):
        """Want to know how do worms eat? Please read me!

        """
        if isinstance(bean, Bean):
            print self.name + ' ate bean ', bean.pooWho,
            print ', which was ' + bean.whosePoo + "'s poo!"
            self.bowel.insert(0, bean.pooWho)
            poo = Bean(self.name, self.bowel.pop())
            print self.name + ' pooed ', poo.pooWho, '!'
            return poo
        raise TypeError('Input must be of Type Bean!')

    def display(self):
        print 'Wormy ' + self.name + ' has ', self.bowel, ' in stomach.'


class Bean(object):

    def __init__(self, whosePoo='wormy', pooWho=0, pooColor='Green'):
        self.whosePoo = whosePoo
        self.pooWho = pooWho
        self.pooColor = pooColor
        print 'Here is a ' + self.pooColor + \
            ' bean that loved by our lovely wormies!'


class WormArmy(object):

    def __init__(self, wormLen=3, wormNum=3, wormList=[], lastArmy=[], wormMap={}):
        for wormListItem in wormList:
            if isinstance(wormListItem, Worm):
                pass
            else:
                raise TypeError

        wormLenList = []
        for theworm in wormList:
            wormLenList.append(len(theworm.bowel))

        self.wormLen = max(wormLenList)
        self.wormList = wormList
        self.wormNum = len(wormList)
        self.lastArmy = [range(1, wormLen + 1)] * wormNum
        self.wormMap = wormMap
        for i, theworm in enumerate(self.wormList):
            self.wormMap[theworm.name] = i + 1

        print 'We have a army of', wormNum, 'wormies: ',
        print [x.name for x in wormList]

    def display(self, bean, first=False):
        if self.makefullworm():
            for bowel_level in range(self.wormLen):
                for theworm in range(self.wormNum):
                    print repr(self.wormList[theworm].bowel[bowel_level]).rjust(1),

                print ''

            if first is False:
                wormindex = self.wormMap[bean.whosePoo] - 1
                poowhere = '  ' * self.wormNum
                poowhere = poowhere[:2 * wormindex] + types.StringType(bean.pooWho) + poowhere[2 * wormindex + 1:]
                print poowhere

    def displayLast(self):
        print 'The lovely wormies wants their hungry bowels be in this order:'
        for bowel_level in range(self.wormLen):
            for theworm in range(self.wormNum):
                print repr(self.lastArmy[theworm][bowel_level]).rjust(1),

            print ''

    def isLastArmy(self):
        armybowel = [x.bowel for x in self.wormList]
        return armybowel == self.lastArmy

    def makefullworm(self):
        return True


class World(object):

    def is_legal_input(self, chosenworm, army):
        """Here make sure this input to be legal, and return worm index"""
        if isinstance(chosenworm, types.StringType):
            #choseworm = chosenworm.strip()
            if chosenworm.isdigit() and 0 < types.IntType(chosenworm) <= army.wormNum:
                return types.IntType(chosenworm)
            if chosenworm.isalpha():
                if chosenworm in army.wormMap:
                    return army.wormMap[chosenworm]
                else:
                    return chosenworm
            else:
                return False
        else:
            return False

    def is_eatible(self, bean, chosenworm, army):
        if isinstance(bean, Bean) and isinstance(army, WormArmy) and isinstance(chosenworm, types.IntType):
            if bean.whosePoo is army.wormList[chosenworm - 1].name:
                return 0
            else:
                return 1
        else:
            return False

    def display_trace(self, trace, isdisplay=True):
        print 'You have fed', len(trace), 'wormies.'
        if isdisplay is True:
            print 'Here is how it all happened:'
            print 'Wormy ' + trace[1].whosePoo + ' ate ' + trace[0].whosePoo + "'s " + trace[0].pooColor + ' poo,'
            for i in range(1, len(trace) - 1):
                print 'which was wormy ' + trace[i].whosePoo + "'s " + trace[i].pooColor + ' poo,'

            print 'which was wormy ' + trace[i].whosePoo + "'s " + trace[i].pooColor + ' poo!!!'
        else:
            print 'Well, never minding how things             happen is a good idea to stay out of trouble!'

    def ask_affirm(self, str='Do you want to know how it all happened? Y/N'):
        answer = raw_input(str)
        if answer is 'Y' or 'Yes' or 'YES' or 'Yea' or 'Yeah' or 'yea' or 'yeah':
            return True
        else:
            return False

    def switch(self, command, trace, army):
        if isinstance(command, types.StringType):
            command = command.lower()
            print 'Your command is:' + command

    def undo(self, trace, army):
        print 'Some time ago...'
        thebean = trace.pop()
        if thebean.whosePoo == 'NAUTRE':
            print 'In fact, this was the beginning of the universe: Big BANG!'
            return thebean
        else:
            theworm = army.wormList[army.wormMap[thebean.whosePoo] - 1]
            theworm.bowel.reverse()
            poo = theworm.eat(thebean)
            theworm.bowel.reverse()
            return poo
