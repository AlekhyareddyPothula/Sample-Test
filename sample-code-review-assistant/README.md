# Sample Repo — SonarQube Test Fixtures

Just sample source code with intentionally injected issues, so a
SonarQube scan (triggered however your pipeline/Slingshot does it)
has real Critical/Blocker/duplication findings to detect and report on.
No CI workflow is included — hook this repo up to your own trigger.

## What's in `src/`

| File | Issues seeded |
|---|---|
| `app.py` | Hardcoded credentials, SQL injection (x2), bare `except`, OS command injection, dead/unreachable code |
| `billing.py` + `reporting.py` | A ~25-line block copy-pasted between the two files (duplication), plus an unused variable and deeply nested if/elif (high cyclomatic complexity) in `reporting.py` |

`sonar-project.properties` sets the project key to
`sample-code-review-assistant` and points `sonar.sources` at `src/`.
Update the project key there (and wherever your Slingshot config
references it) to match what you register in SonarQube.

## Push it to GitHub

\`\`\`bash
cd sample-code-review-assistant
git init
git add .
git commit -m "Initial commit: SonarQube test fixtures"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
\`\`\`

(Create the empty repo on GitHub first — don't initialize it with a
README, or you'll get a merge conflict on push.)

## Registering it in SonarQube

1. Create a project in SonarQube with key `sample-code-review-assistant`
   (or edit `sonar-project.properties` to match a key you prefer).
2. Point your Slingshot trigger / pipeline at this repo the same way you
   would any other project.
3. Open a PR/MR against `main` to fire your existing workflow — the scan
   should surface the duplication, hardcoded secrets, injection, and
   complexity issues seeded above.
