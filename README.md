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
│   ├── strict_equiv_tool_stats.py
│   ├── eval_core.py
│   ├── evaluation_gpt4o.py
│   ├── evaluation_gpt5.py
│   ├── evaluation_llama3_8b.py
│   ├── evaluation_qwen2_5_7b.py
│   ├── evaluation_sonnet_4_6.py
│   └── evaluation_gemini_3_1_pro.py
├── results/
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

## Requirements and Setups

Below are the suggested environment:

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

### Optional Strict-Equivalent Exclusion Mode

You can also build distractors while excluding tools that are judged to be strictly equivalent to any gold tool for the same problem.

First, build the strict-equivalence statistics:

```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/strict_equiv_tool_stats.py \
  --tool-json data/ToolMATH.json \
  --tools-dir data/function_ToolMATH \
  --out-json data/strict_equiv_tool_stats.json \
  --out-csv data/strict_equiv_tool_stats.csv
```

Then pass the resulting JSON into the distractor builder:

```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/build_level_distractors.py \
  --tool-json data/ToolMATH.json \
  --out data/distractors_by_level_no_strict_equiv.json \
  --exclude-strict-equiv \
  --strict-equiv-json data/strict_equiv_tool_stats.json
```

The same flow works for `ToolMATHHard` by changing:

- `--tool-json data/ToolMATHHard.json`
- `--out data/distractors_by_level_toolmathhard.json`
- `--tools-dir data/function_ToolMATHHard`
- optional strict-equivalence outputs such as `data/strict_equiv_tool_stats_toolmathhard.json`

## Evaluation

The `scripts/` directory now includes direct evaluation entrypoints for multiple models:

- `evaluation_gpt4o.py`
- `evaluation_gpt5.py`
- `evaluation_llama3_8b.py`
- `evaluation_qwen2_5_7b.py`
- `evaluation_sonnet_4_6.py`
- `evaluation_gemini_3_1_pro.py`

All of them share the same evaluation logic and accept the same main arguments:

- `--tool-json`: selects `ToolMATH.json` or `ToolMATHHard.json`
- `--tools-dir`: selects `data/function_ToolMATH/` or `data/function_ToolMATHHard/`
- `--distractors-json`: selects the prebuilt distractor file
- `--level`: distractor difficulty level
- `--k`: number of distractors to prepend from the ranked list

Example for ToolMATH:

```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/evaluation_gpt5.py \
  --tool-json data/ToolMATH.json \
  --tools-dir data/function_ToolMATH \
  --distractors-json data/distractors_by_level.json \
  --level 1 \
  --k 100 \
  --num-examples 200 \
  --out results/evaluation_gpt5_toolmath_l1_k100.json
```

Example for ToolMATHHard:

```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/evaluation_gpt5.py \
  --tool-json data/ToolMATHHard.json \
  --tools-dir data/function_ToolMATHHard \
  --distractors-json data/distractors_by_level_toolmathhard.json \
  --level 3 \
  --k 5 \
  --out results/evaluation_gpt5_toolmathhard_l3_k5.json
```

Distractors-only ablation:

```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/evaluation_gpt5.py \
  --tool-json data/ToolMATH.json \
  --tools-dir data/function_ToolMATH \
  --distractors-json data/distractors_by_level.json \
  --level 1 \
  --k 100 \
  --no-gold-tools \
  --out results/evaluation_gpt5_toolmath_l1_k100_nogold.json
```

For non-OpenAI models, use the corresponding script and configure any required OpenAI-compatible endpoint externally, for example via `OPENAI_BASE_URL` and an API key exposed through `OPENAI_API_KEY`.

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
