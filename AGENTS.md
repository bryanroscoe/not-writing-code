# Agent instructions

This repo is a Markdown knowledge base, not code. Keep this file short ([module 07](modules/07-context-engineering.md) explains why).

- Follow [CONTRIBUTING.md](CONTRIBUTING.md): module template, voice, opinion callouts, sourcing.
- Opinions belong only in `> **Bryan's take:**` callouts. Don't invent new ones. Ask.
- Verify 2025+ facts against primary sources. Don't cite SEO or auto-generated "AI news" sites.
- Update the module's "Last checked" date when you re-check its facts.
- After editing any module's "Terms introduced" or "Sources" section, regenerate `reference/glossary.md` and the paper lists in `reference/papers.md`.
- Before committing, check that relative links and heading anchors resolve: `python3 scripts/check_links.py`.
- Slides in `slides/` follow `slides/README.md` and take every fact from their module. If a module changes, check its deck.
- The site build (`python3 scripts/build_site.py`) runs MkDocs in strict mode; fix its warnings, don't silence them.
- Never name a specific employer or client. Workplace material stays generic.
