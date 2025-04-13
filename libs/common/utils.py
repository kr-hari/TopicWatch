from functools import wraps
import time
import asyncio



def timer_decorator(name=None, verbose=True):
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            call_id = f"{name.upper()} - {time.time()}" if name else f"{func.__name__.upper()} - {time.time()}"
            if verbose:
                print(f"[TIMER]**** Starting async call {call_id}")
            
            start_time = time.time()
            result = await func(*args, **kwargs)
            end_time = time.time()

            elapsed_time = end_time - start_time
            if verbose:
                print(f"[TIMER]**** Async function '{func.__name__.upper()}' (Call ID: {call_id}) executed in {elapsed_time:.4f} seconds")
            return result
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            call_id = f"{name.upper()} - {time.time()}" if name.upper() else f"{func.__name__} - {time.time()}"
            if verbose:
                print(f"[TIMER]**** Starting call {call_id}")
            
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            elapsed_time = end_time - start_time
            if verbose:
                print(f"[TIMER]**** Function '{func.__name__.upper()}' (Call ID: {call_id}) executed in {elapsed_time:.4f} seconds")
            return result

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return decorator