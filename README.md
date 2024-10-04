# Project Title

Crypto Profit Calculator

## Assumptions

- Got the BTC price and Network hash rate from public apis as told
- Based on my understanding from the given websites and some research online, was able to write a formula based on the inputs
- From my understnadings and assumprions
  - reducing the power consumption or making it more efficeint would reduce our costs and increase profits
  - another assumption is that monthly and yearly metrics are calcualted from daily metrics
  - the break even metric gives us an estimate of how long the initial investment can be used
  - BTC price also from the public api also effects our calculations, any changes in that price will have an impact to our metrics

## Running the code

Instructions on how to install and set up the project.

the backend applications will be running on: http://localhost:8000/

```bash
cd CalculatorBackend
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload

