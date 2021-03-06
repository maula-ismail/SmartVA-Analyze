from smartva.data.common_data import CHILD

AGE_GROUP = CHILD
KEEP_PATTERN = r'(sid$|real|age$|sex$|cause$|restricted$|s\d+)'

GENERATED_VARS_DATA = {
    's2991': 0,
    's2992': 0,
    's2993': 0,
    's2994': 0,
    's2995': 0,
    's5991': 0,
    's6991': 0,
    's8991': 0,
    's8992': 0,
    's11991': 0,
    's13991': 0,
    's16991': 0,
    's30991': 0,
    's113991': 0,
    's114991': 0,
    's116991': 0,
    's135991': 0,
    's139991': 0,
    's141991': 0,
    'age': 0,
    'sex': 0,
    'restricted': '',
}

VAR_CONVERSION_MAP = {
    'sid': 'sid',
    'g5_02': 'real_gender',
    'g5_04a': 'real_age',
    'g5_04b': 's3',
    'g5_04c': 's4',
    'c1_01': 's5',
    'c1_02': 's6',
    'c1_03': 's7',
    'c1_04': 's8',
    'c1_05': 's9',
    'c1_06a': 's11',
    'c1_07': 's13',
    'c1_08b': 's14',
    'c1_11': 's16',
    'c1_12': 's17',
    'c1_13': 's18',
    'c1_14': 's19',
    'c1_20': 's28',
    'c1_21': 's29',
    'c1_22a': 's30',
    'c1_25': 's31',
    'c4_01': 's110',
    'c4_02': 's111',
    'c4_03': 's112',
    'c4_04': 's113',
    'c4_05': 's114',
    'c4_06': 's115',
    'c4_07b': 's116',
    'c4_08': 's117',
    'c4_09': 's118',
    'c4_10': 's119',
    'c4_11': 's120',
    'c4_12': 's121',
    'c4_13': 's122',
    'c4_14': 's123',
    'c4_15': 's124',
    'c4_16': 's125',
    'c4_17': 's126',
    'c4_18': 's127',
    'c4_19': 's128',
    'c4_20': 's129',
    'c4_22': 's130',
    'c4_23': 's131',
    'c4_24': 's132',
    'c4_25': 's133',
    'c4_26': 's134',
    'c4_27': 's135',
    'c4_28': 's136',
    'c4_29': 's137',
    'c4_30': 's138',
    'c4_31_1': 's139',
    'c4_32': 's141',
    'c4_33': 's142',
    'c4_34': 's143',
    'c4_35': 's144',
    'c4_36': 's145',
    'c4_37': 's146',
    'c4_38': 's147',
    'c4_39': 's148',
    'c4_40': 's149',
    'c4_41': 's150',
    'c4_42': 's151',
    'c4_43': 's152',
    'c4_44': 's153',
    'c4_46': 's154',
    'c4_47_1': 's155',
    'c4_47_2': 's156',
    'c4_47_3': 's157',
    'c4_47_4': 's158',
    'c4_47_5': 's159',
    'c4_47_6': 's160',
    'c4_47_7': 's161',
    'c4_47_8a': 's162',
    'c4_47_9': 's163',
    'c4_47_11': 's164',
    'c4_48': 's165',
    'c4_49': 's166',
    'c5_17': 's188',
    'c5_18': 's189',
    'c5_19': 's190',
    's180': 's180',
    's181': 's181',
}

COPY_VARS = {
    'real_age': 'age',
    'real_gender': 'sex'
}

AGE_QUARTILE_BINARY_VARS = {
    'age': [
        (7, 's2995'),
        (3, 's2994'),
        (1, 's2993'),
        (.4166667, 's2992'),
        (0, 's2991')
    ],
    's116': [
        (1, 's116991')
    ]
}

DURATION_CUTOFF_DATA = {
    'age': 2,
    's9': 1000,
    's14': 1000,
    's28': 270,
    's29': 8,
    's31': 300,
    's111': 5,
    's117': 3,
    's119': 2,
    's122': 7,
    's126': 3,
    's128': 3,
    's142': 5,
    's146': 3.5
}

