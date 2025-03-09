from fastapi import APIRouter

# Create a router for scraper-related endpoints
router = APIRouter(
    prefix="/scraper",
    tags=["scraper"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def hello_world():
    """
    Hello World endpoint to test the API

    Returns:
        str: A hello world message
    """
    return "Hello World from URL Explorer System!"