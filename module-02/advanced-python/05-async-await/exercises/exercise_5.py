"""Exercise 5: Real-world Data Pipeline

Objective: Build an async data processing pipeline with error handling.

Instructions:
1. Complete the fetch_data() function to get data from API
2. Complete the process_data() function to transform data
3. Complete the save_data() function to save results
4. Implement error handling and retries
5. Build a complete pipeline that processes multiple items concurrently

Expected: Pipeline should handle errors gracefully and process items in parallel.

Note: This is a more complex, real-world example.
"""
import asyncio
import time
from typing import List, Optional, Any
from dataclasses import dataclass

@dataclass
class DataItem:
    """Represents a data item in our pipeline."""
    id: int
    raw_data: Optional[str] = None
    processed_data: Optional[str] = None
    status: str = "pending"
    error: Optional[str] = None

# TODO: Complete this async function with retry logic
async def fetch_data(item_id: int, fail_rate: float = 0.0) -> dict:
    """Fetch data from API with optional failure simulation.

    Args:
        item_id: ID of item to fetch
        fail_rate: Probability of failure (0.0 to 1.0) for testing

    Returns:
        Dict with fetched data
    """
    print(f"  Fetching item {item_id}...")

    # TODO: Simulate API delay
    # Hint: await asyncio.sleep(0.5)

    # TODO: Simulate occasional failures for testing
    # Hint: import random
    #       if random.random() < fail_rate:
    #           raise Exception(f"Failed to fetch item {item_id}")

    # TODO: Return fetched data
    # Hint: return {"id": item_id, "data": f"raw_data_{item_id}"}
    pass

# TODO: Complete this async function
async def process_data(data: dict) -> dict:
    """Process/transform the fetched data.

    Args:
        data: Raw data dict from fetch_data

    Returns:
        Dict with processed data
    """
    print(f"  Processing item {data['id']}...")

    # TODO: Simulate processing delay
    # Hint: await asyncio.sleep(0.3)

    # TODO: Transform the data (e.g., uppercase the string)
    # Hint: processed = data['data'].upper()
    #       return {**data, "processed": processed}
    pass

# TODO: Complete this async function
async def save_data(data: dict) -> bool:
    """Save processed data to storage.

    Args:
        data: Processed data dict

    Returns:
        True if save successful
    """
    print(f"  Saving item {data['id']}...")

    # TODO: Simulate save delay
    # Hint: await asyncio.sleep(0.2)

    print(f"  ✓ Saved item {data['id']}")
    # TODO: Return True
    pass

# TODO: Complete this async function with error handling
async def process_item(item_id: int, max_retries: int = 3) -> DataItem:
    """Process a single item through the entire pipeline.

    Args:
        item_id: ID of item to process
        max_retries: Maximum retry attempts on failure

    Returns:
        DataItem with results or error info
    """
    item = DataItem(id=item_id)

    # TODO: Implement retry logic with exponential backoff
    for attempt in range(max_retries):
        try:
            # TODO: Step 1 - Fetch data
            # Hint: raw = await fetch_data(item_id, fail_rate=0.2)
            #       item.raw_data = raw['data']

            # TODO: Step 2 - Process data
            # Hint: processed = await process_data(raw)
            #       item.processed_data = processed['processed']

            # TODO: Step 3 - Save data
            # Hint: await save_data(processed)

            # TODO: Mark as success and return
            # Hint: item.status = "completed"
            #       return item

            pass

        except Exception as e:
            # TODO: Handle errors with retry logic
            # If last attempt, mark as failed and save error
            # Otherwise, wait before retrying (exponential backoff)
            # Hint: if attempt == max_retries - 1:
            #           item.status = "failed"
            #           item.error = str(e)
            #       else:
            #           wait_time = 2 ** attempt
            #           print(f"  ⚠ Retry {attempt + 1}/{max_retries} for item {item_id} after {wait_time}s")
            #           await asyncio.sleep(wait_time)
            pass

    return item

# TODO: Complete the pipeline function
async def run_pipeline(item_ids: List[int]) -> List[DataItem]:
    """Run the complete data pipeline for multiple items.

    Args:
        item_ids: List of item IDs to process

    Returns:
        List of processed DataItems
    """
    print(f"=== Processing {len(item_ids)} items through pipeline ===\n")
    start = time.time()

    # TODO: Create tasks for all items
    # Hint: tasks = [process_item(item_id) for item_id in item_ids]

    # TODO: Run all tasks concurrently
    # Hint: results = await asyncio.gather(*tasks)

    # TODO: Calculate statistics
    elapsed = time.time() - start
    # completed = sum(1 for r in results if r.status == "completed")
    # failed = sum(1 for r in results if r.status == "failed")

    # TODO: Print summary
    # print(f"\n=== Pipeline Complete in {elapsed:.2f}s ===")
    # print(f"Successful: {completed}/{len(item_ids)}")
    # print(f"Failed: {failed}/{len(item_ids)}")

    # TODO: Print details of failed items
    # for item in results:
    #     if item.status == "failed":
    #         print(f"  ✗ Item {item.id}: {item.error}")

    # TODO: Return results
    pass

async def main():
    """Run the data pipeline."""
    # Process 10 items concurrently
    item_ids = list(range(1, 11))

    # TODO: Run the pipeline
    # Hint: results = await run_pipeline(item_ids)

    # TODO: Show some successful results
    # Print first 3 successful items with their processed data
    # successful = [r for r in results if r.status == "completed"]
    # print("\nSample Results:")
    # for item in successful[:3]:
    #     print(f"  Item {item.id}: {item.raw_data} → {item.processed_data}")
    pass

if __name__ == "__main__":
    # TODO: Run the main function using asyncio.run()
    # Hint: asyncio.run(main())
    pass
