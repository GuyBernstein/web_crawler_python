import uvicorn
import argparse
import unittest
from app import app


def run():
    """Run the FastAPI application using uvicorn"""
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )


def test():
    """Run unit tests"""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='URL Explorer System CLI')
    parser.add_argument('command', choices=['run', 'test'], help='Command to execute')

    args = parser.parse_args()

    if args.command == 'run':
        run()
    elif args.command == 'test':
        test()