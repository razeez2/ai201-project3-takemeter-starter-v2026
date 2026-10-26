# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

### Candidate distinctions

From reading posts in the dental hygiene subreddit, I noticed:

1. some posts are about personal experiences, some aren't.
2. most posts involve some need for help.
3. some posts have pictures associated with them.


---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `emotional_support`

**Definition:** Expresses distress or seeks reassurance, validation, or shared experiences, without requesting a concrete solution.

**Example 1:**
>Had a Karen patient today. I called her back and she was immediately disappointed and agitated that I wasn’t her “usual” hygienist, even though there was no alert in her chart that she typically sees the same one. I explained that the hygienist she sees no longer works at the office and she said she wished someone had told her beforehand (fair).

I bring her back to my room, she needs nitrous so I go and get the tanks. The majority of the time I don’t use nitrous, but I know the basics of the tanks so I’m trying to get her situated. I didn’t realize there was a knob to move the oxygen so I had one of the assistants help me. She started being snippy with the assistant after the assistant told her to breath deeply through her nose, she said, “Where else would I breathe?”

I get her started, I numb her teeth with Gingicaine because that’s what she wanted too. She was on a 3-4 MRC but her last visit was 6 months ago, so pocket depths were 4-6 mm localized in her back teeth. I explained my findings to her and she was saying how she typically comes in every 3-4 months but we had her down for 6 months. I told her that we typically make the next appointment after their last one.

I started with hand scaling and then switched to the Cavitron at the end to remove the rest of the stain and tartar. I had the Cavitron at the lowest setting and she was still jumping and fidgeting so I stopped. When I was done, I sat her up and put her on 100% oxygen, and told her I was going to grab the doctor. She told me she wanted to skip the exam, she apparently had another appointment to go to. I walk her up front, she leaves. When I had a spare moment, I went up to the assistant and she told me that the patient called and complained about me.

She said that was the, “worst cleaning she’s ever had”, and she was accusing me of “not using the ultrasonic” and that I must be a “new grad” because I didn’t know how to use nitrous. The assistant flat out said I have been a hygienist for years and that I wasn’t a new grad. The patient said that she wasn’t going to come back and leave a bad review, which she did and I read. She didn’t use my name (thank gosh), but my gosh. I did everything I could, I tried to make her comfortable, get her cleaning done, and be kind as well but none of that mattered because to her I’m just a stupid fuck up.

I’m three years in. I don’t know how much longer I can take this, but there’s little to no career options outside of hygiene. I’m tempted to go back to school and start from scratch.

**Example 2:**
>I think I just need somewhere to rant, I’m really frustrated, embarrassed, and disappointed in myself :(

I’m 19, and my parents never really took me to the dentist as a kid. I finally went myself and, of course, I had a ton of cavities, some pretty bad. It took them 1-2 months to get me in, but in April, I got all my cavities filled. There were about 4-5 across my front teeth. I also got deep cleanings, and now I’m getting cleanings every 4 weeks.

I didn’t have great dental habits before I started going to my dentist—I only brushed in the morning and I didn’t floss. Now, I’m brushing 2x a day (prescription toothpaste at night and flossing at night.)

I went back today because one of my teeth was really sensitive, and I now have another cavity. The dentist said it was pretty small, but to just get it filled to get over with (because she knows I’m an overthinker and would freak out over it.) Regardless, I’m really upset. I thought I was doing super good with my dental hygiene and I was super proud of myself, and I really really really hated getting numbed for the filling before. But now I have to go get numbed again, I’m really upset.

That’s all, I’m just overall very embarrassed and frustrated :,) are cavities normal even if you do everything right? I don’t know if I even did anything wrong or not

### `practical_advice`

**Definition:** Requests information, recommendations, or actions to solve a problem or make a decision.

**Example 1:**

>I was diagnosed with periodontal disease summer of 2025, my hygienist did the pocket depth charting and for a week after I had the most painful inflamed gums. Which was strange bc even though I had poor oral health I had never had that much pain in my gums before. At the time I thought it was just because of the gum disease point blank period. Then came the two sessions of deep cleaning and Arestin and everything went back to normal, no more swelling/ pain. Ever since then I’ve flossed/ brushed/ used a water pik every day. I’ve been to every single 3month cleaning since then and my most recent one was on Wednesday. The hygienist complemented me on my improved oral health, said everything looked great, said my gums looked healthy. Then as I was about to leave she asked to do a pocket depth charting to see if the numbers had improved. She said a good amount of them had and overall there was improvement. Not even an hour after the appointment my gums started to swell and it’s been 3 days and they haven’t improved in the slightest. They are super inflamed and painful and I’m just so confused on what could have caused this? It seemingly all stems from the pocket charting, like could she have disturbed bacteria and just reignited the infection? Will I have to go through with the very expensive deep cleaning again? Im very worried because it’s the weekend and no dentists are open and my gums are so swollen that I’m starting to see recession. Very confused and would love any input. Thank you

**Example 2:**
>How many hours do you guys work a week?
I’m only at 32 hours average, and it’s been mentally hard to do 40 (burn out).

### The hardest boundary

**Which two labels:** `emotional_support` and `practical_advice`.

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->
     If a post requests concrete information or an action to take, label it practical_advice, even if it also expresses distress. If it mainly seeks understanding, reassurance, or solidarity, label it emotional_support.



---

## The Dataset

