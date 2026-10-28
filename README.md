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

TakeMeter classifies text posts from the public r/DentalHygiene community as `emotional_support` or `practical_advice`. Emotional-support posts express distress or seek reassurance, validation, or solidarity, while practical-advice posts request concrete information, recommendations, or actions. When a post does both, the decision rule prioritizes a concrete request for help over its emotional tone. The current version uses 228 reviewed posts. Its small held-out sets and subjective label boundary limit how much the results can establish.

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

**Collection and review:** The initial run used 104 posts. Before the unit 6 evaluation, collection expanded to 230 unique posts. I reviewed the 31 rows still marked as AI-pre-labeled one at a time, and reviewed eight separately flagged cases. Two posts were excluded for missing context and preserved in `excluded_posts.csv`, leaving 228 posts. Some retained posts still lack referenced titles or images; those limitations are recorded in their notes. Earlier user-supplied labels and later corrections are distinguished from AI suggestions in the CSV.

| Label | Count | Share |
|---|---:|---:|
| `emotional_support` | 108 | 47.4% |
| `practical_advice` | 120 | 52.6% |
| **Total** | **228** | **100%** |

The expanded dataset and review were completed before the three-seed “before” experiment. They are separate from the single measured unit 6 improvement. The original 104-post results remain in Git history. No label exceeds 70%.

**Three hard cases — initial AI-drafted boundary analyses**

These analyses were drafted during the initial run. I later reviewed the corresponding labels in conversation: the flossing-anxiety post and burnout post were labeled emotional_support when resubmitted, and the brushing-worry post was confirmed emotional_support. The initial suggested reasoning is retained below as history, not as the final label decisions.

**1. Distress plus a specific request for help flossing**

> *Post excerpt:* “I’m panicking. I don’t want to lose my teeth. (I have gingivitis.)” ... “Gonna do some research and see what’s out there but if anyone has advice, please share 🥲”
>
> *Could have been:* `emotional_support` or `practical_advice`.
>
> *Initial AI label and reasoning:* `practical_advice`. The author expresses anxiety but also describes difficulty using floss and explicitly asks for advice. The concrete request takes priority under the decision rule.
>
> *My review:* I subsequently chose `emotional_support` when resubmitting this post. This differs from the initial AI suggestion and may conflict with my concrete-request priority rule; that is a remaining taxonomy-consistency limitation, not a claim that the initial reasoning was accepted.

**2. Anxiety about brushing, without a specific request for a technique**

> *Post:* “I have a very bad habit of passing out at night and then brushing my teeth in the morning.How worried should I be? I dont have gingivitis thankfully no gum bleeding. I am a lot better than I was but I still do these stupid things. Thanks for letting me ask and vent.”
>
> *Could have been:* `emotional_support` or `practical_advice`.
>
> *Initial AI label and reasoning:* `emotional_support`. The main request appears to be reassurance about worry rather than a concrete change to the routine. Review whether “How worried should I be?” should instead count as a request for factual risk information, and clarify the rule consistently.
>
> *My review:* I confirmed `emotional_support` in the individual review.

**3. Burnout with a practical question at the end**

> *Post excerpt:* “This week has been hell on earth!” ... “If you are a hygienist and find time to go to your gym after work even if it’s crowded, and come home and cook real food, I applaud you. How do you do it.”
>
> *Could have been:* `emotional_support` or `practical_advice`.
>
> *Initial AI label and reasoning:* `practical_advice`. Most of the post vents, but the final question can be read as asking for concrete strategies to manage work, exercise, and meals. Review whether it is a literal request or a rhetorical expression of exhaustion.
>
> *My review:* I subsequently chose `emotional_support` when resubmitting this post. Whether the final question is rhetorical remains a boundary limitation; I retained my chosen label for the controlled experiment.

---

## The Training Run

The details below describe the original 104-post unit 5 run. The expanded 228-post unit 6 experiment is recorded in the run logs below.

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
- *What I changed:* I standardized the label names to `emotional_support` and `practical_advice`. The 31 remaining AI-suggested labels were subsequently reviewed individually, followed by the eight flagged cases.

**Pre-labelling disclosure:** AI formatted copied posts and supplied some initial label suggestions. I subsequently reviewed all 31 rows still marked as awaiting AI-label review, plus eight flagged cases, in conversation. Two missing-context posts were excluded. Earlier batches were labeled by me and formatted by AI. AI helped explain the staff taxonomy and drafted adjudication text from my decisions; my original staff answers are preserved unchanged. AI also prepared the run logs, identified input truncation as a hypothesis to test, ran the controlled experiment, and reproduced the trials to measure the confidence threshold. I chose the retrospective clarification of criterion 3; AI computed the retrospective human–AI audit from Git history and my saved reviews. Verification against original source posts remains a limitation for reconstructed or incomplete excerpts.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---:|---:|---:|
| Overall accuracy | 0.657 | 0.686 | +0.029 |
| Macro F1 | 0.643 | 0.676 | +0.033 |
| F1 — `emotional_support` | 0.714 | 0.621 | -0.094 |
| F1 — `practical_advice` | 0.571 | 0.732 | +0.160 |

Both models were evaluated on the same 35 held-out posts for seed 42. The baseline used the written label definitions.

**What I predicted before I looked:** I did not record a prediction before viewing the comparison results.

**What the gap actually means:** The trained model got one additional post correct (24 versus 23), with stronger practical-advice F1 but weaker emotional-support F1. This is a small observed advantage on one split, not evidence of a reliable overall improvement.

---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.70 | 0.686 | 0.771 | 0.657 | MISSED |
| 2. Per-label precision | practical_advice ≥ 0.80; emotional_support ≥ 0.60 | PA: 0.652; ES: 0.750 | PA: 0.708; ES: 0.909 | PA: 0.667; ES: 0.647 | MISSED — practical_advice below target in all three seeds |
| 3. Dataset balance | 60% practical_advice (clarified retrospectively) | 52.6% | 52.6% | 52.6% | MISSED |
| 4. Human–AI label agreement | ≥ 9/10 posts agree | 10/10 | 10/10 (same audit) | 10/10 (same audit) | MET on retrospective audit |
| 5. Accuracy when confidence ≥ 0.80 | ≥ 0.85 | N/A (0 qualify) | N/A (0 qualify) | N/A (0 qualify) | MISSED — pass not demonstrated |

Source: `results_three_seeds_before.json`, using the reviewed 228-post dataset. Each seed has 35 test posts (17 emotional_support and 18 practical_advice). All runs used Apple Silicon GPU (MPS), PyTorch 2.14.1, and a maximum input length of 128 tokens.

Accuracy ranged from 65.7% to 77.1%, a spread of 11.4 percentage points. This exceeds the assignment’s 10-point stability guideline, so conclusions from a single split are uncertain. Accuracy missed its target in seeds 42 and 2024. Emotional-support precision met its target in all three seeds, but practical-advice precision did not.

Criteria 3 and 4 concern the dataset or labelers rather than model randomness, so they are not independent measurements across seeds. The user clarified criterion 3 as a 60% share after seeing the counts; this is disclosed rather than presented as a pre-registered threshold. Criterion 4 uses the first ten original AI-pre-labeled rows that match posts subsequently reviewed individually by the user. All ten match (human_ai_agreement.json). This is a retrospective consistency audit, not a new blind sample; repeating it in the seed columns does not create three independent trials. The staff agreement exercise uses a separate taxonomy and does not directly measure criterion 4’s human–AI agreement. Criterion 5 was measured afterward by reproducing all six trials with added confidence instrumentation; the accuracy, per-label metrics, and confusion matrices exactly matched the saved originals. No predictions reached 0.80 confidence, so threshold accuracy is undefined and the target cannot be demonstrated. “MISSED” here means insufficient qualifying evidence to establish a pass, not measured accuracy below 85%. See `confidence_threshold_results.json`; the original experiment result files were preserved. Original criteria remain unchanged in `criteria.md`.

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

Seed 42, matching the notebook’s section 7 selection:

