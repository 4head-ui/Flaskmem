from random import choice
def stonepaperknifes(user_input):
    game  = ['Камень','Ножницы','Бумага']
    comp = choice(game)
    try:
        if comp == user_input:
            return('Ничья')
        elif comp == 'Ножницы' and user_input == 'Камень':
            return(f'Выбор бота:{comp}.'
                   f'Проигрыш бота')
        elif comp == 'Камень' and user_input == 'Ножницы':
            return(f'Выбор бота:{comp}.'
                   f'Победа бота')
        elif comp == 'Бумага' and user_input == 'Камень':
            return(f'Выбор бота:{comp}.'
                   f'Победа бота')
        elif comp == 'Камень' and user_input == 'Бумага':
            return(f'Выбор бота:{comp}.'
                   f'Проигрыш бота')
        elif comp == 'Ножницы' and user_input == 'Бумага':
            return(f'Выбор бота:{comp}.'
                   f'Победа бота')
        elif comp == 'Бумага' and user_input == 'Ножницы':
            return(f'Выбор бота:{comp}.'
                   f'Проигрыш бота')
        else:
            return('Ваш ввод команды некоректен,нажмите сыграть снова')
    except Exception:
        pass






