# import os
#
# p = r"Z:\Synthetic movies"
#
#
#
#
#
# for roots, folders, files in os.walk(p):
#     for folder in folders:
#         if folder.startswith("SN"):
#             splited_folder = folder.split("SX")
#             source = os.path.join(roots, folder)
#             joined_folder = "S7".join(splited_folder)
#             destiny = os.path.join(roots, joined_folder)
#
#             os.rename(source, destiny)