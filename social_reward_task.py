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
prefs.hardware['audioLib'] = ['PTB']
from psychopy import gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

# import numpy as np  # whole numpy lib is available, prepend 'np.'
# from numpy import (sin, cos, tan, log, log10, pi, average,
#                    sqrt, std, deg2rad, rad2deg, linspace, asarray)
# from numpy.random import random, randint, normal, shuffle, choice as randchoice
from numpy.random import permutation, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
from operator import itemgetter
from psychopy.hardware import keyboard
import json
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

image_path_prefix = "images/"
image_files = []

###############################################################################
### Done with configuration parameters, do not modify anything past this 
### box.
###############################################################################

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'social_reward_task_rating'  # from the Builder filename that created this script
expInfo = {'participant': '', 'order': ['1', '2'], 'ratings file': '' }
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

if expInfo['ratings file'] == '':
    raise ValueError(f'{expName} requires a ratings file')

if not os.path.isfile(expInfo['ratings file']):
    raise ValueError(f'{expInfo["ratings file"]} does not exist')

with open(expInfo['ratings file'], 'r') as infd:
    user_ratings = json.load(infd)

if 'male_positive' not in user_ratings or 'female_positive' not in user_ratings \
    or 'male_ambiguous' not in user_ratings or 'female_ambiguous' not in user_ratings:
    raise ValueError(f'Could not find pre-ratings in file {expInfo["ratings file"]}, is it the correct file?')

positive_images = permutation([file_info[0] for file_info in user_ratings['male_positive'] + \
    user_ratings['female_positive']]).tolist()

ambiguous_images = permutation([file_info[0] for file_info in user_ratings['male_ambiguous'] + \
    user_ratings['female_ambiguous']]).tolist()

positive_block = ['P']*10 + ['A']*2
ambiguous_block = ['A']*10 + ['P']*2
inter_stimulus_intervals = [1, 3, 5, 7]*3

block_design = []
pos_index = 0
amb_index = 0
for index in range(0,8):
    if (index + int(expInfo['order'])) % 2 == 0:
        stim_indices = [ n % 16 for n in range(pos_index, pos_index+10)] + \
            [ n % 16 for n in [amb_index, amb_index + 1]]
        stim_infos = list(zip(positive_block, stim_indices, 
            permutation(inter_stimulus_intervals).tolist()))
        block_design += [('IBI', 0, 8)] + [stim_infos[index] for index in permutation(range(0,len(stim_infos)))]
        pos_index = (pos_index + 10) % 16
        amb_index = (amb_index + 2) % 16
    else:
        stim_indices = [ n % 16 for n in range(amb_index, amb_index+10)] + \
            [ n % 16 for n in [pos_index, pos_index + 1]]
        stim_infos = list(zip(ambiguous_block, stim_indices, 
            permutation(inter_stimulus_intervals).tolist()))
        block_design += [('IBI',0 ,8)] + [stim_infos[index] for index in permutation(range(0,len(stim_infos)))]
        amb_index = (amb_index + 10) % 16
        pos_index = (pos_index + 2) % 16

# Data file name stem = absolute path + name later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + f"data/{expInfo['participant']}_social_reward_{expInfo['date']}"

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

positive_image_stim = []

for image_path in positive_images:
    positive_image_stim.append(visual.ImageStim(win,
        image=os.path.join(image_path_prefix, image_path), 
        mask=None, 
        units='', 
        pos=(0.0, 0.0), 
        size=None, 
        ori=0.0, 
        color=(1.0, 1.0, 1.0), 
        colorSpace='rgb', 
        contrast=1.0, 
        opacity=None, 
        depth=0))

ambiguous_image_stim = []

for image_path in ambiguous_images:
    ambiguous_image_stim.append(visual.ImageStim(win,
        image=os.path.join(image_path_prefix, image_path), 
        mask=None, 
        units='', 
        pos=(0.0, 0.0), 
        size=None, 
        ori=0.0, 
        color=(1.0, 1.0, 1.0), 
        colorSpace='rgb', 
        contrast=1.0, 
        opacity=None, 
        depth=0))

