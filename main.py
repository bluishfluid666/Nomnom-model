from fastapi import FastAPI()
app = FastAPI()
@app.get("/recommend")
async def recommend_food():
    print("hello")
    similar_foods = bettermodel.search(
      name='spaghetti',
      ingredients=['beef'],
      tags=['italian'],
      nutrition=[700, 80, 10, 50, 150, 30, 50], # NUTRITIONS = ['calories', 'fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']
      must_have_tags=True,
      must_have_all_tags=True,
      rating_important=True
    )[:20] # Take 20 most similar

    names = similar_foods['name']
    ids = similar_foods['id']
    print(ids.tolist(), names.tolist())
    return ids.tolist()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
