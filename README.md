# AI Landing Page Personalizer

## Overview
This project builds a simple AI system that personalizes landing pages based on ad creatives.

## Features
- Input ad creative + landing page URL
- Extract page content
- Generate CRO-optimized improvements
- Show before vs after comparison

## Tech Stack
- Streamlit
- OpenAI API
- BeautifulSoup

## Flow
User Input → Page Scraping → AI Processing → Output

## Assumptions
- Landing page is static HTML
- Only text changes (no UI changes)

## Challenges handled
- Hallucination → restricted prompts
- Broken UI → text-only edits
- Inconsistency → structured output
