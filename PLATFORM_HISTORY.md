Local Organic Food / Cosecha Platform History
1. The original purpose
This started as more than “build a website.”
The real purpose was to create a personal learning platform where you could safely train yourself on modern AI, development workflows, Microsoft/Claude-style tools, automation, and publishing — without using company data, personal accounts, or anything that would create risk.
The guiding principles were:
Controlled complexity.
Understand the machinery first.
No autonomous AI editing.
Local-first development.
Use one API at a time.
Build something real, useful, and yours.
The subject matter became your farm life, food growing, El Salvador family farm plans, and local organic food work.
That became the seed of Cosecha and localorganicfood.org.
2. Hardware foundation: the Cosecha laptop
You bought a Lenovo ThinkPad X1 Carbon Gen 13 with Windows 11 Pro and 32GB RAM as your personal AI/workflow training machine.
The idea was:
You need Windows for Microsoft 365, Excel, Copilot-type learning, and general corporate-tool familiarity.
You also wanted Linux because Claude/code/automation workflows are often cleaner in a Linux-style development environment.
So the machine became a hybrid:
Windows 11 Pro for the main operating system
WSL Ubuntu for Linux development
VS Code as the bridge between the two
Git/GitHub for version control
Python virtual environment for Cosecha
Vercel for deployment
Claude API for AI generation
You named the machine:
Cosecha
That was a good name because the computer itself became the harvesting tool: harvesting notes, garden activity, photos, journal entries, and eventually knowledge.
3. Identity and account strategy
You intentionally separated this platform from your normal personal and work life.
You had the domain organiclocalfood.org, and used that as inspiration to create a development identity:
organiclocalfood@outlook.com
The point was not to run your whole life through that account. It was to keep the project clean, separate, and disposable if needed.
You also owned many other strong domains, but organiclocalfood.org was the first one used for the project.
Later, the better domain became clear:
localorganicfood.org
You owned both, but localorganicfood.org is cleaner, stronger, and easier to understand.
Eventually, the platform fully moved from:
organiclocalfood.org
to:
localorganicfood.org
That was the right branding move.
4. Windows setup
The Lenovo started with normal Windows setup screens, updates, and Microsoft prompts.
You worked through:
Windows account creation
Microsoft setup screens
System updates
Basic configuration
Security/common-sense settings
Edge/Chrome discussion
VS Code installation
WSL installation
Ubuntu setup
You were careful not to over-optimize. The goal was not to make the “perfect” machine. The goal was to get a stable, understandable, resettable AI/dev training platform.
That was important. You avoided turning setup into an endless rabbit hole.
5. Linux / WSL setup
You installed WSL and Ubuntu.
At one point, VS Code opened into the WSL environment and you saw something like:
ORGAN [WSL: UBUNTU]
with folders like .cache, .dotnet, and others.
Your WSL prompt became something like:
organ@Cosecha:~$
That meant the Linux side was alive.
You then created the project directory:
~/projects/cosecha
and worked from:
organ@Cosecha:~/projects/cosecha$
This became the home of the Cosecha farm logging system.
6. Git and GitHub foundation
You set up Git and confirmed your name/email.
You created GitHub repositories, eventually including:
misharomero/cosecha
for the farm logging system, scripts, project notes, STATUS.md, and LEARNING.md.
misharomero/organiclocalfood
for the website.
misharomero/finca-familiar
which was later archived because the El Salvador site moved under the main website at:
/elsalvador/
So the final structure became cleaner:
One main website repo:
organiclocalfood
One main live domain:
localorganicfood.org
Two sites inside one domain:
localorganicfood.org
localorganicfood.org/elsalvador/
7. VS Code setup
You installed Visual Studio Code and connected it to WSL.
You installed or used the Python extension inside WSL.
You learned how to open the project from Linux into VS Code.
You also worked through the distinction between Windows files and Linux files, including paths like:
/mnt/c/Users/organ/...
and the Linux project path:
/home/organ/projects/cosecha
Eventually, VS Code became your editor for the Cosecha project, while the terminal remained the main place where you ran scripts.
8. Python environment
Inside:
~/projects/cosecha
you created a Python virtual environment:
.venv
You activated it with:
source .venv/bin/activate
Your prompt became something like:
(.venv) organ@Cosecha:~/projects/cosecha$
You used Python 3.12.3.
You installed Python packages, including AI/API-related packages and dotenv support.
The Cosecha scripts began as simple tests, then became useful tools.
Early tests included simple environment checks like:
Cosecha environment is working
AI environment ready
That mattered because it proved Windows → WSL → VS Code → Python → terminal was functioning.
9. Early Cosecha scripts
The first real Cosecha script was a daily note / AI summary tool.
It prompted you with something like:
Write your daily note:
Then it generated an AI summary and saved entries to:
farm_log.txt
Example log format included timestamps like:
2026-04-18 22:16:41 – Checked seedlings and watered the garden.
At this stage, Cosecha was still small, but the architecture was already visible:
You enter human farm notes.
The system stores them.
AI summarizes them.
Those summaries can later become journal material.
10. API confusion and transition
At one point, the system used OpenAI-style code and environment variables such as:
OPENAI_API_KEY
You hit a real authentication problem:
401 AuthenticationError
Incorrect API key provided...
There were also .env formatting issues and Python dotenv parsing errors.
You also saw a VS Code message about terminal environment injection being disabled:
An environment file is configured but terminal environment injection is disabled.
Those were not failures. They were part of learning the machinery.
Eventually, the project philosophy settled on:
Single API: Claude / Anthropic
Your current AI work is powered by Claude, specifically:
claude-haiku-4-5
This simplified the platform.
No more bouncing between multiple AI providers during the learning phase.
11. Cosecha terminal menu
You then upgraded Cosecha from individual commands into a small terminal menu.
The menu eventually looked like this:
🌱 COSECHA SYSTEM READY

