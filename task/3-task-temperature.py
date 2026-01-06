from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

run(
    # deployment_name="gpt-4o",
    # deployment_name="claude-sonnet-4@20250514",
    deployment_name="gemini-2.5-pro",
    print_only_content=True,
    # print_only_content=False,
    # TODO:
    #  Use `temperature` parameter with value in range from 0.0 to 1.0!
    #  (Optional) Use `temperature` parameter with value 2.1 and check what happens
    # temperature=0.0,
    # temperature=1.5,
    temperature=1.7,
    # temperature=1.75,
    # n=3,
)
