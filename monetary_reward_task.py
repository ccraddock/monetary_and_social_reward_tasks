#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a heavily edited psychopy script that was first created using \
    PsychoPy3 Experiment Builder (v2021.2.0),
    on Tue 06 Jul 2021 01:38:42 PM CDT
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y


Cameron Craddock modified it to get rid of redundant logic and variables and to make it more
easily adapted to other experiments.
"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

###############################################################################
### CONFIGURATION PARAMETERS
###
### Change the values of these parameters to modify the task.
###
###############################################################################
SCREEN_RESOLUTION = [1920, 1080]
FULLSCREEN = False
LEFT_RESPONSE = '1'  # this is the button to press for a 'lower' guess
RIGHT_RESPONSE = '2'  # this is the butto to press for a 'higher' guess
SCANNER_TRIGGER = '5'
ESCAPE_KEY = 'esc'

###############################################################################
### Done with configuration parameters, do not modify anything past this 
### box.
###############################################################################

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'monetary_reward_task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/cameron/workspace/git_tmp/monetary_reward_task/monetary_reward_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=SCREEN_RESOLUTION, fullscr=FULLSCREEN, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

###############################################################################
#### DEFINE STIMULUS BUIDLING BLOCKS
###############################################################################

arrowVertices=[ [-0.2,0.05], [-0.2,-0.05], [0.0,-0.05], [0.0,-0.1], [0.2,0], [0.0,0.1],  [0.0,0.05] ]
arrow = visual.ShapeStim(win, 
                 lineColor='yellow',
                 lineWidth=2.0, #in pixels
                 fillColor='yellow', #beware, with convex shapes fill colors don't work
                 vertices=arrowVertices,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0,0], #the anchor (rotaion and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 ori=90,
                 autoLog=False)#this stim changes too much for autologging to be useful

instructin_arrow_vertices=[ [-0.1,0.025], [-0.1,-0.025], [0.0,-0.025], [0.0,-0.05], [0.1,0], [0.0,0.05],  [0.0,0.025] ]
down_arrow_instructions = visual.ShapeStim(win, 
                 lineColor='yellow',
                 lineWidth=2.0, #in pixels
                 fillColor='yellow', #beware, with convex shapes fill colors don't work
                 vertices=instructin_arrow_vertices,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0.25,0.25], #the anchor (rotaion and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 ori=90,
                 autoLog=False)#this stim changes too much for autologging to be useful

up_arrow_instructions = visual.ShapeStim(win, 
                 lineColor='yellow',
                 lineWidth=2.0, #in pixels
                 fillColor='yellow', #beware, with convex shapes fill colors don't work
                 vertices=instructin_arrow_vertices,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [-0.25,0.25], #the anchor (rotaion and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 ori=-90,
                 autoLog=False)#this stim changes too much for autologging to be useful

lose_arrow_instructions = visual.ShapeStim(win, 
                 lineColor='red',
                 lineWidth=2.0, #in pixels
                 fillColor='red', #beware, with convex shapes fill colors don't work
                 vertices=instructin_arrow_vertices,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0.375,0.25], #the anchor (rotaion and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 ori=90,
                 autoLog=False)#this stim changes too much for autologging to be useful

no_change_instructions = visual.Circle(win,
                 radius = 0.05,
                 lineColor = 'yellow',
                 lineWidth = 2.0,
                 fillColor = 'yellow',
                 pos = [0.25, 0.25],
                 interpolate = True,
                 opacity = 0.9,
                 autoLog = False)

win_arrow_instructions = visual.ShapeStim(win, 
                 lineColor='green',
                 lineWidth=2.0, #in pixels
                 fillColor='green', #beware, with convex shapes fill colors don't work
                 vertices=instructin_arrow_vertices,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0.125,0.25], #the anchor (rotaion and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 ori=-90,
                 autoLog=False)#this stim changes too much for autologging to be useful

lose_arrow = visual.ShapeStim(win, 
                 lineColor='red',
                 lineWidth=2.0, #in pixels
                 fillColor='red', #beware, with convex shapes fill colors don't work
                 vertices=arrowVertices,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0,0], #the anchor (rotaion and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 ori=90,
                 autoLog=False)#this stim changes too much for autologging to be useful

win_arrow = visual.ShapeStim(win, 
                 lineColor='green',
                 lineWidth=2.0, #in pixels
                 fillColor='green', #beware, with convex shapes fill colors don't work
                 vertices=arrowVertices,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0,0], #the anchor (rotaion and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 ori=-90,
                 autoLog=False)#this stim changes too much for autologging to be useful

