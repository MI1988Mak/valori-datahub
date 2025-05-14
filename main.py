
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_valori_data(city: str = "Berlin", etf: str = "URTH", status: str = "ledig", country: str = "DE", from_currency: str = "USD", to_currency: str = "EUR"):
    return {
        "zinsniveau": 3.89,
        "inflation": 2.4,
        "etf": {
            "symbol": etf,
            "return_10y": 6.7,
            "volatility": 12.3
        },
        "immobilien": {
            "city": city,
            "price_per_sqm": 4820,
            "rent_per_sqm": 12.4
        },
        "steuern": {
            "status": status,
            "freibetrag": 1000,
            "abgeltung": 25
        },
        "wechselkurs": {
            "from": from_currency,
            "to": to_currency,
            "rate": 1.08
        }
    }
