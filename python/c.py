import signal


def handler(sig, frame):
    print(f"sig: {sig}")
    print(f"frame: {frame}")


if __name__ == "__main__":
    signal.signal(signal.SIGTSTP, handler)
    signal.pause()