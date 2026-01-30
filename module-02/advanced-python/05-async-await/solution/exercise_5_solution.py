"""Exercise 5 Solution: Real-world Data Pipeline"""
import asyncio
import time
import random
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class DataItem:
    """Represents a data item in our pipeline."""
    id: int
    raw_data: Optional[str] = None
    processed_data: Optional[str] = None
    status: str = "pending"
    error: Optional[str] = None

async def fetch_data(item_id: int, fail_rate: float = 0.0) -> dict:
    """Fetch data from API with optional failure simulation."""
    print(f"  Fetching item {item_id}...")
    await asyncio.sleep(0.5)  # Simulate API delay

    # Simulate occasional failures for testing
    if random.random() < fail_rate:
        raise Exception(f"Failed to fetch item {item_id}")

    return {"id": item_id, "data": f"raw_data_{item_id}"}

async def process_data(data: dict) -> dict:
    """Process/transform the fetched data."""
    print(f"  Processing item {data['id']}...")
    await asyncio.sleep(0.3)  # Simulate processing delay

    # Transform the data (uppercase the string)
    processed = data['data'].upper()
    return {**data, "processed": processed}

async def save_data(data: dict) -> bool:
    """Save processed data to storage."""
    print(f"  Saving item {data['id']}...")
    await asyncio.sleep(0.2)  # Simulate save delay
    print(f"  ✓ Saved item {data['id']}")
    return True

async def process_item(item_id: int, max_retries: int = 3) -> DataItem:
    """Process a single item through the entire pipeline."""
    item = DataItem(id=item_id)

    # Implement retry logic with exponential backoff
    for attempt in range(max_retries):
        try:
            # Step 1: Fetch data
            raw = await fetch_data(item_id, fail_rate=0.2)
            item.raw_data = raw['data']

            # Step 2: Process data
            processed = await process_data(raw)
            item.processed_data = processed['processed']

            # Step 3: Save data
            await save_data(processed)

            # Mark as success
            item.status = "completed"
            return item

        except Exception as e:
            if attempt == max_retries - 1:
                # Last attempt failed - mark as failed
                item.status = "failed"
                item.error = str(e)
                print(f"  ✗ Item {item_id} failed after {max_retries} attempts")
            else:
                # Retry with exponential backoff
                wait_time = 2 ** attempt
                print(f"  ⚠ Retry {attempt + 1}/{max_retries} for item {item_id} after {wait_time}s")
                await asyncio.sleep(wait_time)

    return item

async def run_pipeline(item_ids: List[int]) -> List[DataItem]:
    """Run the complete data pipeline for multiple items."""
    print(f"=== Processing {len(item_ids)} items through pipeline ===\n")
    start = time.time()

    # Create tasks for all items
    tasks = [process_item(item_id) for item_id in item_ids]

    # Run all tasks concurrently
    results = await asyncio.gather(*tasks)

    # Calculate statistics
    elapsed = time.time() - start
    completed = sum(1 for r in results if r.status == "completed")
    failed = sum(1 for r in results if r.status == "failed")

    # Print summary
    print(f"\n=== Pipeline Complete in {elapsed:.2f}s ===")
    print(f"Successful: {completed}/{len(item_ids)}")
    print(f"Failed: {failed}/{len(item_ids)}")

    # Print details of failed items
    if failed > 0:
        print("\nFailed items:")
        for item in results:
            if item.status == "failed":
                print(f"  ✗ Item {item.id}: {item.error}")

    return results

async def main():
    """Run the data pipeline."""
    # Process 10 items concurrently
    item_ids = list(range(1, 11))

    results = await run_pipeline(item_ids)

    # Show some successful results
    successful = [r for r in results if r.status == "completed"]
    if successful:
        print("\nSample Results:")
        for item in successful[:3]:
            print(f"  Item {item.id}: {item.raw_data} → {item.processed_data}")

if __name__ == "__main__":
    asyncio.run(main())