1) Daily log
2) Weekly summary
3) Show farm log
4) Open project folder
5) Backup farm log
6) Search farm log
The choices ran scripts or commands:
Daily log ran:
python ai_summary.py
Weekly summary ran:
python weekly_summary.py
Show farm log ran:
cat farm_log.txt
Open project folder ran:
explorer.exe .
Backup copied:
farm_log.txt
to:
farm_log_backup.txt
Search used:
grep -i
That was a big step because Cosecha stopped being “some scripts” and became a small usable application.
12. Weekly summary pipeline
Then the weekly summary system came together.
The weekly script reads the farm log, uses Claude to generate a summary, translates or creates Spanish content, and saves outputs.
Current output types include:
weekly .txt summaries
weekly_data.csv
bilingual HTML journal entries
The important pipeline became:
Daily farm activity
→ Cosecha daily log
→ farm_log.txt
→ weekly_summary.py
→ Claude summary
→ Spanish translation
→ bilingual HTML journal entry
→ website journal page
That is the core engine of the whole platform.
13. Website beginning: organiclocalfood.org
The first live website was:
organiclocalfood.org
Hosted on Vercel.
Auto-deployed from GitHub.
You worked through DNS, SSL, propagation, and Vercel deployment issues.
There was a 404 issue at one point:
404: NOT_FOUND
There was also an SSL/certificate challenge issue:
We could not generate a cert for organiclocalfood.org because the required http-01 challenge failed.
You correctly suspected DNS propagation time was involved.
You also asked about SSL, and learned that SSL/HTTPS is what lets the browser trust the site and show it securely.
Eventually, the custom domain worked.
That was the first real web publishing milestone.
14. Website structure
The website became more than a homepage.
It developed into two connected but visually distinct sites:
Main Puyallup Valley site
Originally on organiclocalfood.org, now on:
localorganicfood.org
Theme:
Pacific Northwest
Tahoma / Mt. Rainier
Puyallup Valley
local growing
First Nations land acknowledgment
bilingual English/Spanish toggle
journal
gallery
history
El Salvador / Finca Familiar site
Originally considered as a separate repo/site, later folded into the main website at:
localorganicfood.org/elsalvador/
Theme:
El Salvador
campo life
family farm
San Vicente / Río Lempa feel
bold Latin/tropical design
Spanish/English toggle
photo gallery
family/finca identity
This was a good architecture decision: one domain, two related identities.
15. Visual design milestones
The main site developed a Pacific Northwest identity.
The El Salvador site developed a warmer, tropical, family-farm identity.
You worked with images and background concepts like:
Mount Rainier overlooking the Puyallup River
Tahoma watching over the valley
El Salvador campo life
San Vicente Volcano and Río Lempa
rural Salvadoran scenes
Eventually both sites had real background images and distinct moods:
localorganicfood.org
cooler, green, PNW, Tahoma/Puyallup Valley
localorganicfood.org/elsalvador/
warmer, colorful, tropical, campo/family farm
The design became meaningful instead of generic.
16. First major launch
The site went live with:
Custom domain
Vercel deployment
GitHub auto-deploy
Earthy green design
Bilingual pages
Journal entry
Farm data
Navigation
Photos
At that point, the system was no longer theoretical.
You had:
Your hands in the dirt
→ Cosecha log
→ AI weekly summary
→ bilingual journal
→ GitHub
→ Vercel
→ live public website
That was the first true end-to-end platform.
17. Documentation
You also created project documentation.
Important files include:
STATUS.md
LEARNING.md
These are versioned in GitHub in the Cosecha repo.
That matters because the project is not just code. It is also a learning record.
STATUS.md captures where things stand.
LEARNING.md captures what you are learning and why.
That fits the larger purpose: this is a training platform for you, not just a website.
18. Master Gardener Sale gallery
The journal/photo system grew with real-world content from the WSU Pierce County Master Gardener Annual Plant Sale.
The gallery included:
23 photos
from:
May 2–3, 2026
The journal page also included event information and links to WSU Extension and the Master Gardener Foundation.
That gave the site credibility and local grounding.
It was no longer just your farm notes. It became a record of local growing culture.
19. First journal entry
The first major live journal entry was:
May 13, 2026 — “tomato week”
That entry represented the Cosecha pipeline becoming real.
It had:
English
Spanish
farm context
journal format
public website presence
That was a landmark because it proved your farm logging system could produce publishable web content.
20. Domain migration: organiclocalfood.org to localorganicfood.org
You later decided to move from:
organiclocalfood.org
to:
localorganicfood.org
This was a strong branding decision.
Why?
Local Organic Food is cleaner.
It sounds more like a public-facing project.
It is easier to remember.
It puts “local” first, which fits the Puyallup Valley identity.
It still leaves room for El Salvador because “local” can mean local to place, family, and land — not just Tacoma/Puyallup.
The Vercel domain setup eventually showed:
localorganicfood.org
www.localorganicfood.org
organiclocalfood.org
organiclocalfood.vercel.app
with redirects/production configuration.
The important end state:
localorganicfood.org became the real home.
21. El Salvador site integration
The El Salvador site lives at:
/elsalvador/
This was better than maintaining a separate active repo.
The older repo:
finca-familiar
was archived.
The El Salvador content now sits under the same umbrella brand.
This means the platform has two living branches:
Puyallup Valley food/garden/history/journal
El Salvador finca/family/campo/land
That reflects your actual life: Pacific Northwest growing and El Salvador family land stewardship.
22. May 18, 2026 platform state
As of the latest update, here is what got done:
May 18 journal entry published
Puyallup Valley history page built
All navigation links fixed across all pages
El Salvador lightbox fixed and cleaned up
Arrow navigation added to both photo galleries
Domain fully moved to localorganicfood.org
“Local Organic Food” branding consistent everywhere
Both sites are now looking solid.
This is the current public platform:
localorganicfood.org
Main Local Organic Food / Puyallup Valley site.
localorganicfood.org/elsalvador/
Finca Familiar / El Salvador site.
23. Current platform architecture
Here is the platform as it stands today.
Hardware
Lenovo ThinkPad X1 Carbon Gen 13
Windows 11 Pro
WSL Ubuntu
Used as personal AI/dev training machine
Named Cosecha
Local development
Windows
WSL Ubuntu
VS Code
Git
Python 3.12
Python virtual environment
Terminal menu
Local project folder:
~/projects/cosecha
AI layer
Claude API
Model:
claude-haiku-4-5
Used for:
farm note summaries
weekly summaries
Spanish translation
journal generation
Data/logging layer
farm_log.txt
weekly_data.csv
weekly_summary_*.txt
HTML journal entries
Code repositories
misharomero/cosecha
misharomero/organiclocalfood
misharomero/finca-familiar archived
Hosting
Vercel
Auto-deploy from GitHub
Domain
Current main domain:
localorganicfood.org
Former/redirected domain:
organiclocalfood.org
Website structure
/
Main Puyallup Valley site

