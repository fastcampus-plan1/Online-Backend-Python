from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import time
import asyncio

app = FastAPI()

def sync_job(number: int):
    for i in range(1, number + 1):
        print(f'Job: #{number} | Task #{i}')
        time.sleep(1)
    print(f'> Job: #{number} Done!')

async def async_job(number: int):
    for i in range(1, number + 1):
        print(f'Job: #{number} | Task #{i}')
        await asyncio.sleep(1)
    print(f'> Job: #{number} Done!')


@app.get("/")
async def root():
    print('=' * 80)
    start = time.time()
    sync_job(3)
    sync_job(2)
    sync_job(1)
    end = time.time()
    print(f'>>> Processing time of sync_job: {end - start}')
    print('=' * 80)


    print('=' * 80)
    start = time.time()
    await asyncio.wait([
        asyncio.create_task(async_job(3)),
        asyncio.create_task(async_job(2)),
        asyncio.create_task(async_job(1)),
    ])
    end = time.time()
    print(f'>>> Processing time of async_job: {end - start}')
    print('=' * 80)
    
    return {"msg": "Hello World"}
