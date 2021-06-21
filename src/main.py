import os

import uvicorn

if __name__ == '__main__':
    host = os.environ.get('WEB_HOST', '0.0.0.0')
    port = int(os.environ.get('WEB_PORT', 8080))
    uvicorn.run(
        'webconnector.app:app',
        host=host,
        port=port,
        log_level='info',
        reload=True
    )