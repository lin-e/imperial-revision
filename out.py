import os
import shutil

exclude = [ "co000" ]

output_path = os.path.realpath(".") + "/_output/"
total_pages = { }
total_lines = { }
for d in filter(lambda x : os.path.isdir(x), os.listdir(".")):
    if not (d[0:2] == "co" and d[2].isdigit()) or d in exclude:
        continue
    print("Copying " + d)
    year = "y" + d[2] + "/"
    shutil.copy(os.path.realpath(d) + "/main.pdf", output_path + year + d + ".pdf")
    cmd = "pdfinfo " + d + "/main.pdf | grep 'Pages' | awk '{print $2}'"
    pages = int(os.popen(cmd).read().strip())
    lines = sum(1 for line in open(os.path.realpath(d) + "/main.tex"))
    total_pages["y" + d[2]] = total_pages.get("y" + d[2], 0) + pages;
    total_lines["y" + d[2]] = total_lines.get("y" + d[2], 0) + lines;
    print(d + ": " + str(pages) + " pages")
    print(d + ": " + str(lines) + " lines")
print("Complete!")
print("Total pages:")
for key, val in total_pages.items():
    print("  " + key + ": " + str(val))
print("Total lines:")
for key, val in total_lines.items():
    print("  " + key + ": " + str(val))