no_change = visual.Circle(win,
                 radius = 0.1,
                 lineColor = 'yellow',
                 lineWidth = 2.0,
                 fillColor = 'yellow',
                 pos = [0, 0],
                 interpolate = True,
                 opacity = 0.9,
                 autoLog = False)

result_shape = no_change

# Initialize components for Routine "instructions"
press_to_continue = visual.TextStim(win=win, name='press_to_continue',
    text='Press a button to continue',
    font='Open Sans',
    pos=(0, -.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

key_resp = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixation_text = visual.TextStim(win=win, name='fixation_text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

# Initialize components for Routine "decision"
segment_clock = core.Clock()
card_outline = visual.Rect(
    win=win, name='card_outline',
    width=0.36, height=0.5,
    ori=0.0, pos=(0, 0),
    lineWidth=15.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

card_outline_instructions = visual.Rect(
    win=win, name='card_outline',
    width=0.18, height=0.25,
    ori=0.0, pos=(0, 0.25),
    lineWidth=15.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

card_polygon = visual.Polygon(
    win=win, name='card_outline',
    radius=(0.18, 0.25),
    edges = 8,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

card_text = visual.TextStim(win=win, name='card_text',
    text='?',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0)

card_text_instructions = visual.TextStim(win=win, name='card_text',
    text='?',
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0)

key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "anticipation"
center_text = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

instructions_lower_text = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

###############################################################################
#### FUNCTIONS FOR UPDATING THE STIMULI
###############################################################################

def update_decision(trial_type, response_value, components, reward=None):
    """
    set things back to the baseline
    """
    card_text.setText("?")

    return components, 0

def update_anticipation(trial_type, response_value, components, reward=None):
    """
    There are 4 trial types:
    1. reward, correct response
    2. reward, incorrect response
    3. loss, correct response
    4. loss, incorrect response

    The users response and the trial type are used to determine the value of the chosen card to match
    the desired outcome.  
    """
    orientation = 0
    if trial_type in [1, 2]:

        orientation = -90

    elif trial_type in [3, 4]:

        orientation = 90

    else:
        print(f"Incorrect trial type {trial_type}", file=sys.stderr)
        raise ValueError

    arrow.ori = orientation
    arrow.lineColor = 'yellow'
    arrow.fillColor = 'yellow'

    return components, 0

def update_outcome(trial_type, response_value, components, reward=None):
    """
    There are 4 trial types:
    1. reward, correct response, win arrow
    2. reward, incorrect response, no change
    3. loss, correct response, no change
    4. loss, incorrect response, lose arrow

    The users response and the trial type are used to determine the value of the chosen card to match
    the desired outcome.  
    """

    components.clear()

    components.append({"component": card_outline, "component_name": "card_outline", "start_time": 0.0, "duration": 0.5})
    components.append({"component": card_text, "component_name": "card_text", "start_time": 0.0, "duration": 0.5})

    reward = 0
    result_shape = no_change

    print(f"calling update_outcome with {trial_type} {response_value} {reward}", file=sys.stderr)

    if not response_value:
        
        card_value = np.random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

        center_text.setText("No response!")

        components.append({"component": center_text, "component_name": "center_text", "start_time": 0.51, "duration": 0.5})

    else:
        if trial_type in [1, 3]:
            # the user was correct

            if response_value == LEFT_RESPONSE:
                # the chosen card value should be less than "5"
                card_value = np.random.choice(["1", "2", "3", "4"])

            elif response_value == RIGHT_RESPONSE:
                # the chose card value should be greater than "5"
                card_value = np.random.choice(["6", "7", "8", "9"])

            else:
                print(f"Incorrect response value {response_value}", file=sys.stderr)
                raise ValueError

            if trial_type == 1:
                print(f"Setting result shape to win", file=sys.stderr)
                reward = 1.0
                result_shape = win_arrow

        elif trial_type in [2, 4]:

            # the user was WRONG

            if response_value == LEFT_RESPONSE:
                # the chosen card value should be greater than "5"
                card_value = np.random.choice(["6", "7", "8", "9"])

            elif response_value == RIGHT_RESPONSE:
                # the chose card value should be less than "5"
                card_value = np.random.choice(["1", "2", "3", "4"])

            else:
                print(f"Incorrect response value {response_value}", file=sys.stderr)
                raise ValueError

            if trial_type == 4:
                print(f"Setting result shape to lose", file=sys.stderr)
                reward = -0.5
                result_shape = lose_arrow

        else:
            print(f"Incorrect trial type {trial_type}", file=sys.stderr)
            raise ValueError

        components.append({"component": result_shape, "component_name": "result_shape", "start_time": 0.51, "duration": 0.5})

    card_text.setText(card_value)

    return components, reward

def update_fixation(trial_type, response_value, components, reward=None):
    """
    set things back to the baseline
    """
    center_text.setText("+")

    return components, 0

def update_reward(trial_type, response_value, components, reward=None):

    if not reward or reward < 0:
        reward = 0.0
    center_text.setText(f"You won ${reward}")

    return components, 0

def update_instructions(trial_type, response_value, components, reward=None):

    
    instructions_text = {
        1: 'Hi-Lo Card Game\n\n You will have multiple attempts to win money by '
           'guessing whether the next card drawn from a deck is higher or '
           'lower than 5. The deck contains the cards 1, 2, 3, 4, 6, 7, 8, 9 and is '
           'shuffled before each draw.',
        2: 'When you see the queue card guess whether the next card '
           'will be lower or higher than 5 using the buttons. Use the left button '
           'to guess "lower" and the right button for "higher". Make sure to '
           'respond before the queue card disappears.',
        3: 'After you make your guess, you will see an arrow that indicates how much '
           'you can win or lose for the attempt. An UP arrow means you will '
           'win $1.00 if correct and $0.00 if incorrect. A DOWN arrow '
           'means you will win $0.00 if correct and lose $0.50 if '
           'incorrect.',
        4: 'A card will be selected from the deck and displayed, followed '
           'by a symbol to indicate the outcome. A green arrow means you won '
           '$1.00, a red arrow means you lost $0.50, and a yellow circle means you '
           'won $0.00. "No response" means you failed to make a guess in time.',
        5: 'The total amount you won will be displayed at the end of the game.'
    }

    components = [{"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 300.0},
                  {"component": press_to_continue, "component_name": "continue", "start_time": 0.0, "duration": 300.0}]
    
    if trial_type == 1:
        components.append({"component": center_text, "component_name": "center_text", "start_time": 0.0, "duration": 300.0})
        center_text.setText(instructions_text[trial_type])
    elif trial_type == 2:
        components.append({"component": card_outline_instructions, "component_name": "card_outline", "start_time": 0.0, "duration": 300.0})
        components.append({"component": card_text_instructions, "component_name": "card_text", "start_time": 0.0, "duration": 300.0})
        card_text.setText("?")
        components.append({"component": instructions_lower_text, "component_name": "instructions_lower_text", "start_time": 0.0, "duration": 300.0})
        instructions_lower_text.setText(instructions_text[trial_type])
    elif trial_type == 3:
        components.append({"component": up_arrow_instructions, "component_name": "up_arrow", "start_time": 0.0, "duration": 300.0})
        components.append({"component": down_arrow_instructions, "component_name": "down_arrow", "start_time": 0.0, "duration": 300.0})

        components.append({"component": instructions_lower_text, "component_name": "instructions_lower_text", "start_time": 0.0, "duration": 300.0})
        instructions_lower_text.setText(instructions_text[trial_type])
    elif trial_type == 4:
        components.append({"component": lose_arrow_instructions, "component_name": "lose_arrow", "start_time": 0.0, "duration": 300.0})
        components.append({"component": win_arrow_instructions, "component_name": "win_arrow", "start_time": 0.0, "duration": 300.0})
        components.append({"component": no_change_instructions, "component_name": "no_change", "start_time": 0.0, "duration": 300.0})
        components.append({"component": card_outline_instructions, "component_name": "card_outline", "start_time": 0.0, "duration": 300.0})
        card_outline_instructions.pos = [-0.25, 0.25]
        components.append({"component": card_text_instructions, "component_name": "card_text", "start_time": 0.0, "duration": 300.0})
        card_text_instructions.pos = [-0.25, 0.25]
        card_text_instructions.setText("8")
        components.append({"component": instructions_lower_text, "component_name": "instructions_lower_text", "start_time": 0.0, "duration": 300.0})
        instructions_lower_text.setText(instructions_text[trial_type])

    return components, 0

def update_waiting_on_scanner(trial_type, response_value, components, reward=None):

    center_text.setText('Waiting on scanner ...')
    return components, 0

###############################################################################
#### THIS IS THE TASK DESCRIPTION
###############################################################################
block_list = [
    {
        "repetitions": 4,
        "trial_type_list": [1,2,3,4],
        "response_component": key_resp_2,
        "valid_responses": [LEFT_RESPONSE, RIGHT_RESPONSE, "space"],

        "segments": [
            {
                "name": "instructions",
                "components": [
                    {"component": center_text, "component_name": "instructions", "start_time": 0.0, "duration": 300.0},
                    {"component": press_to_continue, "component_name": "continue", "start_time": 0.0, "duration": 300.0},
                    {"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 300.0}
                ],
                "segment_duration": 300.0,
                "update_components": update_instructions,
                "end_on_keypress": True,
            },
        ]
    },
    {
        "repetitions": 1,
        "trial_type_list": [],
        "response_component": key_resp_2,
        "valid_responses": [SCANNER_TRIGGER],

        "segments": [
            {
                "name": "wait_for_scanner",
                "components": [
                    {"component": center_text, "component_name": "center_text", "start_time": 0.0, "duration": 300.0},
                    {"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 300.0}
                ],
                "segment_duration": 300.0,
                "update_components": update_waiting_on_scanner,
                "end_on_keypress": True,
            },
        ]
    },
    {
        "repetitions": 1,
        "trial_type_list": [],

        "segments": [
            {
                "name": "fixation",
                "components": [
                    {"component": center_text, "component_name": "center_text", "start_time": 0.0, "duration": 20.0},
                ],
                "segment_duration": 20.0,
                "update_components": update_fixation
            },
        ]
    },
    {
        "response_component": key_resp_2,
        "valid_responses": [LEFT_RESPONSE, RIGHT_RESPONSE],
        "repetitions": 24,
        "trial_type_list": np.random.permutation([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]),

        "segments": [
            {
                "name": "decision",
                "components": [
                    {"component": card_outline, "component_name": "card_outline", "start_time": 0.0, "duration": 4.0},
                    {"component": card_text, "component_name": "card_text", "start_time": 0.0, "duration": 4.0},
                    {"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 4.0}
                ],
                "segment_duration": 4.0,
                "update_components": update_decision
            },
            {
                "name": "anticipation",
                "components": [
                    {"component": arrow, "component_name": "anticipation_arrow", "start_time": 0.0, "duration": 6.0},

                ],
                "segment_duration": 6.0,
                "update_components": update_anticipation
            },
            {
                "name": "outcome",
                "components": [
                    {"component": card_outline, "component_name": "card_outline", "start_time": 0.0, "duration": 0.5},
                    {"component": card_text, "component_name": "card_text", "start_time": 0.0, "duration": 0.5},
                    {"component": result_shape, "component_name": "result_shape", "start_time": 0.5, "duration": 0.5},
                ],
                "segment_duration": 1.0,
                "update_components": update_outcome
            },
            {
                "name": "ISI",
                "components": [
                    {"component": center_text, "component_name": "center_text", "start_time": 0.0, "duration": 9.0},
                ],
                "segment_duration": 9.0,
                "update_components": update_fixation
            }
        ]
    },
    {
        "repetitions": 1,
        "trial_type_list": [],

        "segments": [
            {
                "name": "fixation",
                "components": [
                    {"component": center_text, "component_name": "center_text", "start_time": 0.0, "duration": 20.0},
                ],
                "segment_duration": 20.0,
                "update_components": update_fixation
            },
        ]
    },
    {
        "repetitions": 1,
        "trial_type_list": [],

        "segments": [
            {
                "name": "reward",
                "components": [
                    {"component": center_text, "component_name": "center_text", "start_time": 0.0, "duration": 120.0},
                ],
                "segment_duration": 120.0,
                "update_components": update_reward
            },
        ]
    },
]

###############################################################################
#### EXECUTE THE TASK
###############################################################################

# Keep track of the money won and lost
total_reward = 0.0

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

for block in block_list:

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=block["repetitions"], method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=None,
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment

    for trial_index in range(0, block["repetitions"]):

        # update component parameters for each repeat
        if 'response_component' in block and block['response_component']:
            block['response_component'].keys = []
            block['response_component'].rt = []
            _tkeys = []

        if "trial_type_list" in block and len(block["trial_type_list"])>0:
            trial_type = block["trial_type_list"][trial_index]
        else:
            trial_type = 0

        for block_segment in block["segments"]:

            # ------Prepare to start segment -------
            continueRoutine = True
            routineTimer.add(block_segment['segment_duration'])

            # update segment components
            reward = 0.0
            if 'update_components' in block_segment and block_segment['update_components']:
                if "response_component" in block and block["response_component"]:
                    block_segment_components, reward = block_segment['update_components'](
                        trial_type=trial_type, 
                        response_value=block["response_component"].keys,
                        components=block_segment['components'],
                        reward=total_reward)
                else:
                    block_segment_components, reward = block_segment['update_components'](
                        trial_type=trial_type, 
                        response_value=None,
                        components=block_segment['components'],
                        reward=total_reward)
            else:
                block_segment_components = block_segment['components']

            total_reward += reward
            
            print(f"total reward: {total_reward}", file=sys.stderr)

            for thisComponent in block_segment_components:
                thisComponent["component"].tStart = None
                thisComponent["component"].tStop = None
                thisComponent["component"].tStartRefresh = None
                thisComponent["component"].tStopRefresh = None
                # if hasattr(thisComponent["component"], 'status'):
                thisComponent["component"].status = NOT_STARTED
                
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            segment_clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = segment_clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=segment_clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                waitOnFlip = False
                for thisComponent in block_segment_components:
                # *component* updates
                    if thisComponent["component"].status == NOT_STARTED and tThisFlip >= thisComponent["start_time"]-frameTolerance:
                        # keep track of start time/frame for later
                        thisComponent["component"].frameNStart = frameN  # exact frame index
                        thisComponent["component"].tStart = t  # local t and not account for scr refresh
                        thisComponent["component"].tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(thisComponent["component"], 'tStartRefresh')  # time at next scr refresh
                        if hasattr(thisComponent["component"], 'setAutoDraw'):
                            thisComponent["component"].setAutoDraw(True)
                        elif isinstance(thisComponent["component"], keyboard.Keyboard):
                            thisComponent["component"].status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(thisComponent["component"].clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(thisComponent["component"].clearEvents, eventType='keyboard')  # clear events on next screen flip

                    if thisComponent["component"].status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > thisComponent["component"].tStartRefresh + thisComponent["duration"]-frameTolerance:
                            # keep track of stop time/frame for later
                            thisComponent["component"].tStop = t  # not accounting for scr refresh
                            thisComponent["component"].frameNStop = frameN  # exact frame index
                            win.timeOnFlip(thisComponent["component"], 'tStopRefresh')  # time at next scr refresh
                            if hasattr(thisComponent["component"], 'setAutoDraw'):
                                thisComponent["component"].setAutoDraw(False)
                            elif isinstance(thisComponent["component"], keyboard.Keyboard):
                                thisComponent["component"].status = FINISHED

                if "response_component" in block and block["response_component"]:
                    if block["response_component"].status == STARTED and not waitOnFlip:
                        theseKeys = block["response_component"].getKeys(keyList=block["valid_responses"], waitRelease=False)
                        _tkeys.extend(theseKeys)
                        if len(_tkeys):
                            block["response_component"].keys = _tkeys[-1].name  # just the last key pressed
                            block["response_component"].rt = _tkeys[-1].rt
                            if 'end_on_keypress' in block_segment and block_segment["end_on_keypress"] is True:
                                continueRoutine = False

                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in block_segment_components:
                    if hasattr(thisComponent["component"], "status") and thisComponent["component"].status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending segment -------
            for thisComponent in block_segment_components:
                if hasattr(thisComponent["component"], "setAutoDraw"):
                    thisComponent["component"].setAutoDraw(False)
                trials.addData(thisComponent["component_name"]+".started",
                    thisComponent["component"].tStartRefresh)
                trials.addData(thisComponent["component_name"]+".stopped",
                    thisComponent["component"].tStopRefresh)

            # check responses
            if "response_component" in block and block["response_component"]:
                if block["response_component"].keys in ['', [], None]:  # No response was made
                    block["response_component"].keys = None
                trials.addData(block_segment["name"]+'.keys',block["response_component"].keys)
                if block["response_component"].keys != None:  # we had a response
                    trials.addData(block_segment["name"]+'.rt', block["response_component"].rt)

            # blocks that end on keypress are not non-slip safe, so reset the non-slip timer
            if "end_on_keypress" in block_segment and block_segment["end_on_keypress"] is True:
                routineTimer.reset()

# completed blocks of trials

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
