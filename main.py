from fastapi import FastAPI, Response

from datetime import datetime, timezone

endpoint = FastAPI()


@endpoint.get('/api')
async def get_info(slack_name: str, track: str, response: Response):
    res = {
        'slack_name': slack_name,
        'current_day': datetime.now().strftime('%A'),
        'utc_time': str(datetime.now(timezone.utc).\
                    replace(microsecond=0)).replace('+00:00', 'Z').\
                    replace(' ', 'T'),
        'track': track,
        'github_file_url': 'https://github.com/1dgidi/hngx_step1/edit/main/main.py',
        'github_repo_url': 'https://github.com/1dgidi/hngx_step1',
        'status_code': 200
    }

    return res
