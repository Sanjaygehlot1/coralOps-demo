# payment/payment_worker.py

import asyncio

async def retry_payment(
    operation,
    retries=3
):

    for attempt in range(retries):

        try:
            return await operation()

        except Exception:

            if attempt == retries - 1:
                raise

            await asyncio.sleep(
                2 ** attempt
            )
