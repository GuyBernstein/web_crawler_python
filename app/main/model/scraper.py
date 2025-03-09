from pydantic import BaseModel
from typing import List


class ScrapeRequest(BaseModel):
    """Request model for starting a scrape operation"""
    initial_urls: List[str]


class ScrapeResponse(BaseModel):
    """Response model for scrape operation"""
    message: str


class FileListResponse(BaseModel):
    """Response model for file list operation"""
    files: List[str]


class FileContentResponse(BaseModel):
    """Response model for file content operation"""
    raw_url: str
    raw_html: str