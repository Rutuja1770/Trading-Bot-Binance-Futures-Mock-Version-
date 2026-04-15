import random
import time

class MockClient:
    def futures_create_order(self, **kwargs):
        time.sleep(1)  # simulate delay

        return {
            "orderId": random.randint(100000, 999999),
            "symbol": kwargs.get("symbol"),
            "side": kwargs.get("side"),
            "type": kwargs.get("type"),
            "status": "FILLED" if kwargs.get("type") == "MARKET" else "NEW",
            "executedQty": kwargs.get("quantity"),
            "avgPrice": kwargs.get("price", "market_price"),
        }

def get_client():
    return MockClient()