from sys import argv

script, user_name=argv
prompt = '>'

print(f"Hi {user_name}, I'm {script} script.")
print(f"I'd like 2 ask u a few Q.")
print(f"Do u like me {user_name}?")
likes =input(prompt)

print(f"Where do u live {user_name}?")
lives =input(prompt)

print(f"What kinds of computer do u have?")
computer =input(prompt)

print(f"""
        Alright,so u said {likes} about liking me.
        You alive in {lives}.Not sure where that is.
        And u have a {computer} computer.Nice.
        """)
