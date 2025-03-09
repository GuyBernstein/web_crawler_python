from app.main import create_app
from app.main.controller.scraper_controller import router as scraper_router

# Create the FastAPI application
app = create_app()

# Register the routers
app.include_router(scraper_router)