| true \ predicted | emotional_support | practical_advice |
|---|---|---|
| **emotional_support** | 9 | 8 |
| **practical_advice** | 3 | 15 |

**My biggest off-diagonal number, and what it means:**

Eight emotional-support posts were predicted as practical advice, compared with three practical-advice posts predicted as emotional support. In this split, the model leans toward practical advice on this boundary.
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Accuracy | ≥ 0.70 | MISSED | Seeds 42 and 2024 scored 0.686 and 0.657; all seeds must pass. |
| 2 | Precision | PA ≥ 0.80; ES ≥ 0.60 | MISSED | PA precision was 0.652, 0.708, and 0.667. ES passed in all three. |
| 3 | Dataset balance | 60% PA, clarified retrospectively | MISSED | User chose the proportional interpretation; 120/228 = 52.6%, below 60%. Original wording and clarification remain in criteria.md. |
| 4 | Human–AI agreement | ≥ 9/10 | MET on retrospective audit | Ten original AI suggestions matched the user’s later individual reviews; see human_ai_agreement.json. Selection was retrospective, not a new independent trial. |
| 5 | Accuracy at confidence ≥ 0.80 | ≥ 0.85 | MISSED — pass not demonstrated | Reproduced all six trials; none produced a prediction with confidence ≥ 0.80. Conditional accuracy is undefined, not 0%. |

**Diagnoses**

For accuracy and practical-advice precision, the seed-42 matrix shows eight emotional-support posts called practical advice versus three errors in the other direction. Across seeds, emotional-support recall stays between 0.529 and 0.647: the model misses a substantial share of that label. The 11.4-point accuracy spread and only 35 test posts per seed limit the stability of conclusions.

The staff exercise found four disagreements I accepted as rule-application or comprehension mistakes and two I continue to defend. This shows I can over-weight personal experience and confuse an argument’s quality with the presence of supporting evidence. It suggests possible labeling inconsistency, but the staff’s running-post taxonomy differs from my own, so it does not prove which dental-hygiene rows are wrong.

Input truncation was another plausible cause: the before-model reads only 128 tokens, while posts can place their request or main point near the end. I tested a longer input window as one change. This is a hypothesis rather than a demonstrated explanation of every error. The dataset is fairly balanced (108/120), so severe class imbalance is not supported by the counts.

For criterion 5, maximum confidence ranged from 0.587 to 0.655 before and 0.602 to 0.646 after. The 80% threshold selected zero posts in every trial, so there is no conditional accuracy estimate. This diagnoses a coverage/measurement problem at the chosen threshold rather than showing that high-confidence predictions are wrong. I did not lower the threshold after seeing this result.

Dataset balance misses the retrospectively clarified 60% target because the expanded collection contains 120 practical-advice and 108 emotional-support posts. The collection is fairly balanced for classification, but that is distinct from meeting my numerical target. Criterion 4 meets 9/10 in the retrospective ten-post audit, with the limitations disclosed above. Neither the staff agreement rate nor repeated seed columns should be mistaken for independent human–AI trials.

---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** 24 / 30 = 80%

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
> *The post:* The club championship scoring changed in 2019 from top-6 to top-10. Since then our B team has finished above the A team twice. That's not depth improving, it's the scoring rewarding turnout.
>
> *Staff said / I said:* `analysis` / `hot_take`.
>
> *My call, and why:* I keep `hot_take`. I do not think the scoring change supports the conclusion; I read the B-team wins as evidence pointing toward improved depth instead. Under rule 1, I do not regard these facts as carrying the stated argument. The counterargument discussed during review is that facts can carry an argument even if its inference is weak; staff’s `analysis` label does not require the conclusion to be proved.
>
> *Which pile:* (c) I regard the rule as ambiguous here and defend my interpretation of the facts as decoration rather than support.

