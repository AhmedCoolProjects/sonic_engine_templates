from sonic_engine.core.engine import Engine


def main():

    engine = Engine((__file__, './config.yaml'))
    engine.start()


if __name__ == "__main__":
    main()
