#!/usr/bin/env python3

from qutescript import userscript
from time import sleep

@userscript
def hello_world(request):
    selected_html = request.selected_html
    id_loc = selected_html.find('id=')
    request.send_command('click-element id ' + selected_html[id_loc+4:id_loc+6]) 
    sleep(0.05)
    request.send_command('set input.spatial_navigation true')
    request.send_command('enter-mode insert')

if __name__ == '__main__':
    hello_world()
