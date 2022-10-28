import yaml
from math import modf


class Player ():
    name                        = str
    team                        = str
    runs                        = None
    balls                       = None # do extras count?
    fours                       = None
    sixes                       = None
    assists                     = []
    tem                         = str

class Batsman (Player) :
    out_bowler                  = None
    out_fielder                 = None

class Bowler (Player) :
    overs                       = None
    wickets                     = []

class Ball ():
    over                        = int
    ball_no                     = int
    batsman                     = str
    bowler                      = str
    non_stkr                    = str
    xtras                       = dict()
    runs                        = int
    player_out                  = None
    fielders                    = None
    wicket_kind                 = None


    def __init__(self, _ball) :
        (ball_no, _ball),       = _ball.items()

        self.over               = int(modf(ball_no)[1])
        self.ball_no            = round(modf(ball_no)[0] * 10)
        self.batsman            = _ball['batsman']
        self.bowler             = _ball['bowler']
        self.non_stkr           = _ball['non_striker']
        self.runs               = _ball['runs']['total']
        
        if 'extras' in _ball.keys():
            self.xtras          = _ball['extras']
        else :      
            self.xtras          = None
        
        if 'wicket' in _ball.keys():
            if 'fielders' in _ball['wicket'].keys() :
                self.fielders   = _ball['wicket']['fielders']

            self.kind           = _ball['wicket']['kind']
            self.player_out     = _ball['wicket']['player_out']

class Match ():
    city                        = str
    dates                       = list()
    match_type                  = str
    bowlers                     = dict()
    batsmen                     = dict()
    competition                 = None
    outcome                     = dict()
    overs                       = int
    p_of_match                  = str
    team_a                      = str
    team_b                      = str
    toss_win                    = str
    toss_dec                    = str
    umpires                     = dict()
    venue                       = str
    balls_fi                    = dict()
    balls_si                    = dict()

    def __init__(self, path = 'database/yaml_dataset/335982.yaml'):
        with open(path) as f:
            docs = yaml.load_all(f, Loader=yaml.Loader)
            
            for doc in docs:
                self.city           = doc['info']['city']
                self.dates          = doc['info']['dates']
                self.match_type     = doc['info']['match_type']
                self.outcome        = doc['info']['outcome']
                self.overs          = doc['info']['overs']
                self.p_of_match     = doc['info']['player_of_match'][0]
                self.umpires        = doc['info']['umpires']
                self.venue          = doc['info']['venue']
                self.team_a         = doc['info']['teams'][0]
                self.team_b         = doc['info']['teams'][1]
                self.toss_win       = doc['info']['toss']['winner']
                self.toss_dec       = doc['info']['toss']['decision']

                if 'competetion' in doc['info'].keys() :
                    self.competition = doc['info']['competition']
                

                for _ball in doc['innings'][0]['1st innings']['deliveries']:
                    cur_ball = Ball(_ball)
                    self.balls_fi[str(cur_ball.over) + '.' + str(cur_ball.ball_no)] = cur_ball

                    # if cur_ball.batsman in self.batsmen.keys() :
                    #     self.batsmen[cur_ball.batsman].update(_ball, self.team_a)
                    # else :
                    #     self.batsmen[cur_ball.batsman] = Batsman(_ball, self.team_a)

                    # if cur_ball.bowler in self.bowlers.keys() :
                    #     self.bowlers[cur_ball.bowler].update(_ball, self.team_a)
                    # else :
                    #     self.bowlers[cur_ball.bowler] = Bowler(_ball, self.team_a)


                for _ball in doc['innings'][1]['2nd innings']['deliveries']:
                    cur_ball = Ball(_ball)
                    self.balls_si[str(cur_ball.over) + '.' + str(cur_ball.ball_no)] = cur_ball

                if self.toss_dec == 'bat' and self.toss_win != self.team_a :
                    self.team_a, self.team_b = self.team_b, self.team_a

if __name__ == '__main__':
    x = Match('database/yaml_dataset/335990.yaml')
    print((x.city))
    print((x.dates))
    print((x.match_type))
    # for ball in x.balls_fi :
    #     if x.balls_fi[ball].xtras :
    #         print(ball, x.balls_fi[ball].runs, x.balls_fi[ball].xtras)
    print((x.outcome))
    print((x.p_of_match))
    print((x.umpires))
    print((x.venue))
    print(x.team_b)
    print(x.team_a)
    print(x.toss_win)
    print(x.toss_dec)