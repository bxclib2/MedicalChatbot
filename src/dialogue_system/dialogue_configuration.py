# -*- coding:utf-8 -*-

# DIALOGUE STATUS
DIALOGUE_FAILED = 0
DIALOGUE_SUCCESS = 1
NOT_COME_YET = -1
INFORM_WRONG_DISEASE = 2

# REWORD FOR DIFFERENT DIALOGUE STATUS.
REWARD_FOR_DIALOGUE_FAILED = -100
REWARD_FOR_DIALOGUE_SUCCESS = 100
REWARD_FOR_NOT_COME_YET = 0
REWARD_FOR_INFORM_WRONG_DISEASE = -100

# Special Actions.
CLOSE_DIALOGUE = "closing"
THANKS = "thanks"

# Slot value for unknown, placeholder and no value matches.
VALUE_UNKNOWN = "UNK"
VALUE_PLACEHOLDER = "placeholder"
VALUE_NO_MATCH = "No value matches."

# RESPONSE
I_DO_NOT_CARE = "I don't care."
I_DO_NOT_KNOW = "I don't know."
I_DENY = "No"

# Constraint Check
CONSTRAINT_CHECK_SUCCESS = 1
CONSTRAINT_CHECK_FAILURE = 0

# Update condition
SUCCESS_RATE_THRESHOLD = 0.3
AVERAGE_WRONG_DISEASE = 7