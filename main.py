from fastapi import FastAPI

app = FastAPI()


products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1200,
        "category": "electronics"
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 80,
        "category": "electronics"
    },
    {
        "id": 3,
        "name": "Python Book",
        "price": 40,
        "category": "book"
    }
]


@app.get("/")
def home():
    return {"message": "Mini Products API"}

 

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}


@app.get("/products")
def get_products(category: str | None = None):

    if category is None:
        return products

    result = []

    for product in products:

        if product["category"].casefold() == category.casefold():
            result.append(product)

    return result