/elsalvador/
El Salvador / Finca Familiar site
24. What you actually built
You built a small but real publishing platform.
Not just a website.
Not just a farm log.
Not just an AI test.
It is now a complete personal system:
You do real work outside.
You log it locally.
Claude helps summarize and translate.
Python structures the output.
GitHub versions the work.
Vercel publishes it.
The domain presents it publicly.
The website preserves it as a bilingual farm journal.
That is a serious platform.
25. The bigger meaning
The platform now connects several parts of your life:
Your Tacoma/Puyallup growing life
Your El Salvador family farm vision
Your AI training goals
Your finance/controls mindset
Your desire to understand the machinery
Your long-term “gentleman farmer” plan
Your family legacy work
Your local food identity
The important thing is that you did not just “use AI.”
You built an AI-assisted workflow where you still understand the pieces.
That is exactly the right direction for your long-term goal: practical, grounded, controlled use of AI and automation.
26. Current summary
As of today, the platform is:
Hardware complete.
Development environment working.
Cosecha logging system operational.
Claude weekly summary pipeline working.
Spanish/bilingual journal generation working.
GitHub version control working.
Vercel deployment working.
localorganicfood.org live.
Puyallup Valley site solid.
El Salvador site solid.
Navigation fixed.
Galleries improved.
Branding consistent.
Domain migration complete.
The next natural phase is no longer “setup.”
The next phase is:
content rhythm and automation discipline.
Log tomatoes.
Log weekly farm work.
Publish journal entries.
Add El Salvador family farm content.
Keep the system understandable.
Improve slowly, one controlled layer at a time.
