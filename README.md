# Welcome to LifeData
LifeData is my project to study my productivity using the scientific method.
Not productivity in general but specifically _my_ productivity. Currently, I
want to test two hypotheses:
<ol>
  <li>Sleeping earlier increases <i>my</i> productivity</li>
  <li>Taking a forced break at night increases <i>my</i> productivity</li>
</ol>

This repository will hold the scripts I use to log my time, analyze the data, and present
it visually. Additionally, it will hold non-code documents with my findings, as well as
the raw data I have gathered.

## Data Files
The _data_ directory is separated by year, and each year is separated by month.
```
data/[YYYY]/[MM]/[YYYY_MM_DD].txt
```

Each file stores data in the following format.
```
[activityName] [activityStartTime]
```
activityStartTime is in the format HH_MM, 24 hour time. This is the list of all valid activities
along with their activityNames (I named them like stocks just for fun) and definitions:
<ol>
<li><b>sleep</b> <i>SLLP</i> - sleeping at night</li>
<li><b>biological functions</b> <i>BIOL</i> - stuff like eating, brushing my teeth, chores, taking a nap</li>
<li><b>working out</b> <i>WOUT</i> - working out or playing sports</li>
<li><b>social time</b> <i>SOCL</i> - hanging out with friends online or offline (club meetings included)</li>
<li><b>shallow work</b> <i>SHAL</i> - quizzes, tests, interviews, or shallow work like watching a lecture or reading for class</li>
<li><b>deep work</b> <i>DEEP</i> - doing deep work, such as a difficult school project, a difficult coding project,
or preparing for an interview</li>
<li><b>YouTube</b> <i>YTBE</i> - watching low quality YouTube videos or browsing Quora/Facebook mindlessly</li>
<li><b>high quality fun</b> <i>FUNN</i> - video games, reading, exploring the Internet, doing relaxing coding projects (like
this one), watching high quality YouTube videos, but only alone</li>
<li><b>unknown</b> <i>UNKN</i> - when the activity at this time is unknown</li>
</ol>

Additionally, _data/prevActivityName.txt_ stores a single line with the current activity. This activity will be automatically entered
into the new day's file as
```
[prevActivityName] 00_00
```
once the first command is issued that day.

All datetimes are local.

## Logging Activities
To log an activity, use the command
```
python3 lifelog.py [activityName]
```
which will run the Python script logging/lifelog.py. The script will automatically gather the current local date and time and create
a new file in the appropriate directory, if necessary, and append a line to the file. It will then update _data/prevActivityName.txt_.
I recommend making a script in ~/bin which runs
```
python3 ~/Your/Path/To/LifeData/logging/lifelog.py $0
```
for convenience.
