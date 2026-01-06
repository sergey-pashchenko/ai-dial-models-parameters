from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API

run(
    # deployment_name="gpt-4o",
    # # deployment_name="anthropic.claude-3-7-sonnet-20250219-v1:0",
    # # deployment_name="anthropic.claude-sonnet-4-5-20250929-v1:0",
    # # deployment_name="anthropic.claude-sonnet-4-5-20250929-v1:0",
    deployment_name="claude-sonnet-4@20250514",
    # deployment_name="gemini-2.5-pro",
    print_request=False,  # Switch to False if you do not want to see the request in console
    print_only_content=False,  # Switch to True if you want to see only content from response
)