image_background = visual.Rect(
    win=win, name='card_outline',
    width=1.0, height=0.8,
    ori=0.0, pos=(0, 0),
    lineWidth=15.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

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



def update_image(trial_type, response_value, components, reward=None):
    """
    choose the next image 
    """

    global positive_image_stim
    global ambiguous_image_stim
    global image_background

    if trial_type[0] == 'IBI':
        components = []
    else:
        if trial_type[0] == 'P':
            this_image_stim = positive_image_stim[trial_type[1]]
            image_background.fillColor = 'green'
            image_background.lineColor = 'green'
        else:
            this_image_stim = ambiguous_image_stim[trial_type[1]]
            image_background.fillColor = 'white'
            image_background.lineColor = 'white'

        components = [
            {"component": image_background, "component_name": "image_background", "start_time": 0.0, "duration": 3.0},
            {"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 3.0},
            {"component": this_image_stim, "component_name": "image", "start_time": 0.0, "duration": 3.0}]

    return components, 0

def update_thank_you(trial_type, response_value, components, reward=None):
    center_text.setText("Thank you for playing our social game.")

    return components, 0

def update_instructions(trial_type, response_value, components, reward=None):

    global expInfo
    
    instructions_text = {
        1: 'Social Game\n\n We showed your photo to other study participants '
        'and asked them to rate your likability.', 
        2: 'On the following screens you '
        'will see photos of each of those participants on a colored background '
        'that indicates their rating of you.  A green background means they '
        'rated you as highly likable and a white background means that they have not '
        'rated you yet.', 
        3: 'Please pay attention to the faces in the photos and try to remember '
        'who likes you and has not rated you. Please also press a button when '
        'you see each photo.'
    }


    components = [{"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 300.0},
                  {"component": press_to_continue, "component_name": "continue", "start_time": 0.0, "duration": 300.0}]
    
    components.append({"component": center_text, "component_name": "center_text", "start_time": 0.0, "duration": 300.0})
    center_text.setText(instructions_text[trial_type])
  
    return components, 0

def update_waiting_on_scanner(trial_type, response_value, components, reward=None):

    center_text.setText('Waiting on scanner ...')
    return components, 0

first_trial_flag = True
def update_fixation(trial_type, response_value, components, reward=None):

    global center_text
    global fixation_text
    global first_trial_flag

    components = []
    if trial_type[0] == "IBI":
        if first_trial_flag == True:
            center_text.setText('Faces will begin to show in 8 seconds.')
            first_trial_flag = False
        else:
            center_text.setText('Please take a short break. Faces will begin to show again in 8 seconds.')
        components.append({"component": center_text, "component_name": "IBI_text", "start_time": 0.0, "duration": trial_type[2]})
    else:
        components.append({"component": fixation_text, "component_name": "fixation", "start_time": 0.0, "duration": trial_type[2]})

    return components, 0


###############################################################################
#### THIS IS THE TASK DESCRIPTION
###############################################################################
block_list = [
    {
        "name": "instructions",
        "repetitions": 3,
        "trial_type_list": [1,2,3],
        "response_component": key_resp_2,
        "valid_responses": ["space", LEFT_RESPONSE, RIGHT_RESPONSE],

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
        "name": "wait_for_scanner",
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
        "name": "rate_images",
        "repetitions": len(block_design),
        "trial_type_list": block_design,
        "response_component": key_resp_2,
        "valid_responses": [LEFT_RESPONSE, RIGHT_RESPONSE],

        "segments": [
            {
                "name": "show_image",
                "components": [
                    {"component": image_background, "component_name": "image_background", "start_time": 0.0, "duration": 3.0},
                    {"component": positive_image_stim[0], "component_name": "image", "start_time": 0.0, "duration": 3.0},
                    {"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 3.0}
                ],
                "segment_duration": 3.0,
                "update_components": update_image,
                "end_on_keypress": False,
            },
            {
                "name": "fixation",
                "components": [
                    {"component": fixation_text, "component_name": "fixation", "start_time": 0.0, "duration": 3.0},
                ],
                "segment_duration": None,
                "update_components": update_fixation,
                "end_on_keypress": False,
            },
        ]
    },
    {
        "name": "thank_you",
        "repetitions": 1,
        "response_component": key_resp_2,
        "valid_responses": ["space", "esc"],
        "segments": [
            {
                "name": "thank_you",
                "components": [
                    {"component": center_text, "component_name": "thank_you", "start_time": 0.0, "duration": 300.0},
                    {"component": press_to_continue, "component_name": "continue", "start_time": 0.0, "duration": 300.0},
                    {"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 300.0}

                ],
                "update_components": update_thank_you,
                "segment_duration": 300.0,
                "end_on_keypress": True
            },
        ]
    }

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
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=list(range(0,block["repetitions"])),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment

    for trial_index in trials:

        # update component parameters for each repeat
        if 'response_component' in block and block['response_component']:
            block['response_component'].keys = []
            block['response_component'].rt = []
            _tkeys = []

        if "trial_type_list" in block and len(block["trial_type_list"])>0:
            trial_type = block["trial_type_list"][trial_index]
        else:
            trial_type = 0

        trials.addData("trial_type", trial_type)


        for block_segment in block["segments"]:

            # ------Prepare to start segment -------
            continueRoutine = True

            if block_segment['segment_duration'] is not None:
                routineTimer.add(block_segment['segment_duration'])
            else:
                routineTimer.add(trial_type[2])

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
                trials.addData(block_segment["name"]+thisComponent["component_name"]+".started",
                    thisComponent["component"].tStartRefresh)
                if not thisComponent["component"].tStopRefresh:
                    thisComponent["component"].tStopRefresh = tThisFlipGlobal
                trials.addData(block_segment["name"]+thisComponent["component_name"]+".stopped",
                    thisComponent["component"].tStopRefresh)

            # blocks that end on keypress are not non-slip safe, so reset the non-slip timer
            if "end_on_keypress" in block_segment and block_segment["end_on_keypress"] is True:
                routineTimer.reset()

        # check responses
        if "response_component" in block and block["response_component"]:
            if block["response_component"].keys in ['', [], None]:  # No response was made
                block["response_component"].keys = None
                block["response_component"].rt = None
            trials.addData(block["name"]+'.keys',block["response_component"].keys)
            if block["response_component"].keys != None:  # we had a response
                trials.addData(block["name"]+'.rt', block["response_component"].rt)

        thisExp.nextEntry()

# completed blocks of trials

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