**2.**
> *The post:* Everyone blames the hill at 18 miles. I split the field into people who ran the first half under 1:45 and over, and the slowdown after 18 was almost identical for both groups. If the hill were the problem the fast starters would fall apart harder.
>
> *Staff said / I said:* `analysis` / `hot_take`.
>
> *My call, and why:* I accept `analysis` because the writer makes a clear comparison between two groups. Their nearly identical slowdown is evidence used to challenge the explanation about the hill. Under rule 1, that comparison carries the argument rather than decorating an unsupported claim.
>
> *Which pile:* (a) The rule covered it, and I applied it loosely.

**3.**
> *The post:* Carbon plates aren't the whole story. My times dropped 2% in the shoes and another 2% the following year in the same pair, when the only thing that changed was going from 35 to 50 miles a week.
>
> *Staff said / I said:* `analysis` / `hot_take`.
>
> *My call, and why:* After discussing what the sentence meant with AI, I accept `analysis`. The writer reports a further 2% improvement while using the same shoes but increasing weekly mileage from 35 to 50 miles. That comparison supports the argument that shoes do not explain all the improvement, so the facts carry the argument under rule 1. My original choice reflected difficulty understanding the post.
>
> *Which pile:* (a) The rule covered it; I initially misread the post rather than identifying a gap in the definitions.

**4.**
> *The post:* Ran the same loop in 4C and in 24C within a fortnight, same effort by heart rate. 90 seconds slower in the heat over six miles. People keep saying heat costs you 'a bit' and it's more than that.
>
> *Staff said / I said:* `analysis` / `reaction`.
>
> *My call, and why:* I initially chose `reaction` because it describes a personal experience. After discussing rule 3 with AI, I accept `analysis`: the comparison of the same route at similar effort in two temperatures, with a 90-second slowdown, supports the argument about heat. Being a personal experience does not override evidence that carries the argument.
>
> *Which pile:* (a) The rule covered it, and I initially gave too much weight to the personal experience.

**5.**
> *The post:* Three of us ran the same session on the same day, different shoes, within 10 seconds of each other over 5 miles. I'm not saying shoes do nothing, but whatever they do was smaller than the noise between three people.
>
> *Staff said / I said:* `analysis` / `reaction`.
>
> *My call, and why:* On review, I choose `hot_take`, changing my original `reaction` label. My initial reason for `reaction` was that this describes a recent experience. We discussed rule 3, which says recency does not override evidence. I think the numbers decorate the claim rather than carry its argument, so I choose `hot_take` under rule 1. Staff’s alternative reading is that the same-session comparison and 10-second gap support the conclusion about the shoes’ effect.
>
> *Which pile:* (c) I regard the rule as ambiguous here and defend my interpretation of the facts as decoration rather than support.

**6.**
> *The post:* Every injury thread on this forum is the same injury and the same three replies.
>
> *Staff said / I said:* `hot_take` / `reaction`.
>
> *My call, and why:* I accept `hot_take` because the post does not describe a recent event. Under rule 2, it makes a general, unsupported claim about forum threads rather than reporting what just happened to the writer and how it felt.
>
> *Which pile:* (a) The rule covered it, and I initially applied the reaction label too broadly.

**What the pattern in my disagreements tells me:**

Five of my six disagreements were posts staff called analysis; I initially called three hot_take and two reaction. I accepted four staff labels on review and defended two interpretations, showing that recognizing evidence and distinguishing it from personal experience were the main difficulties. This is evidence about my application of these staff rules, not a direct audit of my dental-hygiene labels.



---

## The Improvement

**What I changed:** Increased the maximum input length from 128 to 256 tokens for the after-runs. After-runs were executed from the notebook’s functions by a local Python runner, one fresh process per seed to release model memory; their metrics were combined into `results_three_seeds_after.json`. The 228-post dataset, labels, model, three epochs, learning rate 2e-5, batch size 16, and seeds 42, 7, and 2024 remain the same.

