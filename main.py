from cesarCipher import CeasarCipher
from console.Console import Color
from game import GameRPS
from game.GameRPS import Player


def main():
    # Cesar cipher
    print(Color.BOLD + "CESAR CIPHER" + Color.END)
    message = "hi, how are you?"
    key = 825
    # Encoding
    print(f"{Color.UNDERLINE}Encoding:{Color.END}")
    print(f"\tEncrypting message {Color.BOLD}{message}{Color.END} with key {Color.BOLD}{key}{Color.END}")
    encrypted_message = CeasarCipher.encode(message, key)
    print(f"\tEncrypted message is {Color.BOLD}{encrypted_message}{Color.END}")
    #Decoding
    print(f"{Color.UNDERLINE}Decoding:{Color.END}")
    print(f"\tDecrypting message {Color.BOLD}{encrypted_message}{Color.END} with key {Color.BOLD}{key}{Color.END}")
    decrypted_message = CeasarCipher.decode(encrypted_message, key)
    print(f"\tDecrypted message is {Color.BOLD}{decrypted_message}{Color.END}")

    print("\n\n")
    # Rock, paper, scissors
    print(Color.BOLD + "ROCK, PAPER, SCISSORS GAME" + Color.END)
    player1 = Player(0.1, 0.4, 0.5)
    player2 = Player(0.3, 0.3, 0.4)
    GameRPS.play_rsp(player1, player2, 3)


if __name__ == "__main__":
    main()