**Where the posts came from:** Public posts from [r/DentalHygiene](https://www.reddit.com/r/DentalHygiene/), manually copied into chat and formatted into `labels.csv`. The dataset is one unsplit file; the notebook will make the training/validation/test split.

**Collection limit:** I stopped collecting because I was running out of time. I currently have 104 posts, below both the normal 200-post requirement and the 150-post stop-rule minimum. This is an incomplete collection milestone, not fulfillment of the stop rule. A smaller dataset will also make held-out scores less stable.

**How I labelled them:** I supplied the early labels myself, and AI entered them and formatted the CSV. There are 61 rows recorded as `cold`; this records my own label choices, but I still need to verify that at least 20 were assigned independently before any AI labeling help. Later, I asked AI to pre-label posts using my definitions. The remaining 43 rows are marked `AI pre-labeled; needs human review`. I have not yet recorded completion of that review. Two rows have rejoined passages that also need checking against the original posts.

**Counts per label:**

| Label | Count | Share |
|---|---:|---:|
| `emotional_support` | 54 | 51.9% |
| `practical_advice` | 50 | 48.1% |
| **Total** | **104** | **100%** |

Neither label exceeds 70%. Exact duplicate text, empty text, blank labels, label spelling, and CSV structure were checked. One near duplicate differing only in its first letter was removed, keeping the user-labeled version. Complete source text still needs verification for uncertain excerpts; `incomplete_posts.txt` holds excluded fragments and a possible alternate version.

**Three hard cases — AI-drafted for my review**

These are proposed boundary analyses, not claims that I have independently reviewed or accepted the reasoning.

**1. Distress plus a specific request for help flossing**

> *Post excerpt:* “I’m panicking. I don’t want to lose my teeth. (I have gingivitis.)” ... “Gonna do some research and see what’s out there but if anyone has advice, please share 🥲”
>
> *Could have been:* `emotional_support` or `practical_advice`.
>
> *Current AI label and reasoning:* `practical_advice`. The author expresses anxiety but also describes difficulty using floss and explicitly asks for advice. The concrete request takes priority under the decision rule.
>
> *My review:* Pending.

**2. Anxiety about brushing, without a specific request for a technique**

> *Post:* “I have a very bad habit of passing out at night and then brushing my teeth in the morning.How worried should I be? I dont have gingivitis thankfully no gum bleeding. I am a lot better than I was but I still do these stupid things. Thanks for letting me ask and vent.”
>
> *Could have been:* `emotional_support` or `practical_advice`.
>
> *Current AI label and reasoning:* `emotional_support`. The main request appears to be reassurance about worry rather than a concrete change to the routine. Review whether “How worried should I be?” should instead count as a request for factual risk information, and clarify the rule consistently.
>
> *My review:* Pending.

**3. Burnout with a practical question at the end**

> *Post excerpt:* “This week has been hell on earth!” ... “If you are a hygienist and find time to go to your gym after work even if it’s crowded, and come home and cook real food, I applaud you. How do you do it.”
>
> *Could have been:* `emotional_support` or `practical_advice`.
>
> *Current AI label and reasoning:* `practical_advice`. Most of the post vents, but the final question can be read as asking for concrete strategies to manage work, exercise, and meals. Review whether it is a literal request or a rhetorical expression of exhaustion.
>
> *My review:* Pending.

---

## The Training Run

**Base model:** `distilbert-base-uncased`.

**Environment and device:** Ran sections 1–5 of `takemeter.ipynb` using this project's `.venv/bin/python`. The notebook cells were executed sequentially by a local runner, with outputs saved back into the notebook. `results.json` records `mps`, Apple Silicon GPU (MPS), with PyTorch 2.14.1. Hardware can affect results even when the seed is unchanged.

**Settings:** 3 epochs, learning rate `2e-5`, batch size 16, maximum length 128 tokens, seed 42.

**Anything I changed from the defaults, and why:** Only the label map was changed to `emotional_support` and `practical_advice`. Training hyperparameters stayed at their defaults. Whole posts remain in the CSV, but the model reads at most 128 tokens per post; later requests in long posts can be truncated.

**Split sizes:** Stratified 70/15/15 splitting produced 72 training posts, 16 validation posts, and 16 held-out test posts.

| Label | Train | Validation | Test |
|---|---:|---:|---:|
| `emotional_support` | 38 | 8 | 8 |
| `practical_advice` | 34 | 8 | 8 |
| **Total** | **72** | **16** | **16** |

Each label has only 8 test examples, so scores may change substantially across seeds. The dataset check found no `[FIX ME]` issues but warned that 104 posts is below the submission minimum. Unreviewed AI labels and uncertain source excerpts remain limitations of this preliminary run.

**Run status:** Training and held-out evaluation completed. `results.json` and `test_split.csv` were generated. Sections 6–7 were not run, and interpretation against the criteria is deferred to unit 6. The initial sandbox attempt could not access Hugging Face; the successful retry used network access and detected the MPS GPU.

---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* Eight borderline dental-hygiene posts to stress-test my labels.
- *What came back:* Fictional examples mixing frustration, reassurance, factual questions, and requests for solutions.
- *What I changed:* I shifted from venting versus advice requests to emotional support versus practical advice, and wrote a rule prioritizing concrete requests over emotional tone. The fictional posts were not added to the dataset.

**Moment 2**

- *What I asked for:* CSV formatting for copied Reddit posts, followed by pre-labeling later batches.
- *What came back:* A CSV with my early label choices entered and later AI label suggestions explicitly marked for review. AI also drafted three boundary analyses above.
- *What I changed:* I standardized the label names to `emotional_support` and `practical_advice`. Review and correction of all AI suggestions is still pending.

**Pre-labelling disclosure:** AI helped format and separate pasted posts, entered labels I supplied, and pre-labeled later posts. There are currently 43 AI-pre-labeled rows awaiting human review. AI also rejoined two interleaved posts; those reconstructions require verification against the originals. I have not claimed these rows are reviewed or that the three AI-drafted hard-case analyses are my final judgments.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
