"""
Endpoints/Routes for our App
"""

from fastapi import APIRouter, Depends
from app.schemas.models import CrptoCalcInput, CryptoCalcResult
from app.services.calculator import crypto_profit_calculator

router = APIRouter()

@router.post("/calculate/", response_model=CryptoCalcResult)
def calculate_mining_profit(input: CrptoCalcInput):
    """
    Calculations based on our input
    
    :param input: CrptoCalcInput
    :return: CryptoCalcResult
    """
    try:
        return crypto_profit_calculator(input)
    except ValueError as e:
        raise ValueError(f"Value Error: {str(e)}")