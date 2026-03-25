# Contributing Guide

## Overview

This repository is a dataset of algorithm implementations where the same code is written in multiple human languages (English, Spanish, Portuguese, Chinese, etc.) by translating symbol names and comments **by hand** — no language models allowed for translation.

---

## Dataset Structure

Each entry in the dataset lives in its own folder. The folder name must:

- Be in **snake_case**
- Be in **English**
- Represent the algorithm implemented in the base code

**Example:** For the Sieve of Eratosthenes, the folder should be named `eratosthenes_sieve`.

---

## File Naming Convention

### Base file

Each folder must contain **exactly one** base file. The base file is named following this pattern:

```
base_<lang>.<ext>
```

Where `<lang>` is the [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) two-letter language code of the language used for symbol names and comments, and `<ext>` is the file extension of the programming language used.

**Examples:**

| File | Meaning |
|------|---------|
| `base_us.py` | Python script with symbols/comments in English |
| `base_es.java` | Java script with symbols/comments in Spanish |
| `base_cn.c` | C script with symbols/comments in Chinese |

### Modified files

Each folder may contain **one or more** modified files. A modified file is the base code with all symbol names and comments translated into another human language, **by hand**.

Modified files follow this naming pattern:

```
modified_<lang>.<ext>
```

**Examples:**

| File | Meaning |
|------|---------|
| `modified_es.py` | Python version of the base code with symbols/comments in Spanish |
| `modified_pt.py` | Python version of the base code with symbols/comments in Portuguese |
| `modified_cn.py` | Python version of the base code with symbols/comments in Chinese |

### Obfuscated version (optional)

One of the modified versions may be obfuscated — that is, stripped of all meaningful identifiers. In that case, use the special language tag `_obf`:

```
modified_obf.<ext>
```

**Example:** `modified_obf.py`

---

## Translation Rules

The translation from the base code to a modified version must follow these strict rules:

1. **Translate by hand only.** Using a language model (GPT, Claude, Gemini, etc.) to perform the translation of symbol names or comments is **not allowed**.
2. **Only translate symbols and comments.** The logic, structure, and syntax of the code must remain identical to the base code.
3. **Translate everything.** This includes: variable names, constant names, class names, function/method names, parameter names, and all inline or block comments.
4. **Do not change behavior.** The translated code must be functionally equivalent to the base code.

---

## README.md

Each folder must include a `README.md` file written in **English** with the following sections:

```markdown
# Algorithm Name

## Author
Full name and date in YYYY-MM-DD format.
Example: Joaquin Bogado (2026-03-20)

## Algorithm Description
A description of the algorithm in English. This may be adapted from Wikipedia,
but it must describe the specific algorithm as implemented in the base code.

## Model Used to Create the Base Code
The name of the model used to generate the base code.
Examples: `gpt-4o-mini-20230401`, `claude-sonnet-4-6`, `gemini-2.0-flash`
If the code was written by hand, write: `manually crafted`

### Prompt
If a language model was used, include the exact prompt used, wrapped in triple backticks:
\`\`\`
Write a function that receives a number `number` and returns True if the number
is prime and False if it is not.
\`\`\`
If the code was manually crafted, omit this subsection.

## Obfuscated Version
`none` if there is no obfuscated version.
If obfuscated manually, write: `manually obfuscated`
If a tool was used, describe the tool and include the command invocation if possible.
Example: `pyarmor obfuscate --restrict=0 base_us.py`
```


---

## Testing code
If you provide testing code for your algorithms, put it on a `tests` folder inside your algorithm folder.

---

## Example Folder Layout

```
eratosthenes_sieve/
├── README.md
├── base_us.py
├── modified_es.py
├── modified_pt.py
├── modified_obf.py
└── tests/
    └── tests_base.py
```

---

## Commit Rules
Do not make a single commit for several algorithms. If you are submiting several algorithms, separate each one in a different commit.

---

## Checklist Before Submitting

- [ ] Folder name is in `snake_case` and English
- [ ] Exactly one base file exists, named `base_<lang>.<ext>`
- [ ] All modified files are named `modified_<lang>.<ext>` or `modified_obf.<ext>`
- [ ] All translations were done **by hand** (no LLMs used for translation)
- [ ] No test code in `base_<lang>.<ext>` or `modified_<lang>.<ext>` files.
- [ ] The logic of the code is unchanged across all versions
- [ ] A `README.md` is included with all required sections
- [ ] The `README.md` is written in English

---

## Questions?

Open an issue in the repository describing your question or suggestion.
