# Secure Data Exchange Encoding

This repository contains practical elements for ST4015CMD Assignment Task 1: Enhancing Secure Data Exchange with Encoding Formats and Protocol Integration. It includes Python scripts for encoding simulations and diagrams for data flows. All files are designed to complement the report's analysis.

## How to Interpret and Use This Repo

### Scripts Folder
- **encode_demo.py**: Demonstrates Base64, Hex, and URL encoding on sample data. Shows strengths/weaknesses like size increases.  
  *Run*: `python scripts/encode_demo.py` (Requires Python 3+; no extra installs needed). Output: Encoded strings and efficiency metrics. Ties to Analysis point 1 (strengths/weaknesses evaluation).

- **http_payload_sim.py**: Simulates an HTTP payload with encoding to prevent injection attacks (e.g., escapes XSS chars).  
  *Run*: `python scripts/http_payload_sim.py`. Output: Before/after encoding examples. Relates to Analysis point 2 (securing HTTP payloads).

- **rest_api_example.py**: Mocks a REST API call with Base64-encoded auth and URL-encoded params, showing interoperability.  
  *Run*: `python scripts/rest_api_example.py` (Uses `requests`—install if needed: `pip install requests`). Output: Simulated API response. Links to Analysis point 3 (modern web protocols like REST/OAuth).

### Diagrams Folder
- **figure1_flowchart.drawio/png**: Flowchart for Base64 in TLS-based email transmission (data encode → encrypt → send → decode).  
  *View/Edit*: Open .drawio in Draw.io (diagrams.net). PNG for quick preview. Supports Analysis point 4.

- **figure2_sequence.drawio/png**: Sequence diagram for URL encoding in HTTPS web authentication (user → encode → transmit → decode).  
  *View/Edit*: Same as above. Illustrates protocol integration.

## Setup Requirements
- Python 3.x for scripts.
- No internet/API keys needed—these are offline simulations.
- For diagrams: Use diagrams.net (free online tool).

This repo demonstrates real-world application of encoding formats without compromising security. Refer to the assignment report for theoretical context.