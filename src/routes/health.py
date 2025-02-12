from fastapi import APIRouter

router =APIRouter(prefix='/health');

@router.get('/ready')
def ready():
    return {'status': 'ok'}

@router.get('/live')
def live():
    return {'status': 'ok'}
