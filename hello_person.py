

def hello(name, lang):
    greetings={
        "Spanish":"Halo",
        "English": "Hello",
        "Arabic": "Ahlan",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description= "Provide personal Greetings!"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet"
    )
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["Spanish","English","Arabic"],
        help="The language of greetings."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)