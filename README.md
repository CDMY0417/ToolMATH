# ToolMATH

ToolMATH is a mathematics-oriented tool-use benchmark for evaluating whether a model can select and invoke simple programmatic functions while solving competition-style math problems.

This repository is intended as the public GitHub companion to the released dataset. It includes:

- the `ToolMATH` split and the `ToolMATHHard` split as JSON files,
- the corresponding Python function implementations for both splits,
- a script for constructing deterministic distractor sets,
- and a sample GPT-5-based evaluation script.

## Repository Layout

```text
.
├── data/
│   ├── ToolMATH.json
│   ├── ToolMATHHard.json
│   ├── function_ToolMATH/
│   └── function_ToolMATHHard/
├── scripts/
│   ├── build_level_distractors.py
│   └── sample_evaluation_gpt5.py
└── README.md
```

## Dataset Contents

The repository contains two benchmark splits:

- `data/ToolMATH.json`: the main ToolMATH split with `12,369` examples.
- `data/ToolMATHHard.json`: the harder ToolMATHHard split with `362` examples.

Each dataset record contains:

- `name`: tool or function name
- `description`: natural-language tool description
- `inputs`: argument schema
- `function`: Python filename implementing the tool
- `source_problem`: source math problem
- `source_solution`: reference solution for the source problem
- `level`: problem difficulty
- `type`: math category

The `function` field points to a file in the matching implementation directory:

- `data/ToolMATH.json` pairs with `data/function_ToolMATH/`
- `data/ToolMATHHard.json` pairs with `data/function_ToolMATHHard/`

## Scripts

### `scripts/build_level_distractors.py`

Builds deterministic distractor sets with 100 distractor tools per level for each problem.

Current behavior:

- `level1`: random distractors excluding same-category tools
- `level2`: pure random distractors
- `level3`: random distractors from the same category
- `level4`: embedding-ranked distractors
- `level5`: keyword-overlap plus embedding-ranked distractors

Default inputs and outputs:

- input dataset: `data/ToolMATH.json`
- output distractors file: `data/distractors_by_level.json`
- embedding cache: `data/emb_cache.jsonl`

Example:

```bash
python scripts/build_level_distractors.py
```

Requirements:

- `OPENAI_API_KEY` must be set for embedding generation
- the Hugging Face `datasets` package is used to load `qwedsacf/competition_math`

### `scripts/sample_evaluation_gpt5.py`

Runs a sample ReAct-style evaluation using:

- gold tools,
- top-K distractors from a precomputed distractor file,
- a solver model such as `gpt-5`,
- and a judge model such as `gpt-4o-mini`

Default inputs and outputs:

- distractors file: `data/distractors_by_level.json`
- tool implementation directory: `data/function_ToolMATH/`
- output JSON: `results/sample_evaluation_gpt5.json`

Example:

```bash
python scripts/sample_evaluation_gpt5.py \
  --distractors-json data/distractors_by_level.json \
  --tools-dir data/function_ToolMATH \
  --level 1 \
  --k 100 \
  --num-examples 200 \
  --out results/sample_evaluation_gpt5_l1_k100.json
```

Optional no-gold ablation:

```bash
python scripts/sample_evaluation_gpt5.py \
  --distractors-json data/distractors_by_level.json \
  --tools-dir data/function_ToolMATH \
  --level 1 \
  --k 100 \
  --num-examples 200 \
  --no-gold-tools \
  --out results/sample_evaluation_gpt5_l1_k100_nogold.json
```

Requirements:

- by default, set `OPENAI_API_KEY` for a single-worker run
- if you want multiple workers, pass additional variable names via `--api-key-vars`
- the Hugging Face `datasets` package is used to load `qwedsacf/competition_math`

## Setup

Suggested environment:

```bash
pip install datasets openai
```

For the default single-worker configuration:

```bash
export OPENAI_API_KEY=YOUR_KEY
```

If you want to run multiple workers, pass a comma-separated list through `--api-key-vars` and export the matching variables.

## Source Attribution

ToolMATH is derived in part from the MATH dataset introduced by Hendrycks et al.

```bibtex
@article{hendrycksmath2021,
    title={Measuring Mathematical Problem Solving With the MATH Dataset},
    author={Dan Hendrycks
    and Collin Burns
    and Saurav Kadavath
    and Akul Arora
    and Steven Basart
    and Eric Tang
    and Dawn Song
    and Jacob Steinhardt},
    journal={arXiv preprint arXiv:2103.03874},
    year={2021}
}
```

References:

- MATH repository: https://github.com/hendrycks/math
- MATH paper: https://arxiv.org/abs/2103.03874

If you use ToolMATH, cite the ToolMATH release and the original MATH paper when relevant.

## License

Dataset files in this repository are intended to be distributed under `CC-BY-SA-4.0`.

Because portions of the dataset are derived from MATH, users should review the upstream MATH repository and associated paper when assessing reuse and redistribution obligations for derived content.
