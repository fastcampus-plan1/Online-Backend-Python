async def get_food(food_id: int):
    foods = ["burger", "pizza", "pasta"]
    return foods[food_id]

@app.get('/food/{food_id}')
async def read_food(food_id: int):
    food = await get_food(food_id)
    return food
