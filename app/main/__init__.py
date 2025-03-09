from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create and configure the FastAPI application"""
    app = FastAPI(
        title="URL Explorer System",
        description="A distributed web scraping system that collects URLs and their HTML content",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    return app