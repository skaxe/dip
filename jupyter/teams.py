from enum import Enum, auto

class Team:
    def __init__(self, color='black', russian_str='Команда'):
        self.color = color
        self.russian_str = russian_str


class TeamKeys(Enum):
    MANCHESTER_UNITED = auto()
    LEICESTER_CITY_FC = auto()
    ARSENAL_FC = auto()
    ASTON_VILLA_FC = auto()
    BRIGHTON_AND_HOVE_ALBION_FC = auto()
    BURNLEY_FC = auto()
    CHELSEA_FC = auto()
    CRYSTAL_PALACE_FC = auto()
    EVERTON_FC = auto()
    BRENTFORD_FC = auto()
    LEEDS_UNITED_FC = auto()
    LIVERPOOL_FC = auto()
    MANCHESTER_CITY_FC = auto()
    NEWCASTLE_UNITED_FC = auto()
    NORWICH_FC = auto()
    WEST_HAM_UNITED_FC = auto()
    WATFORD_FC = auto()
    SOUTHAMPTON_FC = auto()
    TOTTENHAM_HOTSPUR_FC = auto()
    WOLVERHAMPTON_WANDERERS_FC = auto()

    # SWANSEA_CITY_FC = auto()
    # HUDDERSFIELD_TOWN_AFC = auto()
    # STOKE_CITY_FC = auto() 
    # WEST_BROMWICH_ALBION_FC = auto() 
    # AFC_BOURNEMOUTH = auto()
    # CARDIFF_CITY_FC = auto()
    # FULHAM_FC = auto()

    # continue

    
TEAMS_INFO = {
    TeamKeys.MANCHESTER_UNITED: Team("#d20222", 'Ман.Юнайтед'),
    TeamKeys.LEICESTER_CITY_FC: Team('#273e8a', 'Лестер'),
    TeamKeys.ARSENAL_FC: Team("#DC143C",'Арсенал'),
    TeamKeys.ASTON_VILLA_FC: Team("#00FFFF",'Астон Вилла'),
    TeamKeys.BRIGHTON_AND_HOVE_ALBION_FC: Team("#00BFFF",'Брайтон'),
    TeamKeys.BURNLEY_FC: Team("#8FCE00", 'Бёрнли'),
    TeamKeys.CHELSEA_FC: Team("#0000FF",'Челси'),
    TeamKeys.CRYSTAL_PALACE_FC: Team("# 87CEFA",'Кристал Пэлас'),
    TeamKeys.EVERTON_FC: Team("#7C1EFF",'Эвертон'),
    TeamKeys.BRENTFORD_FC: Team("#32CD32",'Брентфорд'),
    TeamKeys.LEEDS_UNITED_FC: Team("#20B2AA",'Лидс'),
    TeamKeys.LIVERPOOL_FC: Team("#FF4500",'Ливерпуль'),
    TeamKeys.MANCHESTER_CITY_FC: Team("#40E0D0",'Ман.Сити'),
    TeamKeys.NEWCASTLE_UNITED_FC: Team("ce7e00", 'Ньюкасл'),
    TeamKeys.NORWICH_FC: Team("#008000", 'Норвич'),
    TeamKeys.WEST_HAM_UNITED_FC: Team("#8B0000",'Вест Хэм'),
    TeamKeys.WATFORD_FC: Team("#FFFF00",'Уотфорд'),
    TeamKeys.SOUTHAMPTON_FC: Team("#FFD700",'Саутгемптон'),
    TeamKeys.TOTTENHAM_HOTSPUR_FC: Team("#1E90FF",'Тоттенхэм'),
    TeamKeys.WOLVERHAMPTON_WANDERERS_FC: Team("#000000",'Вулверхэмптон'),
    # TeamKeys.SWANSEA_CITY_FC: Team("#000023", 'Суонси Сити'),
    # TeamKeys.HUDDERSFIELD_TOWN_AFC: Team("#40E0D4",'Хаддерсфилд Таун'),
    # TeamKeys.STOKE_CITY_FC: Team("#0200FB",'Сток Сити'),
    # TeamKeys.WEST_BROMWICH_ALBION_FC: Team("#7C1EAA",'Вест Бромвич Альбион'),
    # TeamKeys.AFC_BOURNEMOUTH: Team("#a20272", 'Борнмут'),
    # TeamKeys.CARDIFF_CITY_FC: Team("8F5543", 'Кардифф Сити'),
    # TeamKeys.FULHAM_FC: Team("#AAB244",'Фулхэм'),



    # continue
}