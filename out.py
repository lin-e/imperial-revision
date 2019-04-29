import os
import shutil
output_path = os.path.realpath(".") + "/_output/"
total_page = 0
for d in filter(lambda x : os.path.isdir(x), os.listdir(".")):
    if d in [".git", "_output", "programming"]:
        continue
    print("Copying " + d)
    shutil.copy(os.path.realpath(d) + "/main.pdf", output_path + d + ".pdf")
    cmd = "pdfinfo " + d + "/main.pdf | grep 'Pages' | awk '{print $2}'"
    pages = int(os.popen(cmd).read().strip())
    total_page += pages
    print(d + ": " + str(pages) + " pages")
print("Complete!")
print("Total pages: " + str(total_page))
