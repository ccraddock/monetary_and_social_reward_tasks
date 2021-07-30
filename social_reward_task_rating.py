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
image_files = permutation([
    'm-001-2.tiff',
    'm-002-2.tiff',
    'm-003-2.tiff',
    'm-004-2.tiff',
    'm-005-2.tiff',
    'm-006-2.tiff',
    'm-007-2.tiff',
    'm-008-2.tiff',
    'm-009-2.tiff',
    'm-010-2.tiff',
    'm-011-2.tiff',
    'm-012-2.tiff',
    'm-013-2.tiff',
    'm-014-2.tiff',
    'm-015-2.tiff',
    'm-016-2.tiff',
    'w-001-2.tiff',
    'w-002-2.tiff',
    'w-003-2.tiff',
    'w-004-2.tiff',
    'w-005-2.tiff',
    'w-007-2.tiff',
    'w-008-2.tiff',
    'w-009-2.tiff',
    'w-010-2.tiff',
    'w-011-2.tiff',
    'w-012-2.tiff',
    'w-013-2.tiff',
    'w-014-2.tiff',
    'w-015-2.tiff',
    'w-016-2.tiff',
    'w-017-2.tiff'
]).tolist()

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
expInfo = {'participant': '', 'session': ['pre-rating', 'post-rating'], 'order': ['1', '2'], 'ratings file': '' }
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

print(f'{expInfo}', file=sys.stderr)

if expInfo['session'] == 'post-rating':

    if expInfo['ratings file'] == '':
        raise ValueError(f'{expInfo["session"]} requires a ratings file')

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

    print(f'{positive_images}', file=sys.stderr)
    print(f'{ambiguous_images}', file=sys.stderr)

    if expInfo['order'] == '1':
        image_files = positive_images + ambiguous_images
    else:
        image_files = ambiguous_images + positive_images    
   

# Data file name stem = absolute path + name later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + f"data/{expInfo['participant']}_{expInfo['session']}_{expInfo['date']}"

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


image_stim = []

for image_path in image_files:
    image_stim.append(visual.ImageStim(win,
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

# Initialize components for Routine "instructions"
press_to_continue = visual.TextStim(win=win, name='press_to_continue',
    text='Press the spacebar to continue',
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
    set things back to the baseline
    """
    print(f'setting image for {trial_type}', file=sys.stderr)
    components = [{"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 300.0},
                  {"component": image_stim[trial_type], "component_name": "image", "start_time": 0.0, "duration": 300.0}]

    return components, 0

def update_thank_you(trial_type, response_value, components, reward=None):
    center_text.setText("Thank you for completing the ratings.")

    return components, 0

def update_instructions(trial_type, response_value, components, reward=None):

    global expInfo
    
    if expInfo['session'] == 'pre-rating':
        instructions_text = {
            1: 'On the following screens you will see pictures of other participants '
            'in the study. Please rate how much you think you would like the person '
            'in the picture on a scale from 1 to 9, were 1 = "not at all", and '
            '9 = "very much".'
        }
    else:
        instructions_text = {
            1: 'On the following screens you will be re-shown the pictures from the '
            'social game. Please rate HOW GOOD YOU FELT when you saw the image during '
            'the game on a scale from 1 to 9, were 1 = "not good at all", and '
            '9 = "very good".'
        }

    components = [{"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 300.0},
                  {"component": press_to_continue, "component_name": "continue", "start_time": 0.0, "duration": 300.0}]
    
    components.append({"component": center_text, "component_name": "center_text", "start_time": 0.0, "duration": 300.0})
    center_text.setText(instructions_text[trial_type])
  
    return components, 0

def update_waiting_on_scanner(trial_type, response_value, components, reward=None):

    center_text.setText('Waiting on scanner ...')
    return components, 0

###############################################################################
#### THIS IS THE TASK DESCRIPTION
###############################################################################
block_list = [
    {
        "name": "instructions",
        "repetitions": 1,
        "trial_type_list": [1],
        "response_component": key_resp_2,
        "valid_responses": ["space"],

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
        "name": "rate_images",
        "repetitions": len(image_files),
        "trial_type_list": list(range(len(image_files))),
        "response_component": key_resp_2,
        "valid_responses": [str(i) for i in range(1,10)],

        "segments": [
            {
                "name": "show_image_wait_for_rating",
                "components": [
                    {"component": image_stim[0], "component_name": "image", "start_time": 0.0, "duration": 300.0},
                    {"component": key_resp_2, "component_name": "key_resp_2", "start_time": 0.0, "duration": 300.0}
                ],
                "segment_duration": 300.0,
                "update_components": update_image,
                "end_on_keypress": True,
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

user_rating = {}
for block in block_list:

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=list(range(0,block["repetitions"])),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment

    for trial_index in trials:

        print(f"trial {trial_index}", file=sys.stderr)

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
            if block["name"] == "rate_images":
                user_rating[image_files[trial_type]] = block["response_component"].keys

        thisExp.nextEntry()

# completed blocks of trials

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

if expInfo['session'] == 'pre-rating':
    male_images = []
    female_images = []

    for image_name, rating in user_rating.items():
        if image_name[0] == 'm':
            male_images.append((image_name, rating))
        elif image_name[0] == 'w':
            female_images.append((image_name, rating))
        else:
            print(f'Could not classify {image_name}', file=sys.stderr)

    male_images = sorted(male_images, key=lambda x: int(x[1]))
    female_images = sorted(female_images, key=lambda x: int(x[1]))

    male_positive = male_images[:4] + male_images[-4:]
    male_ambiguous = male_images[4:13]

    female_positive = female_images[:4] + female_images[-4:]
    female_ambiguous = female_images[4:13]

    user_rating = {'male_positive': male_images[:4] + male_images[-4:],
                'male_ambiguous': male_images[4:12],
                'female_positive': female_images[:4] + female_images[-4:],
                'female_ambiguous': female_images[4:12],
                }

# these shouldn't be strictly necessary (should auto-save)
with open(filename+'.json', 'w') as ofd:
    json.dump(user_rating, ofd, indent=4)

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
