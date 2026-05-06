# ToolMATH

ToolMATH is a math-grounded benchmark for evaluating tool-augmented language models under controlled long-horizon multi-tool reasoning conditions. The benchmark converts stepwise MATH solutions into reusable Python tools with natural-language descriptions and typed input schemas, and evaluates models in tool environments that vary distractor similarity and tool availability.

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
├── .gitignore
└── README.md
```

## Contents of the Dataset

This repository contains the two benchmark splits described in the paper:

- `ToolMATH`: `7,699` questions and `12,369` validated tools
- `ToolMATHHard`: `329` questions and `362` human-authored validated tools

The files are organized as follows:

- `data/ToolMATH.json`: the main ToolMATH tool metadata file
- `data/ToolMATHHard.json`: the ToolMATHHard tool metadata file
- `data/function_ToolMATH/`: Python implementations referenced by `ToolMATH.json`
- `data/function_ToolMATHHard/`: Python implementations referenced by `ToolMATHHard.json`

Each JSON record contains:

- `name`: tool or function name
- `description`: natural-language description of the tool
- `inputs`: typed input schema
- `function`: Python filename implementing the tool
- `source_problem`: source math problem
- `source_solution`: reference solution for the source problem
- `level`: problem difficulty
- `type`: math category

The `function` field points to a Python file in the corresponding implementation directory for that split.

## Setup or Requirements

Suggested environment:

```bash
pip install datasets openai
```

External resources used by the included scripts:

- the Hugging Face `datasets` package is used to load `qwedsacf/competition_math`
- `OPENAI_API_KEY` is required for embedding generation in distractor construction
- `OPENAI_API_KEY` is also the default key used by the sample evaluation script

If you want to run multi-worker evaluation, you can pass a comma-separated list of environment variable names via `--api-key-vars` and export the matching keys.

## Building Deterministic Distractors

The script [build_level_distractors.py](/data4/hyeonjechoi/math_predefined/Test_MATH/public_repo/scripts/build_level_distractors.py:1) constructs deterministic distractor sets for the main ToolMATH split.

It builds `100` distractor tools per problem for each of five levels:

- `level1`: random distractors excluding same-category tools
- `level2`: pure random distractors
- `level3`: random distractors from the same category
- `level4`: embedding-ranked distractors
- `level5`: keyword-overlap plus embedding-ranked distractors

The script uses:

- input tool file: `data/ToolMATH.json`
- output distractor file: `data/distractors_by_level.json`
- embedding cache: `data/emb_cache.jsonl`

Example:

```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/build_level_distractors.py
```

This matches the deterministic distractor construction described in the paper: for each problem and each level, an ordered list of 100 distractors is built once and reused so that smaller `k` settings are prefixes of larger ones.

## Evaluation

The script [sample_evaluation_gpt5.py](/data4/hyeonjechoi/math_predefined/Test_MATH/public_repo/scripts/sample_evaluation_gpt5.py:1) is a sample evaluation script for running a GPT-5-style ReAct setup on ToolMATH with gold tools plus top-`K` distractors.

By default it uses:

- one worker
- one API key from `OPENAI_API_KEY`
- distractors from `data/distractors_by_level.json`
- tool implementations from `data/function_ToolMATH/`
- output path `results/sample_evaluation_gpt5.json`

Example:

```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/sample_evaluation_gpt5.py \
  --distractors-json data/distractors_by_level.json \
  --tools-dir data/function_ToolMATH \
  --level 1 \
  --k 100 \
  --num-examples 200 \
  --out results/sample_evaluation_gpt5_l1_k100.json
```

Optional Distractors-only style ablation:

```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/sample_evaluation_gpt5.py \
  --distractors-json data/distractors_by_level.json \
  --tools-dir data/function_ToolMATH \
  --level 1 \
  --num-examples 200 \
  --no-gold-tools \
  --out results/sample_evaluation_gpt5_l1_nogold.json
```

This sample script is not the full evaluation suite from the paper. It is included as a minimal public example of the benchmark interface and a reference implementation for gold-present and distractors-only style conditions.

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

If you use ToolMATH, cite both the ToolMATH release and the original MATH paper when relevant.

Dataset files in this repository are intended to be distributed under `CC-BY-SA-4.0`.

Because portions of the dataset are derived from MATH, users should review the upstream MATH repository and associated paper when assessing reuse and redistribution obligations for derived content.
