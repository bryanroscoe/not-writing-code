# Lesson spec: Writing Code Is Dead

The course is a slide-led lesson player. Each module in the repo becomes one lesson: a short run of screens, one idea per
screen, a real visual on most, and a spoken talk track under every screen. The long module stays behind each screen as a
"Go deeper" link. Lesson 01 is finished and approved by Bryan. It is the reference for everything below.

## Files

| What | Path |
|---|---|
| Reference lesson (read it all before writing) | `course/lessons/01.html` |
| Shared CSS and engine (read the CSS; never edit) | `course/shell.html` |
| Your lesson | `course/lessons/NN.html` |
| Build and checks | `python3 -I course/build.py --only NN` writes `course/build/NN.html` |
| Screenshots | `course/shoot.sh NN 0 3 7 done` (and `THEME=light course/shoot.sh ...`) writes `course/shots/` |
| Module sources | `/Users/bryan/Developer/not-writing-code-stages/modules/NN-*.md` |
| Repo rules | `/Users/bryan/Developer/not-writing-code-stages/CONTRIBUTING.md` (Voice, Opinions vs facts, Sourcing) |

Paths starting `course/` are under `/Users/bryan/.t3/scratch/2026-11-16-hey-i-made-a-private-e3b4fe18/prototype/`.
Edit only your own lesson file and your own report. Other agents are writing other lessons at the same time.

## Shape of a lesson

```html
<section class="lesson" data-lesson="NN" data-title="Title as on the course map" data-minutes="M" hidden>
  <style> /* optional; every selector starts with .lesson[data-lesson="NN"] */ </style>
  <script type="application/json" class="say">[["\\bo3\\b", "oh three"]]</script>   <!-- optional, see Talk track -->
  <article class="screen" data-title="Start"> ... </article>
  <article class="screen"> ... </article>        <!-- 12 to 22 content screens -->
  <article class="screen solo" data-title="Done"> ... </article>
  <script> /* optional, see Scripts */ </script>
</section>
```

The first line must match that pattern exactly. `data-minutes` is roughly one minute per content screen.

- **Start screen:** copy lesson 01's. Eyebrow `Stage N · Stage name` (or `Orientation`), `<h1>` title, meta
  `Lesson NN · M min`, `<div class="actions intro-actions">` with the Start button, a `Full notes` link to the module,
  and a visual in `.vis`.
- **Content screens:** `.text` with an eyebrow (the topic, two or three words), an `<h2>` that states the idea as a claim
  ("Chatting with a model never changes its weights", not "Weights"), one or two short paragraphs, and a
  `Go deeper: <topic>` link. Then a `.vis` with the visual. Use `screen solo` only for a screen with no visual.
- **Done screen:** copy lesson 01's. Eyebrow `Lesson NN done`, `<h2>Next: <next lesson title></h2>`, actions: primary
  `<a class="btn primary arrow-r" href="#lesson-MM">Lesson MM</a>`, `<a class="btn" href="#map">Course map</a>`,
  `<button type="button" class="btn" data-go="1">Review</button>`, then the `Full notes` link. Lesson 18 has no next lesson.
- **Talk track:** the last child of every `<article>` is `<div class="talk" hidden>` with `<p>` paragraphs, then at most
  one `<p class="inclass">` for the instructor.

## Content

- Take every fact from the module. If the module is unclear, stale or wrong, don't paper over it: say so in your report.
  Check 2025+ facts against primary sources when you're unsure; don't cite SEO or AI-news sites.
- One idea per screen. Teach the module's core path, not every section. 12 to 22 content screens. List what you left out
  in your report.
- Opinions only where the module marks them as `Bryan's take`, and label them that way on screen. Never invent one.
- Never name a specific employer or client. Write "Truemed" exactly like that if it ever comes up.
- Date anything that will go stale ("as of November 2026").

## Visuals

Most screens need a visual that teaches, not decoration: a diagram, a worked example, a before and after, a real output.
Reuse the shell's components first (read its CSS and see how lesson 01 uses them): `.vis`, `.two`, `.two.wide-r`,
`.chip` with `c1`..`c6`, `.chips`, `.bars`/`.track`/`.num`, `.prompt`/`.caret`, `.doc`, `.msg`, `.node`, `.paths`,
`.frames`, `.stops3`, `.not`, `.remember`, `.cap`, `.note`, `mark`, inline SVG with the `f-*` fill classes.

- New styles go in your lesson's `<style>`, every selector prefixed `.lesson[data-lesson="NN"]`. Colors only from the
  shell's tokens (`var(--accent)`, `var(--t1)`..., `var(--line)`), so dark and light both work.
- Screens must work at 390px wide. Use `@container page (max-width: 600px)` (not `@media`) for narrow layouts.
- Label made-up examples with `<span class="tag">Illustrative</span>`. Say "Real ... output" only for real output you ran
  or the module quotes.
- Avoid `id` attributes. If you need one, prefix it `lNN-`.

## Microcopy (Bryan's rule; he has called this out twice)

Keep microcopy minimal. UI text (taglines, intros, card and status text, captions, tags, button and link labels) names
the thing or the action in a few words. No subtitle that restates the heading, no sentence about how the page works or
where things live, no status notes. Before you finish, reread every caption, tag, label and eyebrow and cut each line the
reader doesn't need. Captions stay only when they teach something the visual can't.

## Voice

An experienced engineer explaining this to a smart student over lunch: direct, plain, short declarative sentences,
contractions, candid about limits. Avoid:

- em dashes (the build rejects them), semicolon chains, stacked parentheticals;
- bold lead-in labels, colon headers, decorative bold;
- reflexive "X, not Y", tidy moral endings, triplets for rhythm, "Here's the thing", "Notice...", "In other words",
  "crucially", "matters", rhetorical questions, "This screen shows...", summary sentences that restate the paragraph;
- stiff words: utilize, leverage, robust, seamless, delve.

## Talk track

It is read aloud by a voice and also shown as text beside the screen. Write for the ear.

- 2 to 5 paragraphs per content screen, each under about 600 characters (the build rejects 1,800+). Roughly 100 to 170
  spoken words per screen. Start and Done get one or two short paragraphs.
- Say what the screen shows and what it means for someone who builds software with agents. Add what the slide can't
  hold: the example, the caveat, the history. Don't read the slide back word for word.
- Short sentences. Spell out what a voice would stumble on when it doesn't hurt the text on screen ("59 times 61",
  "60 squared"). For names that must look one way and sound another, add pairs to the lesson's
  `<script type="application/json" class="say">` list: a JavaScript regex source and its spoken form. The shell already
  says o1, GPT-4o, R1, R1-Zero, GPT-N, CLAUDE.md and "Lesson 0N" correctly.
- `<p class="inclass">`: one line for an instructor: a question to ask the room, a demo to run, or a misconception to
  watch for. Not every screen needs one.

## Scripts

Avoid them. If a visual needs one, put a single `<script>` at the end of the section like lesson 01's:
`const lesson = document.currentScript.closest('.lesson')`, query inside `lesson` only, no globals, and start or stop
anything animated on the screen's `nwc:show` and `nwc:hide` events. Respect `prefers-reduced-motion`.

## Done means

1. `python3 -I course/build.py --only NN` prints no PROBLEMS.
2. You screenshot Start, Done and at least five content screens (the visually heaviest ones) at desktop and phone,
   one of them also in light mode, opened the images, and fixed anything clipped, overflowing or unreadable.
3. You reread every screen's microcopy against the rule above.
4. Your report is written (see your task for its path).
