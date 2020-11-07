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
<li><b>lecture</b> <i>LECT</i> either watching a lecture or reading for class</li>
<li><b>obligations</b> <i>OBLG</i> quizzes, tests, interviews</li>
<li><b>working out</b> <i>WOUT</i> working out or playing sports</li>
<li><b>social time</b> <i>SOCL</i> hanging out with friends online or offline (club meetings included)</li>
<li><b>sleep</b> <i>SLEP</i> sleeping at night or taking a nap</li>
<li><b>YouTube</b> <i>YTBE</i> watching low quality YouTube videos</li>
<li><b>reading</b> <i>READ</i> reading for enjoyment (not reading for class)</li>
<li><b>high quality fun</b> <i>FUUN</i> video games, exploring the Internet, watching high quality YouTube videos, but only alone</li>
</ol>
