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
The _data_ directory is separated by year, and each year is separated by month.<br>
  data/[YYYY]/[MM]/[YYYYMMDD].txt<br>

Each file stores data in the following format.<br>
  [activityName] [activityStartTime]<br>
activityStartTime is in the format HHMM, 24 hour time. This is the list of all valid activities
along with their activityNames (I named them like stocks just for fun) and definitions:
<ol>
<li><b>sleep</b> <i>SLLP</i> - sleeping at night</li>
<li><b>biological functions</b> <i>BIIO</i> - stuff like eating, brushing my teeth, chores, taking a nap</li>
<li><b>working out</b> <i>WOUT</i> - working out or playing sports</li>
<li><b>social time</b> <i>SOCL</i> - hanging out with friends online or offline (club meetings included)</li>
<li><b>shallow work</b> <i>SHAL</i> - quizzes, tests, interviews, or shallow work like watching a lecture or reading for class</li>
<li><b>deep work</b> <i>DEEP</i> - doing deep work, such as a difficult school project, a difficult coding project,
or preparing for an interview</li>
<li><b>YouTube</b> <i>YTBE</i> - watching low quality YouTube videos or browsing Quora/Facebook mindlessly</li>
<li><b>high quality fun</b> <i>FUUN</i> - video games, reading, exploring the Internet, doing relaxing coding projects (like
this one), watching high quality YouTube videos, but only alone</li>
</ol>
