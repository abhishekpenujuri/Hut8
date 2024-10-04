"""
Input and Result Validations
"""
from pydantic import BaseModel

class CrptoCalcInput(BaseModel):
    electricity_cost: float
    power_consumption: float
    hash_rate: float
    initial_investment: float

class CryptoCalcResult(BaseModel):
    dailyCost: float
    monthlyCost: float
    yearlyCost: float
    dailyRevenueUSD: float
    monthlyRevenueUSD: float
    yearlyRevenueUSD: float
    dailyRevenueBTC: float
    monthlyRevenueBTC: float
    yearlyRevenueBTC: float
    dailyProfitUSD: float
    monthlyProfitUSD: float
    yearlyProfitUSD: float
    breakevenTimeline: float
    costToMine: float
