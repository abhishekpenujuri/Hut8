# Project Title

Crypto Profit Calculator

## Assumptions

- Got the BTC price and Network hash rate from public apis as told
- based on my understanding from the given websites and some research online, was able to write a formula based on the inputs

## Running the code

Instructions on how to install and set up the project.

the backend applications will be running on: http://localhost:8000/

```bash
cd CalculatorBackend
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload

