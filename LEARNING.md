# Cosecha Learning Notes

## Terminal
- WSL Ubuntu prompt looks like: `organ@Cosecha:~$`
- Windows CMD looks like: `C:\Users\organ>`
- PowerShell looks like: `PS C:\Users\organ>`
- Ctrl+C cancels a running command
- If stuck, press Enter a few times then Ctrl+C

## API Keys
- OpenAI keys start with `sk-proj-`
- Anthropic/Claude keys start with `sk-ant-`
- They are different companies, different keys, never interchangeable
- Keys can live in: .env file, .bashrc, or system environment
- System environment variable overrides .env file

## Markdown
- Plain text format, files end in .md
- `**bold**`, `# heading`, `- bullet point`
- GitHub renders it beautifully
- No lock-in, works in any text editor

## Windows vs WSL
- Two operating systems running at once
- WSL Ubuntu = where all dev work lives (Python, Git, Cosecha)
- Windows = Microsoft tools, browser, desktop apps
- They have separate file systems
## Terminal Tips
- Can paste multiple commands at once — terminal runs them in sequence

## Progress Notes

### May 16, 2026
- Fixed Cosecha weekly summary — API key was in three places at once (.env, .bashrc, system environment)
- Learned: system environment variable overrides .env file
- Learned: OpenAI keys start with sk-proj-, Anthropic/Claude keys start with sk-ant-
- Switched entirely to Claude API — single API for everything
- Added Spanish translation to weekly summary via Claude
- Generated bilingual HTML journal entries from Cosecha
- Built organiclocalfood.org from scratch in HTML/CSS
- Two sites on one domain — Puyallup (organiclocalfood.org) + El Salvador (organiclocalfood.org/elsalvador/)
- Puyallup site: Tahoma background, First Nations land acknowledgment, bilingual EN/ES toggle
- El Salvador site: bold Latin energy, tropical colors, ES/EN toggle
- Connected GitHub to Vercel — auto-deploys on every push
- Added photo gallery with lightbox — 23 photos from WSU Master Gardener Sale
- Added event info and WSU Extension links to journal page
- Learned: Chrome DevTools Console (F12) runs JavaScript live in browser — temporary, doesn't save
- Learned: can paste multiple terminal commands at once
- Created STATUS.md and LEARNING.md in Cosecha repo