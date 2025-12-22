import uvicorn

from volcan.settings import settings


def main():
    uvicorn.run('volcan.app:app',
                host=settings.server_host,
                port=settings.server_port,
                reload=True)


if __name__ == "__main__":
    main()
