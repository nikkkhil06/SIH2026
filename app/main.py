from fastapi import FastAPI

from app.routers import prediction, vessels, fuels, operational_data, environmental_data, fuel_prediction, optimization

from app.database.connection import engine

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI (
    title="GreenFleetQ API",
    description="Backend for SIH PS 26138",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction.router)
app.include_router(vessels.router)
app.include_router(fuels.router)
app.include_router(operational_data.router)
app.include_router(environmental_data.router)
app.include_router(fuel_prediction.router)
app.include_router(optimization.router)


@app.get("/")
def root():
    return {
        "message": "GreenFleetQ backend is running successfully!"
    }

# @app.get("/db-test")
# def database_test():
#     try:
#         with engine.connect():
#             return {
#                 "status": "success",
#                 "message": "Database connection successful"
#             }
#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }    