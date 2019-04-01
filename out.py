import os
import shutil
output_path = os.path.realpath(".") + "/_output/"
for d in filter(lambda x : os.path.isdir(x), os.listdir(".")):
    if d in [".git", "_output"]:
        continue
    shutil.copy(os.path.realpath(d) + "/main.pdf", output_path + d + ".pdf")