import random

# Creación del deck
deck = []
suits = ['Corazón', 'Diamante', 'Pica', 'Espada']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} de {suit}')

# Hacer el deck aleatorio mediante la función random.shuffle
random.shuffle(deck)

# Obtener el nombre del jugador
player_name = input('Nombre del jugador? ')

# Iniciar el juego
while True:
    # 2 cartas para el jugador
    player_cards = [deck.pop(), deck.pop()]

    # 1 carta para la Casa
    house_cards = [deck.pop()]

    # Mostrar las cartas del jugador, y la carta de la casa
    print(f'La Casa: {house_cards[0]}')
    print(f'{player_name}: {player_cards}')

    # Turno del jugador
    while sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 if card.split()[0] in ['J', 'Q', 'K'] else 11 for card in player_cards]) <= 21:
        hit_or_stand = input(' Escribe la palabra otra para pedir carta o presiona enter para quedarte ')
        if hit_or_stand.lower() == 'otra':
            player_cards.append(deck.pop())
            print(f'{player_name}: {player_cards}')
        else:
            break

    # Turno de la casa
    while sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 if card.split()[0] in ['J', 'Q', 'K'] else 11 for card in house_cards]) < 17:
        house_cards.append(deck.pop())

    # Mostrar la mano final
    print(f'La Casa: {house_cards}')
    print(f'{player_name}: {player_cards}')

    # Determine the winner
    if sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 if card.split()[0] in ['J', 'Q', 'K'] else 11 for card in player_cards]) > 21:
        print(f'{player_name} Perdiste! La Casa gana!')
        result = 'Perdedor'


    elif sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 if card.split()[0] in ['J', 'Q', 'K'] else 11 for card in house_cards]) > 21:
        print('En hora buena! Ganaste!')
        result = 'Ganador'


    elif sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 if card.split()[0] in ['J', 'Q', 'K'] else 11 for card in player_cards]) > sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 if card.split()[0] in ['J', 'Q', 'K'] else 11 for card in house_cards]):
        print(f'{player_name} ha resultado ganador!')
        result = 'Ganador'


    elif sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 if card.split()[0] in ['J', 'Q', 'K'] else 11 for card in player_cards]) < sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 if card.split()[0] in ['J', 'Q', 'K'] else 11 for card in house_cards]):
        print('La casa gana!')
        result = 'Perdedor'