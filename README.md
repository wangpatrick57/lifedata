# Welcome to LifeData
LifeData is my project to study my productivity using the scientific method. Specifically,
I want to test two hypotheses:
<ol>
<li>Sleeping earlier increases productivity</li>
<li>Taking a forced break at night increases productivity</li>
</ol>

This repository will hold the scripts I use to log my time, analyze the data, and present
it visually. Additionally, it will hold non-code documents with my findings, as well as
the raw data I have gathered.

## The Data Library
The _data_ directory is separated by year, and each year is separated by month.
  data/[YYYY]/[MM]/[YYYYMMDD].txt

Each file stores data in the following format.
  [activityName] [activityStartTime]
activityStartTime is in the format HHMM, 24 hour time. This is the list of all valid activities
along with their activityNames (I named them like stocks just for fun) and definitions:
<ol>
<li>**lecture** _LECT_ either watching a lecture or reading for class</li>
<li>**obligations** _OBLG_ quizzes, tests, interviews</li>
<li>**working out** _WOUT_ working out or playing sports</li>
<li>**social time** _SOCL_ hanging out with friends online or offline (club meetings included)</li>
<li>**sleep** _SLEP_ sleeping at night or taking a nap</li>
<li>**YouTube** _YTBE_ watching low quality YouTube videos</li>
<li>**reading** _READ_ reading for enjoyment (not reading for class)</li>
<li>**high quality fun** _FUUN_ video games, exploring the Internet, watching high quality YouTube videos, but only alone</li>
</ol>
