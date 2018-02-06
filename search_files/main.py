# Python code to search .mp3 files in current
# folder (We can change file type/name and path
# according to the requirements.
# import os
#
# # This is to get the directory that the program
# # is currently running in.
# dir_path = os.path.dirname(os.path.realpath(__file__))
#
# for root, dirs, files in os.walk('d:\\'):
#     for file in files:
#
#         # change the extension from '.mp3' to
#         # the one of your choice.
#         if file.endswith('.mp3'):
#             print(root + '/' + str(file))

import glob
file_list = glob.glob('d:\*\\*.*')
print(file_list)