INJURY_VARS = {
    ('s166', 10): [
        's155',
        's156',
        's157',
        's158',
        's159',
        's160',
        's161',
        's162',
        's163',
        's165',
    ]
}

BINARY_CONVERSION_MAP = {
    's5': {
        2: 's5991',
    },
    's6': {
        2: 's6991',
        3: 's6991',
    },
    's8': {
        1: 's8991',
        2: 's8992',
    },
    's11': {
        4: 's11991',
        5: 's11991',
    },
    's13': {
        1: 's13991',
        2: 's13991',
    },
    's16': {
        2: 's16991',
    },
    's30': {
        3: 's30991',
        4: 's30991',
        5: 's30991',
    },
    's113': {
        3: 's113991',
    },
    's114': {
        2: 's114991',
        3: 's114991',
    },
    's135': {
        3: 's135991',
    },
    's139': {
        1: 's139991',
    },
    's141': {
        1: 's141991',
    },
    'sex': [2]
}

BINARY_VARS = [
    'sex',
    's7',
    's17',
    's18',
    's19',
    's110',
    's112',
    's115',
    's118',
    's120',
    's121',
    's123',
    's124',
    's125',
    's127',
    's129',
    's130',
    's131',
    's132',
    's133',
    's134',
    's136',
    's137',
    's138',
    's143',
    's144',
    's145',
    's147',
    's148',
    's149',
    's150',
    's151',
    's152',
    's153',
    's154',
    's155',
    's156',
    's157',
    's158',
    's159',
    's160',
    's161',
    's162',
    's163',
    's164',
    's165',
    's188',
    's189',
    's190'
]

DROP_LIST = [
    's3',
    's4',
    's166',
    's5',
    's6',
    's8',
    's11',
    's13',
    's16',
    's30',
    's113',
    's114',
    's116',
    's135',
    's139',
    's141'
]

CENSORED_MAP = {
    1: [   # AIDS
        's137',         # Did [name] have a bulging fontanelle during the illness that led to death?
    ],
    3: [   # Diarrhea/Dysentery
        's999933',      # word_pneumonia
        's135991',      # unconsciousness started >24hrs before death
        's123',         # Was the cough very severe?
        's137',         # Did [name] have a bulging fontanelle during the illness that led to death?
    ],
    5: [   # Encephalitis
        's999933',      # word_pneumonia
        's118',         # Did the frequent loose or liquid stools continue until death?
    ],
    9: [   # Malaira
        's999933',      # word_pneumonia
        's999914',      # word_dehydr
        's137',         # Did [name] have a bulging fontanelle during the illness that led to death?
    ],
    10: [   # Measles
        's137',         # Did [name] have a bulging fontanelle during the illness that led to death?
    ],
    11: [   # Meningitis
        's999933',      # word_pneumonia
    ],
    12: [   # Other Cancers
        's999914',      # word_dehydr
        's137',         # Did [name] have a bulging fontanelle during the illness that led to death?
    ],
    13: [   # Other Cardiovascular Diseases
        's137',         # Did [name] have a bulging fontanelle during the illness that led to death?
        's129',  # During the illness that led to death, did he/she have indrawing of the chest?
        's131',  # Breathing: Grunting
        's133',  # Did [name] experience any generalized convulsions or fits during the illness that led to death
        's134',  # Was [name] unconscious during the illness that led to death?
        's999919',  # word_fever
        's999933',  # word_pneumonia
        's136',  # Did [name] have a stiff neck during the illness that led to death?
        's135991',  # unconsciousness started >24hrs before death
        's189',  # Mother had positive HIV test
        's190',  # Has the deceased's (biological) mother ever been told she had AIDS by a health worker?
    ],
    15: [   # Other Digestive Diseases
        's999933',      # word_pneumonia
        's137',         # Did [name] have a bulging fontanelle during the illness that led to death?
    ],
    17: [   # Pneumonia
        's99991',       # word_abdomen
        's999926',      # word_jaundic
        's99999',       # word_cancer
    ],
}

REQUIRED_MAP = {}