**Which diagnosis pointed at it:** Long posts may lose their final requests or context at 128 tokens. A tokenizer audit found 102/228 posts exceed 128 tokens, compared with 37/228 exceeding 256 tokens. Reading more text tests that truncation hypothesis without changing the taxonomy or labels. The result will show whether this change helps; it cannot establish truncation as the sole cause.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Accuracy | ≥ 0.70 | 0.743 | 0.686 | 0.714 | MISSED |
| 2. Precision | PA ≥ 0.80; ES ≥ 0.60 | PA: 0.765; ES: 0.722 | PA: 0.684; ES: 0.688 | PA: 0.682; ES: 0.769 | MISSED |
| 3. Dataset balance | 60% PA, clarified retrospectively | 52.6% | 52.6% | 52.6% | MISSED |
| 4. Human–AI agreement | ≥ 9/10 | 10/10 | 10/10 (same audit) | 10/10 (same audit) | MET on retrospective audit |
| 5. Accuracy at confidence ≥ 0.80 | ≥ 0.85 | N/A (0 qualify) | N/A (0 qualify) | N/A (0 qualify) | MISSED — pass not demonstrated |

All after-runs used Apple Silicon GPU (MPS), PyTorch 2.14.1, and 256 tokens. Each seed uses the same split as its before-run.

**Did it help, and how do I know:** The result is mixed. Mean accuracy rose from 70.5% to 71.4% across the three splits, but seed 7 worsened and the 70% accuracy target still failed across all three trials. Mean macro F1 rose from 0.698 to 0.712. This is a modest observed improvement, not proof of a reliable gain or of truncation as the sole cause.

| Seed | Before accuracy | After accuracy | Change (percentage points) |
|---|---:|---:|---:|
| 42 | 68.6% | 74.3% | +5.7 |
| 7 | 77.1% | 68.6% | -8.6 |
| 2024 | 65.7% | 71.4% | +5.7 |

After-run accuracy spread was 5.7 percentage points. Longer inputs also increased training work. I stopped after this single change to keep the experiment interpretable.

---

### Confidence threshold measurement

These are reproduced runs using the same dataset, settings, seeds, and Apple GPU. All six reproduce the original accuracy, per-label metrics, and confusion matrices. `measure_confidence.py` adds measurement only; it does not change training, labels, or predictions.

| Phase | Seed | Maximum confidence | Predictions ≥ 0.80 | Accuracy on qualifying predictions |
|---|---:|---:|---:|---|
| before | 42 | 0.587 | 0 | N/A — empty group |
| before | 7 | 0.655 | 0 | N/A — empty group |
| before | 2024 | 0.618 | 0 | N/A — empty group |
| after | 42 | 0.602 | 0 | N/A — empty group |
| after | 7 | 0.630 | 0 | N/A — empty group |
| after | 2024 | 0.646 | 0 | N/A — empty group |

Source: `confidence_threshold_results.json`. Reproduce with `.venv/bin/python measure_confidence.py`. This needs the model cache or Hugging Face access; each trial runs in a fresh process to release GPU memory.

---

## What's Still Broken

Accuracy still misses the 70% target across seeds. I would next audit misclassified posts against the concrete-request rule and collect more examples of ambiguous emotional-support posts, but did not make those additional changes because this experiment measures one improvement only.

The per-label precision target also remains missed. I would examine emotional-support posts predicted as practical advice before trying more training settings. The staff exercise suggests some rule-application difficulty, but cannot identify errors in this different taxonomy by itself.

Criterion 3 was clarified retrospectively as 60% practical advice and misses that target; future collection could target that share, but changing the data again would add another intervention. Criterion 4 passes a retrospective audit only; a future prospective blind sample would provide stronger evidence. Criterion 5 was measured but has zero qualifying predictions in all six trials. A future evaluation should state a minimum qualifying sample count and collect enough held-out examples to assess confidence; I retained the original 80%/85% thresholds for this submission. All five criteria now have a documented verdict, including the evidence limitation behind criterion 5’s non-pass.

**The gap between what I meant my labels to capture and what the model learned:**

I intended the labels to distinguish a request for reassurance from a request for concrete information, even when both have an emotional tone. The before-run seed-42 matrix shows eight emotional-support posts called practical advice, so the learned boundary does not consistently match that intent; the matrix alone cannot establish what textual features caused those errors.

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
