"""
Simple photovoltaic (PV) energy calculations.
"""


def yearly_pv_generation(capacity_kw: float, specific_yield: float) -> float:
    """
    Estimate yearly PV electricity production in kWh.

    specific_yield typical values:
    900–1200 kWh per kW installed capacity per year.
    """
    return capacity_kw * specific_yield


def self_consumption(generation_kwh: float, self_consumption_rate: float) -> float:
    """
    Calculate how much PV electricity is used directly.
    """
    return generation_kwh * self_consumption_rate


def savings(self_used_kwh: float, electricity_price: float) -> float:
    """
    Estimate yearly savings in €.
    """
    return self_used_kwh * electricity_price
