from trpg import Master, Dice, Param, Thing, Process, Role, Event, Route, Game

class Test:
    def __init__(self):

        Param('POW', {'POW': 1, })
        Param('SEN', {'SEN': 1, })
        Param('INT', {'INT': 1, })

        Param('戦', {'戦': 1, 'POW': 5, }, Dice(2,6,10))
        Param('Punch_Offence',  {'Punch_Offence' : 0.5, 'SEN': 4, }, Dice(2,6))
        Param('Punch_Deffence', {'Punch_Deffence': 0.7, 'INT': 3, }, Dice(2,6))

        Param('WAY', {'WAY': 1}, Dice(1, 2))
        
        Thing('きびだんご', {'POW': 1, '戦': 1, })
        Thing('きび単位', {'POW': 1, '戦': 2, })

        Thing('桃太郎', {'POW': 10, 'SEN': 10, 'INT': 10, '戦': 1, 'Punch_Offence': 1, 'Punch_Deffence': 1, }, ['きびだんご'])
        Thing('犬', {'POW': 15, 'SEN':  8, 'INT':  8, '戦': 1, 'Punch_Offence': 1, 'Punch_Deffence': 1, })
        Thing('雉', {'POW':  8, 'SEN': 15, 'INT':  8, '戦': 1, 'Punch_Offence': 1, 'Punch_Deffence': 1, })
        Thing('猿', {'POW':  8, 'SEN':  8, 'INT': 15, '戦': 1, 'Punch_Offence': 1, 'Punch_Deffence': 1, })

        d26 = Dice(2, 6).dice
        Thing('鬼A', {'POW': 3, 'SEN': 5, 'INT': 6, '戦': d26(), 'Punch_Offence': d26(), 'Punch_Deffence': d26(), })
        Thing('鬼B', {'POW': d26(), 'SEN': d26(), 'INT': d26(), '戦': d26(), 'Punch_Offence': d26(), 'Punch_Deffence': d26(), })
        Thing('大鬼', {'POW': 30, 'SEN': 5, 'INT': 5, '戦': d26(), 'Punch_Offence': d26(), 'Punch_Deffence': d26(), })

        Process('Battle_Bar', '戦', 'bar')
        Process('Battle_COM', '戦', 'compare')
        Process('Battle_Inc', '戦', 'increase')
        Process('Battle_Dec', '戦', 'decrease', 'Punch_Offence', 'Punch_Deffence')

        Process('OneOfTwo', 'WAY', 'dice')

        Event('1', text='むかしむかし、あるところに、おじいさんとおばあさんがいました。')
        Event('2', text='その日も、おじいさんは山へ芝刈りに、おばあさんは川へ洗濯に行っていました。')
        Event('3', text='おばあさんが川で洗濯をしていると、どんぶらこどんぶらこと大きな桃が流れてきました。')
        Event('4', text='- 中略 -')
        Event('5', text='桃太郎はすくすくと育ち、あっという間に立派な青年に育ちました。')
        Event('6', text='そんな頃合いに、町の方で鬼どもが暴れまわっているという噂が聞こえてきました。')
        Event('7', text='桃「おじいさん、僕、鬼退治をしに行くよ！」')
        Event('8', text='おじい「心優しい、桃太郎や。お前ならそういうと思って準備をしておいたよ」')
        Event('9', text='そう言っておいじいさんは桃太郎に刀と旗を渡しました。')
        Event('10', text='おばあ「お腹が空くといけないから、このきびだんごを持ってお行き」')
        Event('11', text='桃「おばあさん、ありがとう。おばあさんのきびだんごは日本一ですから、食べれば力も百萬力です」')
        Event('12', text='そう言って桃太郎は鬼ヶ島へ鬼退治へと向かいました。')

        Event('E0', text='鬼ヶ島に来ている\nすると突然鬼が襲いかかってきた')
        Event('E1', 'Battle_COM', (0, 0, 1), ('鬼A',''), text='鬼Aの攻撃\n誰が攻撃を受けますか？')
        Event('E1n', 'Battle_Dec', (0, 0, 0), ('',''))
        Event('E2', 'Battle_COM', (0, 1, 0), ('','鬼A'), text='桃太郎陣営の攻撃')
        Event('E2n', 'Battle_Dec', (0, 0, 0), ('',''))
        Event('E3', text='さらに鬼が襲いかかってきた')
        Event('E4', 'Battle_COM', (0, 0, 1), ('鬼B',''), text='鬼Bの攻撃\n誰が攻撃を受けますか？')
        Event('E4n', 'Battle_Dec', (0, 0, 0), ('',''))
        Event('E5', 'Battle_COM', (0, 1, 0), ('','鬼B'), text='桃太郎陣営の攻撃')
        Event('E5n', 'Battle_Dec', (0, 0, 0), ('',''))
        Event('E6', 'OneOfTwo', text='何かが近づいてくる！？')
        Event('E7', text='大鬼が現れた')
        Event('E8', 'Battle_COM', (0, 0, 1), ('大鬼',''), text='大鬼の攻撃\n誰が攻撃を受けますか？')
        Event('E8n', 'Battle_Dec', (0, 0, 0), ('',''))
        Event('E9', 'Battle_COM', (0, 1, 0), ('','大鬼'), text='桃太郎陣営の攻撃')
        Event('E9n', 'Battle_Dec', (0, 0, 0), ('',''))
        Event('E10', text='大鬼は滅ぼされた\n故郷に平和が戻った')
        Event('gameover', text='ゲームオーバー')

        Event('EK0', 'Battle_Bar', (0, 0, 0), ('','きびだんご'))
        Event('EK1', 'Battle_Inc', (0, 0, 1), ('きびだんご',''))
        Event('EK2', 'Battle_Bar', (0, 0, 0), ('きび単位','きびだんご'))

        Route('start', '1', {'2': ('next', 0),})
        Route('2', '2', {'3': ('next', 0),})
        Route('3', '3', {'4': ('next', 0),})
        Route('4', '4', {'5': ('next', 0),})
        Route('5', '5', {'6': ('next', 0),})
        Route('6', '6', {'7': ('next', 0),})
        Route('7', '7', {'8': ('next', 0),})
        Route('8', '8', {'9': ('next', 0),})
        Route('9', '9', {'10': ('next', 0),})
        Route('10', '10', {'11': ('next', 0),})
        Route('11', '11', {'12': ('next', 0),})
        Route('12', '12', {'R1': ('next', 0),})

        Route('R0', 'E0', {'R1': (0, 0),})
        Route('R1', 'E1', {'R1n': ('next', 0),})
        Route('R1n', 'E1n', {'gameover': (0, 0),'R2': (1, 1000),})
        Route('R2', 'E2', {'R2n': ('next', 0),})
        Route('R2n', 'E2n', {'R3': (0, 0),'R1': (1, 1000),})
        Route('gameover', 'gameover', noend=False)
        Route('R3', 'E3', {'R4': (0, 0),}, noend=False)
        Route('R4', 'E4', {'R4n': ('next', 0),})
        Route('R4n', 'E4n', {'gameover': (0, 0),'R5': (1, 1000),})
        Route('R5', 'E5', {'R5n': ('next', 0),})
        Route('R5n', 'E5n', {'R6': (0, 0),'R4': (1, 1000),})
        Route('R6', 'E6', {'R7': (1, 0),'R6': (2, 0),})
        Route('R7', 'E7', {'R8': (0, 0),}, noend=False)
        Route('R8', 'E8', {'R8n': ('next', 0),})
        Route('R8n', 'E8n', {'gameover': (0, 0),'R9': (1, 1000),})
        Route('R9', 'E9', {'R9n': ('next', 0),})
        Route('R9n', 'E9n', {'R10': (0, 0),'R8': (1, 1000),})
        Route('R10', 'E10', noend=False)
        
        Route('kibi', 'EK0', {'RK2': (-1000, 0), 'RK1': (1, 1000),})
        Route('RK1', 'EK1', {'RK2': ('next', 0),})
        Route('RK2', 'EK2', {'kibi': ('next', 0),}, noend=False)

        Role('TARO', ['桃太郎', '犬', '雉', '猿'], ['start', 'kibi'])

    def test01(self):
        Game(['TARO']).start()
        

Test().test01()