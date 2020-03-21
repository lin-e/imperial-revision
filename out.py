import os
import shutil
output_path = os.path.realpath(".") + "/_output/"
total_page = 0
total_line = 0
for d in filter(lambda x : os.path.isdir(x), os.listdir(".")):
    if d in [".git", "_output", "programming"]:
        continue
    print("Copying " + d)
    year = "y" + d[2] + "/"
    shutil.copy(os.path.realpath(d) + "/main.pdf", output_path + year + d + ".pdf")
    cmd = "pdfinfo " + d + "/main.pdf | grep 'Pages' | awk '{print $2}'"
    pages = int(os.popen(cmd).read().strip())
    lines = sum(1 for line in open(os.path.realpath(d) + "/main.tex"))
    total_page += pages
    total_line += lines
    print(d + ": " + str(pages) + " pages")
    print(d + ": " + str(lines) + " lines")
print("Complete!")
print("Total pages: " + str(total_page))
print("Total lines: " + str(total_line))
