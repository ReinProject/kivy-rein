"""Provides functionality for the MainScreen view"""

from functionality.Setting import Setting
from functionality.queries import get_active_jobs

def view_active_job(job, screen_manager):
    screen_manager.current = 'JobScreen'
    job_screen = screen_manager.get_screen('JobScreen')

    # Set job name label
    job_screen.ids['job_name'].text = job['name']
    
    # Determine job status
    job_status = ''
    if 'delivery_accepted' in job:
        job_status = 'Delivery has been accepted'

    elif 'dispute' in job:
        if 'resolution' in job['dispute']:
            job_status = 'Dispute has been resolved'

        else:
            job_status = "Dispute in progress"

    elif 'delivery' in job:
        job_status = 'Delivery has been made'

    elif 'offer' in job:
        job_status = 'Job is in progress'

    elif 'bid' in job:
        job_status = 'Bids have been made'

    else:
        job_status = "As yet, there are no bids"

    job_screen.ids['job_status'].text = job_status

def set_user_job_data(screen_manager):
    main_screen = screen_manager.get_screen('MainScreen')
    main_screen.ids['rv_active'].data = [{'value': item['name'], 'job': item} for item in get_active_jobs(Setting.read('delprivkey'))]
