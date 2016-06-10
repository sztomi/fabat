# -*- coding: utf8 -*-
import os
import time
import wikipedia
from slackclient import SlackClient

BOT_NAME = 'wbot'

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("SLACK_BOT_ID")
# constants
AT_BOT = "<@" + BOT_ID + ">"

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def do_wikipedia(query):
    # type: (query -> str)
    return wikipedia.summary(query, sentences=3)


commands = {
    'wikipedia': do_wikipedia
}


def handle_command(command, channel):
    response = "Csillagseggű székely gyerek!"

    if ' ' in command:
        cmd, query = command.split(' ', 1)

        if cmd in commands:
            response = commands[cmd](query)

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            print(output_list)
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("wbot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
