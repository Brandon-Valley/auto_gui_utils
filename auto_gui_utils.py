''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line

util_submodule_l = ['focus_utils']  # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules

# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l

''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''

from util_submodules.focus_utils import focus_utils as fu                  ; util_submodule_import_check_count += 1

''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''



import pyautogui as pag
import time






# start = pyautogui.locateCenterOnScreen('del_btn.PNG')#If the file is not a png file it will not work
# print(start)
# pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image



def click_when_appears(img_path, timeout = None):
    start = None
    start_time = time.time()
    
    while(start == None):
        start = pag.locateCenterOnScreen(img_path)#If the file is not a png file it will not work
        
        if timeout != None and time.time() - start_time > timeout:
            raise Exception("ERROR:  Timeout reached: " + str(timeout) + " seconds have passed and the image has not been found in the foreground of the main display:  " + img_path)
        
#     print(start)
    pag.moveTo(start)#Moves the mouse to the coordinates of the image
    pag.click(start)







''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Footer -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
sys.modules = og_sys_modules
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if __name__ == '__main__':
    print('In Main:  auto_gui_utils')
    
    
#     fu.set_foreground('Internet Explorer(2)')
    
    
    
    img_path = "C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\bitbucket_tools\\auto_gui_imgs\\repository_settings_btn.PNG"
    click_when_appears(img_path, timeout = 1)
    
    
    
    
    
    
    
    
    
    
    print('End of Main:  auto_gui_utils')