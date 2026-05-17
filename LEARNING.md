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