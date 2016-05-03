# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""

import os
try:
    import bpy
except ImportError:
    pass

import sys
sys.path.append("/home/maurizio/GitBook/Library/maoz75/gli-appunti/python")
import blender_tests


def get_yoga_files(base_dir="/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/asana_yoga/"):
    raw_list_of_files = os.listdir(base_dir)
    list_of_files = []
    for l in raw_list_of_files :
        if l.find('.jpg')>-1:
            list_of_files.append(l)
    return list_of_files
    
def load_all_in_blender():
    base_dir="/home/maurizio/GitBook/Library/maoz75/gli-appunti/figures/asana_yoga/"
    sequenza = load_sequence(get_yoga_files(base_dir))
    bpy.ops.import_image.to_plane(files=sequenza,
        directory=base_dir, 
        filter_image=True, filter_movie=True, filter_glob="", force_reload=True, 
        use_shadeless=True, use_transparency=True, transparency_method='Z_TRANSPARENCY', alpha_mode='PREMUL', 
        relative=False)
    set_camera_down()

def load_sequence(list_of_files):
    list_of_files_for_planes=[]
    for l in list_of_files:
        list_of_files_for_planes.append({'name':l})
    return list_of_files_for_planes

def select_camera():    
    bpy.ops.object.select_pattern(pattern="Camera")
    
def select_selection():
    return bpy.context.selected_objects

def set_camera_down(camera):
    camera.location[0] = 0
    camera.location[1] = 0
    camera.location[2] = 2
    camera.rotation_euler[0] = 0
    camera.rotation_euler[1] = 0
    camera.rotation_euler[2] = 0

def some_uts():
    help(bpy.data.objects)
    list(bpy.data.objects) #lists data objects present in blender file.
    bpy.data.objects['Camera'].location[0] = 0


def create_timeline(translation_x = -1.77):
    waits = [] # list transient in
    transactions = [] # list of pauses
    steps = 12
    for u in range(steps):
        waits.append(20)
        transactions.append(20)
    time_index = 0
    for scene in range(steps):
        bpy.context.scene.frame_current = time_index
        bpy.ops.anim.keyframe_insert_menu(type='__ACTIVE__', confirm_success=True)
        time_index += waits[scene]
        bpy.context.scene.frame_current = time_index
        bpy.ops.anim.keyframe_insert_menu(type='__ACTIVE__', confirm_success=True)
        bpy.ops.transform.translate(value=(translation_x, 0, 0))
        time_index += transactions[scene]
    bpy.context.scene.frame_end = 481
    bpy.context.scene.file_format = 'H264'
    bpy.context.scene.render.filepath = "/tmp/tem3.avi"
    bpy.context.scene.render.resolution_x = 640
    bpy.context.scene.render.resolution_y = 360



def right_sequence():
    blender_tests.set_camera_down(bpy.data.objects['Camera'])
    blender_tests.set_camera_down(bpy.data.objects['Lamp'])
    bpy.data.objects['Camera'].select=True
    bpy.data.objects['Lamp'].select=True    
    blender_tests.load_all_in_blender()
    #create_timeline()

    
    
