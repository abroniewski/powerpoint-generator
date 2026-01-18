# powerpoint-generator

## One-line summary
A small Python tool for turning structured text files into PowerPoint slides and generating synthetic event data for demos.

## The Problem
- Creating repeatable slide decks from structured notes is slow when done manually.
- Ad hoc slide templates lead to inconsistent layouts across teams.
- Demo datasets for event reporting are time-consuming to assemble by hand.
- Running the same presentation flow across multiple decks is error-prone.
Common alternatives such as manual PowerPoint editing or copying from docs are too slow for repeated or automated decks.

## The Approach
- Inputs: a structured `.txt` slide script and optional parameters for synthetic event data generation.
- Processing: parse slide blocks, map fields to PowerPoint layouts, and render a `.pptx` from a template; generate CSVs for event, social, and sponsor data.
- Outputs: a PowerPoint deck saved to `ppt/` and timestamped CSV files saved to `data/`.

## Demo
Add screenshot: docs/images/demo.png
What you would see: a generated deck created from the template file, with titles, body text, and speaker notes filled in.

## Value Delivered
- Turns a plain text script into a PowerPoint deck with consistent layouts.
- Reduces manual copy-paste work for recurring presentations.
- Creates synthetic CSVs for demo dashboards and reports without external data sources.

## Scope & Status
- Project type: Demo
- Current state: Active
- Known limitations:
  - The slide parser expects the exact `--- Slide ---` and `--- End Slide ---` markers.
  - Only the title and a single content placeholder are populated for each slide.
  - Layout indices must match the template's available layouts.
  - The data generator uses random values and has no reproducible seed.
This project does not attempt to be a full presentation authoring suite or a data analytics platform.

## Tech Stack
- Python
- python-pptx
- CSV output for generated data

## Getting Started
Prerequisites:
- Python 3.x
- `pip`

Minimal setup and first run:
1. `python -m pip install python-pptx`
2. `mkdir -p ppt`
3. `cp src/presentation_content_template.txt ppt/my_deck.txt`
4. Edit `ppt/my_deck.txt` with your slide content.
5. `python src/powerpoint_generator.py`

## Usage
Generate a deck from a text file:
- `python src/powerpoint_generator.py`
  - Select your `.txt` file from the interactive prompt.
  - The output deck is saved to `ppt/` with the same base name.

Generate synthetic event data:
- `python src/data_generator.py`
  - Output is written to `data/` as timestamped CSVs such as:
    - `event_data_YYYYMMDD_HHMMSS.csv`
    - `social_media_data_YYYYMMDD_HHMMSS.csv`
    - `professional_data_YYYYMMDD_HHMMSS.csv`

## Configuration
No environment variables are required. There is no `.env.example` in this repo.

## Project Structure
- `src/`: Python scripts and the PowerPoint template assets.
  - `blank_powerpoint_template.pptx`: Base template used for deck creation.
  - `powerpoint_generator.py`: Parses slide scripts and writes a `.pptx`.
  - `presentation_content_template.txt`: Example slide script format.
  - `data_generator.py`: Creates synthetic CSVs for event reporting.

## Testing
Tests: not implemented.

## Roadmap
Next:
- Add CLI flags for input and output paths.
- Validate slide layouts and content fields before rendering.
- Add a sample generated deck to `docs/`.
Later:
- Support richer slide elements such as charts and images.
- Allow batch generation from multiple input files.

## License
License: not specified. No `LICENSE` file is present.

## Credits / Acknowledgements
- [python-pptx](https://github.com/scanny/python-pptx) for PowerPoint file generation.

## Contact / Support
Open an issue on GitHub: https://github.com/abroniewski/powerpoint-generator/issues
