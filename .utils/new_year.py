import os
from pathlib import Path
from datetime import datetime
import shutil
import subprocess

# Get the current working directory
cwd = os.getcwd()

# Get current year
year = datetime.now().year

# Create a new directory
new_dir = Path(cwd, f"{year}/tests").mkdir(parents=True, exist_ok=True)
new_dir = Path(cwd, f"{year}/data").mkdir(parents=True, exist_ok=True)
try:
    subprocess.check_call('mklink /J "%s" "%s"' % (Path(cwd, str(year), "utils"), Path(cwd, ".utils")), shell=True)
except subprocess.CalledProcessError:
    pass

# Copy file from .utils to new directory
shutil.copy(Path(cwd, ".utils", "day.py"), Path(cwd, f"{year}"))
shutil.copy(Path(cwd, ".templates", "conftest.py"), Path(cwd, f"{year}/tests"))

with Path(cwd, str(year), "README.md").open("w", encoding="utf-8") as f:
    f.write(
        (
            f"# 🎄 Advent of Code {year} 🎄\n\n ## Runtime Error Log\n\n"
            f"### {year}-{datetime.now().month:02d}-{datetime.now().day:02d}\n\n"
        )
    )

with open(Path(Path(__file__).resolve().parent.parent, "README.md"), "r+") as f:
    splitter = "## 🌟 Completion Status 🌟"
    goal_splitter = f"### {year-1}"
    old_readme = f.read()

    if str(year) in old_readme:
        print("Already updated!")
        exit()

    intro, completion_status = old_readme.split(splitter)

    intro, goals = intro.split(goal_splitter)

    new_goals = f"\n### {year}\n\n\n"

    new_year_head = f"\n### [{year}](./{year}/)"

    comment = " <!--{y}.{d:02d}.{p}--> |"

    new_table = [
        "\n\n|        | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th | 11th | 12th | 13th |",
        "\n| ------ |" + " --- |" * 13,
        "\n| Part 1 |" + "".join((comment.format(y=year, d=day, p=1) for day in range(1, 14))),
        "\n| Part 2 |" + "".join((comment.format(y=year, d=day, p=2) for day in range(1, 14))),
        "\n\n|        | 14th | 15th | 16th | 17th | 18th | 19th | 20th | 21st | 22nd | 23rd | 24th | 25th |",
        "\n| ------ |" + " --- |" * 12,
        "\n| Part 1 |" + "".join((comment.format(y=year, d=day, p=1) for day in range(14, 26))),
        "\n| Part 2 |" + "".join((comment.format(y=year, d=day, p=2) for day in range(14, 26))),
        "",
    ]

    new_text = [intro, new_goals, goal_splitter, goals, splitter, new_year_head] + new_table + [completion_status]

    f.seek(0)
    f.write("".join(new_text))
