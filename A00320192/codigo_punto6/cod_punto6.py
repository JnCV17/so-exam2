from slackclient import SlackClient
import cli.app
import psutil
import os
from flask import Flask, request

@cli.app.CommandLineApp
def cod_punto6(app):
    slack_token = 'xoxp-356698734240-356698734544-357190918564-49c3e5624e9da4dda1d7f74b8b7285bb' 
    sc = SlackClient(slack_token)
    sc.api_call( "chat.postMessage", channel="so-exam2",text =str(psutil.cpu_times())+"\n\n"+str(psutil.cpu_percent(interval=1, percpu=True))+"\n\n"+str(psutil.cpu_stats())+"\n\n"+str(psutil.virtual_memory())+"\n\n"+str(psutil.swap_memory())+"\n\n"+str(psutil.diskpartitions())+str(psutil.disk_usage('/'))))   

if __name__ == "__main__":
    cod_punto6.run()
