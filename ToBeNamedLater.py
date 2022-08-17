import yaml
from math import modf

class ball ():
    over                        = int
    ball_no                     = int
    batsman                     = str
    bowler                      = str
    non_stkr                    = str
    xtras                       = dict()
    runs                        = int
    player_out                  = None
    fielder                     = None
    wicket_kind                 = None

class match ():
    city                        = str
    dates                       = list()
    match_type                  = str
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

    def __init__(self, path = 'dataset/ipl/335982.yaml'):
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
                    cur_ball = ball()
                    cur_ball.over = int(modf(list(_ball.keys())[0])[1])
                    cur_ball.ball_no = round(modf(list(_ball.keys())[0])[0] * 10)
                    # cur_ball.batsman = 
                    print(cur_ball.over, end = " ")
                    print(cur_ball.ball_no)
                   
        # 'city', 'competition', 'dates', 'gender', 'match_type',
        # 'outcome', 'overs', 'player_of_match', 'teams', 'toss', 'umpires', 'venue'
    



if __name__ == '__main__':
    x = match('dataset/ipl/335982.yaml')
    
    # print((x.city))
    # print((x.dates))
    # print((x.match_type))
    # print((x.outcome))
    # print((x.p_of_match))
    # print((x.umpires))
    # print((x.venue))
    # print(x.team_b)
    # print(x.team_a)
    # print(x.toss_win)
    # print(x.toss_dec)